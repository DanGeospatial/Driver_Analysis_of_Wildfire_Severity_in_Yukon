"""
Train wildfire regression model using XGBoost
Optimize with Ray Tune and HyperOPT
"""

import ray
from ray import tune
from ray.tune.search.hyperopt import HyperOptSearch
from hyperopt import hp
from ray.train import ScalingConfig
from ray.train.xgboost import XGBoostTrainer
import xgboost

# Import Data
dNBR3Y = "D:/Research/Masters/8_RStudio/Input Data/ERA5/total/dNBR_total_3y.csv"

ray.init(include_dashboard=False)

# Preprocess Data
dataset = ray.data.read_csv(dNBR3Y)
train, valid = dataset.train_test_split(test_size=0.25)

scaling_config = ScalingConfig(
    num_workers=8,
    use_gpu=True
)


def objective(config):
    parameters = {
        "eval_metric": "rmse",
        "eta": config["eta"],
        "gamma": config["gamma"],
        "max_depth": config["max_depth"],
        "min_child_weight": config["min_child_weight"],
        "subsample": config["subsample"],
        "colsample_bytree": config["colsample_bytree"],
        "lambda": config["lambda"],
        "alpha": config["alpha"]
    }

    trainer = XGBoostTrainer(
        datasets={"train": train, "valid": valid},
        label_column="dNBR",
        params=parameters,
        scaling_config=scaling_config,
        # num_boost_round and num_parallel_tree
    )

    trained = trainer.fit()
    test_rmse = trained.metrics.get("valid-rmse")

    return {"rmse": test_rmse}


method = HyperOptSearch()
samples = 1000

#
search_config = {
    "eta": tune.loguniform(0.01, 1),
    "gamma": tune.randint(0, 10),
    "max_depth": tune.randint(3, 10),
    "min_child_weight": tune.randint(1, 5),
    "subsample": tune.loguniform(0.5, 1),
    "colsample_bytree": tune.loguniform(0.5, 1),
    "lambda": tune.randint(1, 5),
    "alpha": tune.randint(0, 5)
}


def trial_str_creator(trial):
    return trial.trial_id


tuner = tune.Tuner(
    objective,
    tune_config=tune.TuneConfig(
        metric="rmse",
        mode="min",
        search_alg=method,
        num_samples=samples,
        trial_dirname_creator=trial_str_creator
    ),
    param_space=search_config,
)

results = tuner.fit()
print("Optimal hyperparameters: ", results.get_best_result().config)
print(results.get_best_result())
