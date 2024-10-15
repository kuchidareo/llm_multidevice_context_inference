import random

from omegaconf import DictConfig
import pandas as pd

from utils import calculate_cnn_misclassification_trend

class MislabelingProcessor():
    def __init__(self):
        self.indices_to_mislabel = []

    def mislabeling(self, df, mislabeling_mode, target_labels, mislabeling_rate, num_label_duplication, num_label_mislabeling, metadata):
        for label in target_labels:
            num_row_mislabeling = int(len(df[df[f"{label}_label_0"] != "0"]) * mislabeling_rate)
            mislabeling_column_index = random.sample(range(num_label_duplication), num_label_mislabeling)

            for col_index in mislabeling_column_index:
                if label == "locomotion":
                    misclassification_trend = calculate_cnn_misclassification_trend(label)
                    values = metadata.locomotion_label_values
                    fused_mislabel_value = metadata.locomotion_fused_mislabel
                elif label == "gesture":
                    misclassification_trend = calculate_cnn_misclassification_trend(label)
                    values = metadata.gesture_label_values
                    fused_mislabel_value = metadata.gesture_fused_mislabel

                misclassifications = random.choices(
                    misclassification_trend,
                    weights=[row[2] for row in misclassification_trend],
                    k=num_row_mislabeling
                )
                if mislabeling_mode == "wild":
                    for target, mislabel, _ in misclassifications:
                        self.apply_label_change(df, label, col_index, target, mislabel, values)
                elif mislabeling_mode == "fused":
                    for target, _, _ in misclassifications:
                        self.apply_label_change(df, label, col_index, target, fused_mislabel_value, values)

        return df

    def apply_label_change(self, df, label, col_index, target_value, mislabel_value, attack_labels):
        is_changed = False
        while not is_changed:
            target_row_indexes = df[df[f"{label}_label_{col_index}"] == target_value].index
            if not target_row_indexes.empty:
                target_row_index = random.choice(target_row_indexes)
                df.loc[target_row_index, f"{label}_label_{col_index}"] = mislabel_value
                print(f"index: {target_row_index}, {label}_label_{col_index}: {target_value} -> {mislabel_value}")
                is_changed = True
                self.indices_to_mislabel.append(target_row_index)
            else:
                print(f"No instances of {target_value} found in column {label}_label_{col_index}")
                target_value = random.choice(attack_labels)
                while target_value in ["0", mislabel_value]:
                    target_value = random.choice(attack_labels)

def apply_mislabeling(
    df: pd.DataFrame,
    mislabeling_config: DictConfig,
    dataset_name: str,
    metadata: DictConfig
):
    match dataset_name:
        case "opportunity":
            processor = MislabelingProcessor()
            mislabeled_df = processor.mislabeling(
                df, 
                mislabeling_config.mislabeling_mode,
                mislabeling_config.target_labels,
                mislabeling_config.mislabeling_rate,
                mislabeling_config.num_label_duplication,
                mislabeling_config.num_label_mislabeling,
                metadata
            )
            return mislabeled_df, processor.indices_to_mislabel
        case "your-dataset-name":
            # Add preprocess code here.
            pass
        case default:
            raise ValueError(f"Dataset {dataset_name} not recognized.")