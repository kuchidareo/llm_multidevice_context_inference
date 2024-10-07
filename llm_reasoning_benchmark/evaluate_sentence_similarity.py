from collections import defaultdict
import os

from sentence_transformers import SentenceTransformer, util
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from static import UCI_ex_result_annotation


class SentenceSimilarity:
    pca_components = 2

    def __init__(self, base_sentence, sentence_list, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.base_sentence = base_sentence
        self.sentence_list = sentence_list
        self.cosine_similarity_list = []

    def get_cosine_similarity(self, sentence1, sentence2):
        embedding1 = self.model.encode(sentence1, convert_to_tensor=True)
        embedding2 = self.model.encode(sentence2, convert_to_tensor=True)

        cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
        return cosine_scores

    def get_pca_embedding(self):
        pca = PCA(n_components=self.pca_components)
        embedding_list = [self.model.encode(sentence, convert_to_tensor=True).cpu() for sentence in self.sentence_list]  
        pca.fit(embedding_list)
        return pca.transform(embedding_list)
    
    def get_cosine_similarity_list(self):
        for sentence in self.sentence_list:
            self.cosine_similarity_list.append(self.get_cosine_similarity(sentence, self.base_sentence))
        return self.cosine_similarity_list
    
    def make_plot(self, annotation, ex_tag, model, rate, xlabel, ylabel):
        pca_embedding = self.get_pca_embedding()
        title = f"{ex_tag}_{model}_{rate}"

        plt.scatter(0.0, 0.0, c="blue")
        plt.annotate(f'baseline', (0.0, 0.0))

        for i in range(len(self.sentence_list)):
            color = "blue" if annotation[ex_tag][model][rate][i] else "red"
            plt.scatter(pca_embedding[i, 0], pca_embedding[i, 1], c=color)
            plt.annotate(f'trial: {i+1}', (pca_embedding[i, 0], pca_embedding[i, 1]))

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(os.path.join("ex_result", ex_tag, "pca_fig", f"{title}.png"))
        plt.show()

    
def extract_sentence_list(base_sentence_path, path_list):
    sentence_list = []
    with open(base_sentence_path, 'r') as file:
        lines = str(file.readlines())
        start_index = lines.find('### assistant') + 1
        end_index = lines.rfind('### user')
        base_sentence = str([line.strip() for line in lines[start_index:end_index]])

    for path in path_list:
        print(path)
        with open(path, 'r') as file:
            lines = str(file.readlines())
            start_index = lines.find('### assistant') + 1
            end_index = lines.rfind('### user')
            sentence_list.append(str([line.strip() for line in lines[start_index:end_index]]))

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
model = "gpt-4o-2024-08-06"
rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

base_sentence_path = os.path.join('ex_result', 'baseline_story', "S1-ADL1.dat_gpt-4o-2024-08-06_1_['locomotion']_swim_random_1_0.0_1.md")


def main():
    cosine_similarity_list = defaultdict(list)
    for rate in rates: 
        path_list = get_path_list(ex_tag, model, rate)
        base_sentence, sentence_list = extract_sentence_list(base_sentence_path, path_list)
        similarity = SentenceSimilarity(base_sentence, sentence_list)
        similarity.make_plot(
            UCI_ex_result_annotation,
            ex_tag=ex_tag,
            model=model,
            rate=rate,
            xlabel="PCA 1",
            ylabel="PCA 2"
        )
        cosine_similarity_list[rate] = similarity.get_cosine_similarity_list()

    print(cosine_similarity_list)

if __name__ == "__main__":
    main()