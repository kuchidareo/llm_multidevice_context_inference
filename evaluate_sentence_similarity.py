import csv
import os

from sentence_transformers import SentenceTransformer, util
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from openai import OpenAI
import torch

from static import UCI_ex_result_annotation


class TextSimilarityAnalysis:
    pca_components = 2

    def __init__(self, base_sentence, sentence_list, model_name):
        self.model_type = None
        if model_name == "all-MiniLM-L6-v2":
            self.model = SentenceTransformer(f"sentence-transformers/{model_name}")
            self.model_type = "sentence-transformer"
        elif model_name == "text-embedding-3-small":
            self.model = "text-embedding-3-small"
            self.model_type = "openai-embeddings"

        self.base_sentence = base_sentence
        self.sentence_list = sentence_list
        self.cosine_similarity_list = []

    def get_cosine_similarity(self, sentence1, sentence2):
        if self.model_type == "sentence-transformer":
            embedding1 = self.model.encode(sentence1, convert_to_tensor=True)
            embedding2 = self.model.encode(sentence2, convert_to_tensor=True)
        elif self.model_type == "openai-embeddings":
            embedding1 = client.embeddings.create(input=[sentence1], model=self.model).data[0].embedding
            embedding2 = client.embeddings.create(input=[sentence2], model=self.model).data[0].embedding

        cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
        return float(cosine_scores.cpu())
    
    def get_embedding(self):
        if self.model_type == "sentence-transformer":
            embedding_list = [self.model.encode(self.base_sentence, convert_to_tensor=True).cpu()]
            embedding_list.extend([self.model.encode(sentence, convert_to_tensor=True).cpu() for sentence in self.sentence_list])
        elif self.model_type == "openai-embeddings":
            embedding_list = [client.embeddings.create(input=[self.base_sentence], model=self.model).data[0].embedding]
            embedding_list.extend([client.embeddings.create(input=[sentence], model=self.model).data[0].embedding for sentence in self.sentence_list])

        return {"baseline": embedding_list[0], "sentence": embedding_list[1:]}

    def get_pca_embedding(self):
        pca = PCA(n_components=self.pca_components)
        if self.model_type == "sentence-transformer":
            embedding_list = [self.model.encode(self.base_sentence, convert_to_tensor=True).cpu()]
            embedding_list.extend([self.model.encode(sentence, convert_to_tensor=True).cpu() for sentence in self.sentence_list])
        elif self.model_type == "openai-embeddings":
            embedding_list = [client.embeddings.create(input=[self.base_sentence], model=self.model).data[0].embedding]
            embedding_list.extend([client.embeddings.create(input=[sentence], model=self.model).data[0].embedding for sentence in self.sentence_list])

        pca.fit(embedding_list)
        pca_list = pca.transform(embedding_list)
        return {"baseline": pca_list[0], "sentence": pca_list[1:]}
    
    def get_cosine_similarity_list(self):
        for sentence in self.sentence_list:
            self.cosine_similarity_list.append(self.get_cosine_similarity(sentence, self.base_sentence))
        return self.cosine_similarity_list
    
    def make_pca_plot(self, pca_embedding, annotation, title, ex_tag, xlabel, ylabel):
        plt.scatter(pca_embedding["baseline"][0], pca_embedding["baseline"][1], c="blue")
        plt.annotate(f'baseline', (pca_embedding["baseline"][0], pca_embedding["baseline"][1]))

        for i in range(len(self.sentence_list)):
            color = "blue" if annotation[i] else "red"
            plt.scatter(pca_embedding["sentence"][i, 0], pca_embedding["sentence"][i, 1], c=color)
            plt.annotate(f'trial: {i+1}', (pca_embedding["sentence"][i, 0], pca_embedding["sentence"][i, 1]))

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(os.path.join("ex_result", ex_tag, "pca_fig", f"{title}.png"))
        plt.show()

    def export_pca_embedding_to_csv(self, pca_embedding, annotation, title, ex_tag):
        csv_path = os.path.join("log_for_paper_figures", ex_tag, "pca_embedding", f"{title}.csv")
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Trial', 'Color', 'PCA_X', 'PCA_Y'])
            writer.writerow(["baseline", "blue", pca_embedding["baseline"][0], pca_embedding["baseline"][1]])
            for i, embedding in enumerate(pca_embedding["sentence"]):
                color = "blue" if annotation[i] else "red"
                writer.writerow([i+1, color, embedding[0], embedding[1]])

    def export_cosine_similarity_to_csv(self, cosine_similarity, annotation, title, ex_tag):
        csv_path = os.path.join("log_for_paper_figures", ex_tag, "cosine_similarity", f"{title}.csv")
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Trial', 'Color', 'Cosine Similarity'])
            writer.writerow(["baseline", "blue", 1])
            for i, similarity in enumerate(cosine_similarity):
                color = "blue" if annotation[i] else "red"
                writer.writerow([i+1, color, similarity])
    
    def export_embedding(self, embedding, title, ex_tag):
        torch.save(embedding["baseline"], os.path.join('log_for_paper_figures', ex_tag, "embedding", f"{title}_baseline_embedding.pt"))
        for i, sentence in enumerate(embedding["sentence"]):
            torch.save(sentence, os.path.join(os.path.join('log_for_paper_figures', ex_tag, 'embedding', f"{title}_trial_{i+1}_embedding.pt")))

    def make_cosine_similarity_plot(self, cosine_similarity, annotation, title, ex_tag, xlabel, ylabel):
        # Create a bar plot with color based on UCI_ex_annotation
        for i in range(len(self.sentence_list)):
            color = "blue" if annotation[i] else "red"
            plt.bar(i+1, cosine_similarity[i], color=color)

        # Add title and labels
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        # Show the plot
        plt.savefig(os.path.join("ex_result", ex_tag, "cosine_dist_fig", f"{title}.png"))
        plt.show()


