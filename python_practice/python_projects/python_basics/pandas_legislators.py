import pandas as pd 

dtypes = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}

df = pd.read_csv(
    "/workspaces/data_engineering_projects/python_practice/python_projects/python_basics/groupby_data/materials-pandas-groupby/legislators-historical.csv"
    , dtype=dtypes,
    usecols=list(dtypes.keys()) + ["birthday","last_name"],
    parse_dates=["birthday"]
)


