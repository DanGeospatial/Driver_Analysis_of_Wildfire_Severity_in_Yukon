"""
Remove features to improve accuracy and efficiency by dropping features that are unimportant, add error, etc.
"""
from ray.train import ScalingConfig
from ray.train.xgboost import XGBoostTrainer

clean_path = "I:/Wildfire_Datasets_v2/combined_clean.csv"

# Input into feature elimination

# Output dataset of optimal variables
