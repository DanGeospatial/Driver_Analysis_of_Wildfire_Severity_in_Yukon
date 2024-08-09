from xgboost import XGBRegressor as xgbr

checked_data = "I:/Wildfire_Datasets_v2/combined_reduced.csv"
parameters = {
        "eta": config["eta"],
        "gamma": config["gamma"],
        "max_depth": config["max_depth"],
        "min_child_weight": config["min_child_weight"],
        "subsample": config["subsample"],
        "colsample_bytree": config["colsample_bytree"],
        "lambda": config["lambda"],
        "alpha": config["alpha"],
        "num_boost_round"
}

