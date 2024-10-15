import csv
import os

import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
import torch

from static import UCI_ex_result_annotation, UCI_activity_durations
from avg_result import misclassification_avg_result, fuse_avg_result

# Import the all csv data from story_correction/cosine_similarity dir.
# The file name contains the poisoning rate. e.g. story_correction_text-embedding-3-small_gpt-4o-2024-08-06_0.1.csv
def import_csv_data(ex_tag):
    data = {}
    for file in os.listdir(f"{ex_tag}/cosine_similarity"):
        model = file.split("_")[3]
        poisoning_rate = file.split("_")[-1].replace(".csv", "")
        if model not in data:
            data[model] = {}
        if poisoning_rate not in data[model]:
            data[model][poisoning_rate] = []

        if file.endswith(".csv"):
            with open(f"{ex_tag}/cosine_similarity/{file}", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    data[model][poisoning_rate].append(row)
        data[model] = {k: v for k, v in sorted(data[model].items(), key=lambda item: item[0])}
        
    return data

# import embedding data model -> poisoning_rate -> baseline or sentence -> embedding
# the embedding list is ordered by the trial number.
def import_embedding_data(ex_tag):
    data = {}
    for file in os.listdir(f"{ex_tag}/embedding"):
        model = file.split("_")[3]
        embedding_model = file.split("_")[2]
        poisoning_rate = file.split("_")[4]
        trial_number = file.split("_")[-2]
        if model not in data:
            data[model] = {}
        if poisoning_rate not in data[model]:
            data[model][poisoning_rate] = {}
        if "sentence" not in data[model][poisoning_rate]:
            data[model][poisoning_rate]["sentence"] = []
        if "baseline" not in data[model][poisoning_rate]:
            data[model][poisoning_rate]["baseline"] = []

        if file.endswith(".pt"):
            if trial_number == "baseline":
                data[model][poisoning_rate]["baseline"] = torch.load(f"{ex_tag}/embedding/{file}")
            else:
                # Append the loaded tensor and sort the list by trial_number
                data[model][poisoning_rate]["sentence"].append((trial_number, embedding_model, torch.load(f"{ex_tag}/embedding/{file}")))
                data[model][poisoning_rate]["sentence"].sort(key=lambda x: x[0])  # Sort by trial_number

    # Make a sorted list from data. Ordered by model -> poisoning_rate -> sentence
    model_order = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-2024-08-06"]
    returning_list = []
    returning_list.append(data["gpt-3.5-turbo"]["0.1"]["baseline"])
    for model in model_order:
        for rate in data[model].keys():
            for sentence in data[model][rate]["sentence"]:
                returning_list.append(sentence[2])
    
    index_to_content = {}
    index_to_content[0] = "baseline"
    index = 1

    for model in model_order:
        for rate in data[model].keys():
            for sentence in data[model][rate]["sentence"]:
                index_to_content[index] = f"{ex_tag}_{sentence[1]}_{model}_{rate}_{sentence[0]}"
                index += 1
    
    return returning_list, index_to_content

def import_measure_activity_duration_csv_file(ex_tag):
    data = {}
    with open (f"{ex_tag}/log.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == "gpt_model":
                continue
            model, rate, trial = row[1], row[2], row[3]
            cleanup, coffee_time, early_morning, relaxing, sandwich_time = row[-5], row[-4], row[-3], row[-2], row[-1]

            if model not in data:
                data[model] = {}
            if rate not in data[model]:
                data[model][rate] = []
            
            data[model][rate].append((trial, {"Relaxing": relaxing, "Coffee-time": coffee_time, "Early-morning": early_morning, "Cleanup": cleanup, "Sandwich-time": sandwich_time}))
            data[model][rate].sort(key=lambda x: x[0])
    return data

# Make box figure of accuracy on the different rate of poisoning .
def make_cosine_similarity_box_figure():
    ex_tag = "story_correction"
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-2024-08-06"]
    for model in models:
        data = import_csv_data(ex_tag)[model]
        cosine_similarity = {rate: [] for rate in data.keys()}  # Initialize with empty lists for each rate
        for rate, rows in data.items():
            for row in rows:
                if row[0] == "Trial" or row[0] == "baseline":
                    continue
                cosine_similarity[rate].append(float(row[2]))  # Collect cosine similarities for each rate

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.boxplot(cosine_similarity.values())
        ax.set_xticklabels([f"{rate}" for rate in cosine_similarity.keys()])
        ax.set_ylabel("Cosine Similarity")
        ax.set_title("Cosine Similarity of Story Correction")
        plt.savefig("box_figure.png")
        plt.show()

# Make a line plot of accuracy on the story_correction ex.
def make_line_plot_of_accuracy():
    ex_tag = "story_correction"
    data = import_csv_data(ex_tag)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for model, rows in data.items():
        accuracy = {rate: [] for rate in rows.keys()}  # Initialize with empty lists for each rate
        for rate, rows in rows.items():
            for row in rows:
                if row[0] == "Trial" or row[0] == "baseline":
                    continue
                if row[1] == "blue":
                    accuracy[rate].append(1)
                elif row[1] == "red":
                    accuracy[rate].append(0)
            accuracy[rate] = sum(accuracy[rate]) / len(accuracy[rate])  # Calculate accuracy for each rate
        ax.plot(accuracy.keys(), accuracy.values(), "-o", label=model)

    ax.set_xlabel("Poisoning Rate")
    ax.set_ylabel("Accuracy")
    ax.legend()
    ax.set_title("Accuracy of Story Correction")
    plt.savefig("line_acc_plot_all_models.png")
    plt.show()

def make_line_plot_of_cosine_similarity():
    ex_tag = "story_correction"
    data = import_csv_data(ex_tag)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for model, rows in data.items():
        cosine_similarity = {rate: [] for rate in rows.keys()}
        for rate, rows in rows.items():
            for row in rows:
                if row[0] == "Trial" or row[0] == "baseline":
                    continue
                cosine_similarity[rate].append(float(row[2]))
            cosine_similarity[rate] = sum(cosine_similarity[rate]) / len(cosine_similarity[rate])
        ax.plot(cosine_similarity.keys(), cosine_similarity.values(), "-o", label=model)
    ax.set_xlabel("Poisoning Rate")
    ax.set_ylabel("Cosine Similarity")
    ax.legend()
    ax.set_title("Cosine Similarity of Story Correction")
    plt.savefig("line_plot_all_models.png")
    plt.show()

def make_pca_plot():
    ex_tag = "story_correction"
    embedding, index_to_content = import_embedding_data(ex_tag)

    pca = PCA(n_components=2)
    pca.fit(embedding)
    pca_list = pca.transform(embedding)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    baseline = pca_list[0]
    ax.scatter(baseline[0], baseline[1], c="blue")
    ax.annotate(f'baseline', (baseline[0], baseline[1]))

    # index_to_content = {1: 'story_correction_text-embedding-3-small_gpt-3.5-turbo_0.1_1}...
    for i in range(1, len(pca_list)):
        content = index_to_content[i]
        model = content.split("_")[3]
        rate = content.split("_")[4]
        trial = content.split("_")[-1]
        annotation = UCI_ex_result_annotation[ex_tag][model][float(rate)]

        color = "blue" if annotation[int(trial)-1] else "red"
        ax.scatter(pca_list[i][0], pca_list[i][1], c=color)
        ax.annotate(f'{model}', (pca_list[i][0], pca_list[i][1]))

    ax.set_xlabel("PCA1")
    ax.set_ylabel("PCA2")
    ax.set_title("PCA of Story Correction")
    plt.savefig("pca_plot.png")
    plt.show()

def make_activity_duration_box_plot():
    ex_tag = "measure_activity_duration_fuse"
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-2024-08-06"] # gpt-3.5-turbo, gpt-4o-mini, gpt-4o-2024-08-06
    activity_labels = ["Relaxing", "Coffee-time", "Early-morning", "Cleanup", "Sandwich-time"] # Relaxing, Coffee-time, Early-morning, Cleanup, Sandwich-time
    
    for model in models:
        for activity_label in activity_labels:
            data = import_measure_activity_duration_csv_file(ex_tag)[model]
            
            durations = {rate: [] for rate in data.keys()}  # Initialize with empty lists for each rate
            durations["label"] = [UCI_activity_durations[activity_label] for _ in range(5)]
            for rate, rows in data.items():
                for row in rows:
                    if row[1][activity_label] == "":
                        continue
                    durations[rate].append(float(row[1][activity_label]))  # Collect cosine similarities for each rate

            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.boxplot(durations.values())
            ax.set_xticklabels([f"{rate}" for rate in durations.keys()])
            ax.set_ylabel("Duration")
            # ax.set_title(f"{model}_{activity_label}_Activity Duration")
            ax.set_title(f"{model}_{activity_label}_Activity Duration [Swim & Hand Shake]")
            plt.savefig(f"{ex_tag}/{model}_{activity_label}.png")
            plt.show()

def make_activity_duration_box_plot_with_all_activities():
    ex_tag = "measure_activity_duration"
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-2024-08-06"] # gpt-3.5-turbo, gpt-4o-mini, gpt-4o-2024-08-06
    rate_extract = "0"
    activity_labels = ["Relaxing", "Coffee-time", "Early-morning", "Cleanup", "Sandwich-time"] # Relaxing, Coffee-time, Early-morning, Cleanup, Sandwich-time

    csv_path = os.path.join(ex_tag, "activity_duration_0.0_baseline.csv")
    with open(csv_path, mode='w', newline='') as file:
        for model in models:
            data = import_measure_activity_duration_csv_file(ex_tag)[model]
            durations = {activity_label: [] for activity_label in activity_labels}
            for activity_label in activity_labels:
                for rate, rows in data.items():
                    if rate == rate_extract:
                        for row in rows:
                            if row[1][activity_label] == "":
                                continue
                            durations[activity_label].append(float(row[1][activity_label]))  # Collect cosine similarities for each rate
            
            fig = plt.figure(figsize=(7,7)) 
            ax = fig.add_subplot(111)
            ax.boxplot(durations.values())

            writer = csv.writer(file)
            writer.writerow(['Model', 'activity_label', 'activity_duration'])
            for label, duration in durations.items():
                for value in duration:
                    writer.writerow([f"{model}", f"{label}", value])

            ax.set_xticklabels([activity_label for activity_label in durations.keys()], rotation=45, fontsize=8)
            ax.set_ylabel("Duration(s)", fontsize=12)
            # ax.set_title(f"{model}_{activity_label}_Activity Duration [Swim & Hand Shake]")
            plt.savefig(f"{ex_tag}/all_activities_{model}.png")
            plt.show()

def make_activity_duration_box_plot_with_all_activities_multiple():
    ex_tag = "measure_activity_duration"
    csv_path = os.path.join(ex_tag, "activity_duration_0.0_baseline.csv")
    df = pd.read_csv(csv_path)
    sns.set(font_scale=1.6)
    sns.set_style("whitegrid")
    plt.rcParams['figure.subplot.left'] = 0.17
    plt.rcParams['figure.subplot.bottom'] = 0.23
    
    sns.boxplot(x='activity_label', y='activity_duration', hue="Model", data=df)
    plt.xlabel("")
    plt.xticks(rotation=30)
    plt.ylabel("Duration(s)")
    plt.savefig("activity_duration_0.0_baseline_test.png")
    plt.show()

def make_cosine_similarity():
    ex_tag = "measure_activity_duration"
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o"]
    csv_path = os.path.join(ex_tag, "misclassification_ex_cosine_similarity.csv")
    df = pd.read_csv(csv_path)
    sns.set(font_scale=1.6)
    sns.set_style("whitegrid")

    sns.lineplot(
        x="Rate",
        y="cosine similarity",
        hue="Model",
        style="Model",
        data=df,
        markers=True,
        dashes=False
    )
    plt.show()

def calculate_cosine_similarity(a, b):
    return float(np.dot(a, b) / (norm(a) * norm(b)))


def make_cosine_similarity_misclassification_plot():
    ex_tag = "measure_activity_duration"
    models = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4o-2024-08-06"]
    correct_duration = [57, 178, 349, 160, 319]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    csv_path = os.path.join(ex_tag, "misclassification_ex_cosine_similarity.csv")
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model', 'Rate', 'cosine similarity'])
        for model in models:
            if ex_tag == "measure_activity_duration":
                data = misclassification_avg_result[model]
            elif ex_tag == "measure_activity_duration_fuse":
                data = fuse_avg_result[model]
            
            cosine_similarity_dict = {}
            for rate, row in data.items():
                cosine_similarity_dict[rate] = calculate_cosine_similarity(correct_duration, row)
                writer.writerow([f"{model}", f"{rate}", cosine_similarity_dict[rate]])
            ax.plot(cosine_similarity_dict.keys(), cosine_similarity_dict.values(), "-o", label=model)

    ax.set_xlabel("Misclassification Rate")
    ax.set_ylabel("Cosine Similarity")
    ax.legend()
    plt.savefig("cosine_similarity_misclassification.png")
    # plt.savefig("cosine_similarity_fuse.png")

    plt.show()
    

def main():
    # make_cosine_similarity_box_figure()
    # make_line_plot_of_accuracy()
    # make_line_plot_of_cosine_similarity()
    # make_pca_plot()
    # make_activity_duration_box_plot()
    # make_activity_duration_box_plot_with_all_activities()
    # make_cosine_similarity_misclassification_plot()
    # make_activity_duration_box_plot_with_all_activities_multiple()
    make_cosine_similarity()

if __name__ == "__main__":
    main()