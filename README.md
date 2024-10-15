# LLM reasoning capabilities for multi-device context inference
- We demonstrate the advantages of multi-device context inference with LLMs.
<!-- Figure or table to show the performance -->

## Requirements
| Language・Library  | Version |
| --------------------- | ---------- |
| Python                | 3.10.10     |
| openai               | 1.51.0    |
| numpy                | 2.1.2      |
| scikit-learn | 1.5.2     |
| torch                 | 2.4.1        |
- see requirements.txt

## Env
- OPENAI_API_KEY: Your openai api key

## Dataset link
- [OPPORTUNITY Activity Recognition](https://archive.ics.uci.edu/dataset/226/opportunity+activity+recognition)

<!-- TODO: What will we do in this repo? -->
## Mislabeling mode: wild & fused

## Instruction
- Global hyperparameters are configured in .yaml files in the config directory.

## Parameters
| Parameter  | Value | Description |
| ---------- | ----- | ----------- |
| **experiment_type** | (activity_comprehension_ex, duration_comprehension_ex) | The type of experiment being run. | 
| **gpt_model** | (gpt-3.5-turbo, gpt-4o-mini, gpt-4o-2024-08-06) | The GPT model used for LLM output. |
| **trial** | 1 | The current trial of the experiment. |
| **mislabeling** | | Mislabeling-related settings |
| - target_labels | ["locomotion", "gesture"] | Labels that will be mislabeled. |
| - mislabelling_mode | wild or fused | Mode for applying mislabeling. |
| - mislabeling_rate | 0.1 | The probability at which mislabeling will occur. For instance 10% of the non-Null data on the column will be mislabeled. |
| - num_label_duplication | 1 | Number of duplicate column instances. Assuming multiple sensors.|
| - num_label_mislabeling| 1 | Number of column assigned mislabels. |
| **dataset** | | Dataset-related settings |
| - dataset_name | opportunity | Name of the dataset used in the experiment. |
| - metadata_path | datasets/metadata/opportunity.yaml | Path to the metadataa file for the selected dataset. This file typically includes information on data structure, classes. |

## Examples
- `python main.py --config-name default experiment_type=duration_comprehension_ex gpt_model=gpt-4o-2024-08-06 mislabeling.mislabeling_rate=0.05`

## Acknowledgements
- Codes for cnn mislabeling trend are based on [Exploring-the-OPPORTUNITY-Dataset-for-Activity-Recognition
](https://github.com/IliesChibane/Exploring-the-OPPORTUNITY-Dataset-for-Activity-Recognition) by IliesChibane,licensed under the MIT License.