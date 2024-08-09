import ray
from ray.train import ScalingConfig
from ray.train.xgboost import XGBoostTrainer

checked_data = "I:/Wildfire_Datasets_v2/combined_checked.csv"
ray.init(include_dashboard=False)

# Import data
dataset = ray.data.read_csv(checked_data)

# Configure workers
scaling_config = ScalingConfig(
    use_gpu=True
)

train, valid = dataset.train_test_split(test_size=0.25)

parameters = {
    "eval_metric": "rmse",
}

# Train Classifier
trainer = XGBoostTrainer(
    datasets={"train": train, "valid": valid},
    label_column="dNBR",
    params=parameters,
    scaling_config=scaling_config,
)

trained = trainer.fit()
acc = trained.metrics.get("valid-rmse")
print(acc)
# Get Variable Importance
# iterimportance = trained.metrics.get()
print(trained.metrics)
print(trained)
