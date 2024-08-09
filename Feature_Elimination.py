"""
Remove features to improve accuracy and efficiency by dropping features that are unimportant, add error, etc.
"""
import ray
import pandas as pd
from ray.train import ScalingConfig
from ray.train.xgboost import XGBoostTrainer

checked_data = "I:/Wildfire_Datasets_v2/combined_checked.csv"
variables = ['1_clm', '23_clm', '24_clm', '25_clm', '26_clm', '27_clm', '28_clm', '29_clm', '2_clm', '30_clm', '31_clm',
             '32_clm', '33_clm', '34_clm', '35_clm', '36_clm', '37_clm', '38_clm', '39_clm', '3_clm', '40_clm',
             '42_clm', '43_clm', '44_clm', '45_clm', '46_clm', '47_clm', '48_clm', '4_clm', '5_clm', '6_clm', '7_clm',
             'Aspect', 'dNBR', 'Elevation', 'LC', 'mNBR', 'pre', 'Slope', 'tpi', 'twi']
ray.init(include_dashboard=False)

# Import data
dataset = ray.data.read_csv(checked_data)

# Configure workers
scaling_config = ScalingConfig(
    num_workers=16,
    use_gpu=True
)

# Set accuracy and importance Storage
testAcc = []
varImp = []


# Run Recursive Feature Elimination
def rfe_control(inputs):
    global testAcc
    global varImp

    train, valid = inputs.train_test_split(test_size=0.25)

    # Train Classifier
    trainer = XGBoostTrainer(
        datasets={"train": train, "valid": valid},
        label_column="dNBR",
        scaling_config=scaling_config,
    )

    trained = trainer.fit()
    acc = trained.metrics.get("valid-rmse")

    # Get Variable Importance
    iterimportance = trained.metrics.get()
    print(trained.metrics)
    imp = iterimportance.keys()
    values = iterimportance.values()

    # Get the least important variable
    minimumIndex = values.indexOf(values.reduce(ee.Reducer.min()))
    minimumItem = imp.get(minimumIndex)

    inputs = inputs.remove(minimumItem)

    testAcc = testAcc.add(acc)
    varImp = varImp.add(inputs)

    return inputs


def rfe(subset):
    # Get Test Accuracy
    while subset.length().getInfo() > 3:
        subset = rfe_control(subset)

    global testAcc
    global varImp
    # Find the Bands with the Highest Accuracy
    maxValue = testAcc.indexOf(testAcc.reduce(ee.Reducer.max()))
    maxIndex = varImp.get(maxValue)

    return maxIndex


# Store RFE Output
bestBands = rfe(variables)
print(bestBands.getInfo())

# Output dataset of optimal variables
