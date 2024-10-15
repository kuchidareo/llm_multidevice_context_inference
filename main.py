import hydra
from omegaconf import DictConfig, OmegaConf

from dataset import load_datasets
from mislabeling import apply_mislabeling
from llm_experiment import activity_comprehension_ex, duration_comprehension_ex
from utils import generate_filename, export_csv, export_llm_conversation

@hydra.main(config_path="conf", config_name="default", version_base=None)
def main(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))
    hydra_output_dir = hydra.core.hydra_config.HydraConfig.get().runtime.output_dir
    metadata = OmegaConf.load(cfg.dataset.metadata_path)

    filtered_df = load_datasets(cfg.dataset, metadata)
    misclassified_df, misclassified_row_indices = apply_mislabeling(filtered_df, cfg.mislabeling, cfg.dataset.dataset_name, metadata)

    filename = generate_filename(cfg.dataset, cfg.mislabeling, cfg.experiment_type, cfg.gpt_model, cfg.trial)
    export_csv(misclassified_df, hydra_output_dir, filename)

    csv_text = misclassified_df.to_csv(index=False, header=False)

    if cfg.experiment_type == "activity_comprehension_ex":
        conversation = activity_comprehension_ex(csv_text, cfg.gpt_model, misclassified_df, misclassified_row_indices)
    elif cfg.experiment_type == "duration_comprehension_ex":
        conversation = duration_comprehension_ex(csv_text, cfg.gpt_model)

    export_llm_conversation(conversation, hydra_output_dir, filename)

if __name__ == "__main__":
    main()