def extract_sentence_list(base_sentence_path, path_list):
    sentence_list = []
    with open(base_sentence_path, 'r') as file:
        lines = str(file.readlines())
        start_index = lines.find('### assistant') + 1
        end_index = lines.rfind('### user')
        base_sentence = str(lines[start_index:end_index].strip())

    for path in path_list:
        with open(path, 'r') as file:
            lines = str(file.readlines())
            start_index = lines.find('### assistant') + 1
            end_index = lines.rfind('### user')
            sentence_list.append(str(lines[start_index:end_index].strip()))

    return base_sentence, sentence_list

def get_path_list(ex_tag, model, rate):
    path_list = []
    for file in os.listdir(os.path.join('ex_result', ex_tag)):
        if f"_{model}_" in file and f"_{rate}_" in file:
            trial_number = file.split("_")[-1].split(".")[0]
            new_trial_number = trial_number.zfill(2)
            new_file_name = file.replace(f"_{trial_number}.md", f"_{new_trial_number}.md")
            os.rename(os.path.join('ex_result', ex_tag, file), os.path.join('ex_result', ex_tag, new_file_name))
            path_list.append(os.path.join('ex_result', ex_tag, new_file_name))
    return sorted(path_list)


ex_tag = "story_correction" # binary_choice, story_correction, seq_story_correction
model = "gpt-4o-2024-08-06" # gpt-4o-2024-08-06, gpt-4o-mini, gpt-3.5-turbo
embedding_model = "text-embedding-3-small" # all-MiniLM-L6-v2, text-embedding-3-small
rates = [0.1]

base_sentence_path = os.path.join('ex_result', 'baseline_story', "S1-ADL1.dat_gpt-4o-2024-08-06_1_['locomotion']_swim_random_1_0.0_1.md")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    cosine_similarity = {}
    for rate in rates: 
        path_list = get_path_list(ex_tag, model, rate)

        base_sentence, sentence_list = extract_sentence_list(base_sentence_path, path_list)
        text_similarity_analysis = TextSimilarityAnalysis(base_sentence, sentence_list, model_name=embedding_model)
        title = f"{ex_tag}_{embedding_model}_{model}_{rate}"
        cosine_similarity[rate] = text_similarity_analysis.get_cosine_similarity_list()
        annotation = UCI_ex_result_annotation[ex_tag][model][rate]
        embedding = text_similarity_analysis.get_embedding()
        pca_embedding = text_similarity_analysis.get_pca_embedding()

        # text_similarity_analysis.make_pca_plot(
        #     pca_embedding,
        #     annotation,
        #     title,
        #     ex_tag,
        #     xlabel="PCA 1",
        #     ylabel="PCA 2"
        # )

        # text_similarity_analysis.make_cosine_similarity_plot(
        #     cosine_similarity[rate],
        #     annotation,
        #     title,
        #     ex_tag,
        #     xlabel="Trial ID",
        #     ylabel="Cosine Distance",
        # )

        # For zhigang analysis
        # text_similarity_analysis.export_pca_embedding_to_csv(pca_embedding, annotation, title, ex_tag)
        # text_similarity_analysis.export_cosine_similarity_to_csv(cosine_similarity[rate], annotation, title, ex_tag)
        text_similarity_analysis.export_embedding(embedding, title, ex_tag)

if __name__ == "__main__":
    main()