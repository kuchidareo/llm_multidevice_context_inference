import os

opportunity_index_to_locomotion_label = {
    0: "0",
    1: "Stand",
    2: "Walk",
    3: "Sit",
    4: "Lie"
}

opportunity_index_to_gesture_label = {
    0: "0",
    1: "Open Door 1",
    2: "Open Door 2",
    3: "Close Door 1",
    4: "Close Door 2",
    5: "Open Fridge",
    6: "Close Fridge",
    7: "Open Dishwasher",
    8: "Close Dishwasher",
    9: "Open Drawer 1",
    10: "Close Drawer 1",
    11: "Open Drawer 2",
    12: "Close Drawer 2",
    13: "Open Drawer 3",
    14: "Close Drawer 3",
    15: "Clean Table",
    16: "Drink from Cup",
    17: "Toggle Switch"
}

def calculate_cnn_misclassification_trend(label):
    if label == "locomotion":
        confusion_matrix = opportunity_cnn_locomotion_confusion_matrix
        index_to_label = opportunity_index_to_locomotion_label
    elif label == "gesture":
        confusion_matrix = opportunity_cnn_gesture_confusion_matrix
        index_to_label = opportunity_index_to_gesture_label

    regular_matrix = [[0 for _ in range(len(confusion_matrix))] for _ in range(len(confusion_matrix[0]))]
    misclassify_trend = []
    total_proportion = 0

    for i, row in enumerate(confusion_matrix):
        num_total = sum(row)
        for j, value in enumerate(row):
            if i == j:
                regular_matrix[i][j] = 0
            else:
                regular_matrix[i][j] = value / num_total
                total_proportion += value / num_total

    for i, row in enumerate(regular_matrix):
        for j, value in enumerate(row):
            probability = value / total_proportion
            if probability > 0.0:
                misclassify_trend.append([index_to_label[i], index_to_label[j], probability])
    return misclassify_trend

## TODO: Add explanation for this matrix.
opportunity_cnn_locomotion_confusion_matrix = [
    [1200, 0, 0, 0, 0],
    [2, 1188, 23, 0, 0],
    [1, 0, 706, 11, 0],
    [0, 0, 3, 589, 1],
    [0, 0, 0, 1, 247],
]
opportunity_cnn_gesture_confusion_matrix = [
    [4297, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 96, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 79, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 35, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 30, 1, 0, 0, 0, 5, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 2, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 17, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 24, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 205, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 20],
]

## TODO: Add experiment_type to the filename
def generate_filename(dataset_config, misclassification_config, ex_type, gpt_model, trial):
        dataset_name = dataset_config.dataset_name
        target_labels = str(misclassification_config.target_labels)
        mislabeling_mode = misclassification_config.mislabeling_mode
        num_label_duplication = misclassification_config.num_label_duplication
        num_label_mislabeling = misclassification_config.num_label_mislabeling
        mislabeling_rate = misclassification_config.mislabeling_rate

        filename = f"{dataset_name}_{gpt_model}_{ex_type}_{mislabeling_mode}_{target_labels}_{num_label_duplication}_{num_label_mislabeling}_{mislabeling_rate}_{trial}"
        return filename

def export_csv(df, output_dir, filename):
    df.to_csv(os.path.join(output_dir, f"{filename}.csv"), index=False)

def export_llm_conversation(conversation, output_dir, filename):
    with open(os.path.join(output_dir, f"{filename}.md"), "w") as f:
        for utterance in conversation:
            f.write(f"### {utterance['role']}\n")
            f.write(f"{utterance['content']}\n")