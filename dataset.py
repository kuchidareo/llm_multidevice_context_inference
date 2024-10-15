import os

from omegaconf import DictConfig
import pandas as pd

class FilterData():
    def __init__(self, config):
        self.config = config

    @staticmethod
    def filter_out_zero_values(df, column_index_to_save):
        valid_row_indices = pd.Series([False] * len(df))
        for col_index in column_index_to_save:
            valid_row_indices |= (df.iloc[:, col_index] != 0)
        df = df[valid_row_indices]
        return df
    
    @staticmethod
    def replace_labels_with_legend(df, column_index_to_legend):
        # label -> corresponding legend
        for col_index, value_to_legend in column_index_to_legend.items():
            df.iloc[:, col_index] = df.iloc[:, col_index].replace(value_to_legend)

        return df
        
    @staticmethod
    def select_columns(df, column_index_to_save):
        # Selecting only the columns of interest for locomotion and ML_Both_Arms
        df = df.iloc[:, column_index_to_save]
        return df
    
    @staticmethod
    def extract_moments_of_change(df):
        # Extract moments where values are changing
        df = df[df.ne(df.shift()).any(axis=1)]
        return df

    @staticmethod
    def add_relative_time_column(df, sampling_freq):
        df['relative_time(s)'] = (df.index / sampling_freq).astype(int)
        return df

    @staticmethod
    def rename_columns(df):
        df.rename(columns={243: 'locomotion_label_0', 249: 'gesture_label_0'}, inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df

def filter_data(
    df: pd.DataFrame,
    config: DictConfig,
    metadata: DictConfig
):
    """  
    locomotion_label_0 gesture_label_0  relative_time(s)
0               Stand               0                92
1                Walk               0               261
2                 Lie               0               272
3               Stand               0               302
4                Walk               0               315
    """

    match config.dataset_name:
        case "opportunity":
            column_index_to_save = [
                metadata.locomotion_column_index,
                metadata.ML_Both_Arms_column_index
            ]
            column_index_to_legend = {
                metadata.locomotion_column_index: metadata.locomotion_label_legend,
                metadata.ML_Both_Arms_column_index: metadata.ML_Both_Arms_label_legend
            }
            sensor_frequency = metadata.sampling_frequency_hz
            df.iloc[:, column_index_to_save] = df.iloc[:, column_index_to_save].astype(str)
  
            df = FilterData.filter_out_zero_values(df, column_index_to_save)
            df = FilterData.replace_labels_with_legend(df, column_index_to_legend)

            df = FilterData.select_columns(df, column_index_to_save)
            df = FilterData.extract_moments_of_change(df)
            df = FilterData.add_relative_time_column(df, sensor_frequency)
            df = FilterData.rename_columns(df)

            return df
    
        case "your-dataset-name":
            # Add preprocess code here.
            pass
        case default:
            raise ValueError(f"Dataset {config.dataset_name} not recognized.")
        

def load_datasets(
    config: DictConfig,
    metadata: DictConfig,
):
    df = pd.read_csv(
        os.path.join(metadata.dataset_directory, metadata.adl_name),
        sep=' ',
        header=None
    )
            
    filtered_dataset = filter_data(df, config, metadata)

    return filtered_dataset
