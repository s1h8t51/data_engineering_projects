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

#from pandas_legislators import df
#df.tail()
#df.dtypes
#>>> n_state = df.groupby(["state","gender"],as_index=False)["last_name"].count()

#instead of count we can also use size where size calculates nan values unlike count
#orderby done by default by group by parameter sort which is true unless you tell

#df.groupby(["state","gender"],as_index=False,sort=False)["last_name"].count()

#split-apply-combine

## air quality_dataset


import pandas as pd

# 1. Load the data normally with usecols
df1 = pd.read_csv(
    "/workspaces/data_engineering_projects/python_practice/python_projects/python_basics/groupby_data/materials-pandas-groupby/airqual.csv",
    sep=",", 
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"],
    na_values=[-200]
)

# format matches "3/10/04 18:00:00"
df1["tstamp"] = pd.to_datetime(
    df1["Date"] + " " + df1["Time"], 
    format="%m/%d/%y %H:%M:%S"
)

# 3. Rename and Clean up
df1 = df1.rename(
    columns={
        "CO(GT)": "co",
        "T": "temp_c",
        "RH": "rel_hum",
        "AH": "abs_hum",
    }
)


df1.set_index("tstamp", inplace=True)
df1.drop(columns=["Date", "Time"], inplace=True)


# resamppling
#df.groupby([df.index.year, df.index.quarter])["co"].agg(["max", "min"]).rename_axis(["year", "quarter"])
#timebased resampling 
#df.resample("Q")["co"].agg(["max", "min"])


def parse_millisecond_timestamp(ts):
    """Convert ms since Unix epoch to UTC datetime instance."""
    return pd.to_datetime(ts, unit="ms")

df2 = pd.read_csv(
    "/workspaces/data_engineering_projects/python_practice/python_projects/python_basics/groupby_data/materials-pandas-groupby/news.csv",
    sep="\t",
    header=None,
    index_col=0,
    names=["title", "url", "outlet", "category", "cluster", "host", "tstamp"],
    parse_dates=["tstamp"],
    date_format="%m/%d/%y %H:%M:%S",
    dtype={
        "outlet": "category",
        "category": "category",
        "cluster": "category",
        "host": "category",
    },
)

## Unix Epoch time in milliseconds. -- so we are converting here 
## ranked leaderboard of the news outlets that mention "Fed" the most.
# index -- name of the news outlet 
# The Value: The total number py of articles from that outlet where the title contains the word "Fed"
#

#df2.groupby("outlet", sort=False)["title"].apply(lambda ser: ser.str.contains("Fed").sum()).nlargest(10)

#faster version 

#
# 1. Create a temporary boolean column (Vectorized - very fast!)
#df2['has_fed'] = df2['title'].str.contains("Fed")

# 2. Group by that boolean column
# (True counts as 1, False as 0)
#results = df2.groupby("outlet")['has_fed'].sum().nlargest(10)

#title, ser = next(iter(df.groupby("outlet", sort=False)["title"]))title
# ser.head()

## best groupby methods

#Aggregation (Reduction)
# Returns a smaller DataFrame (one row per outlet)
df_agg = df2.groupby("outlet")["title"].agg(["count", "max"])
print(df_agg.head())

#Filter
# Returns a subset of the original DataFrame (rows from small outlets are gone)
df_filtered = df2.groupby("outlet").filter(lambda x: len(x) > 100)
print(f"Original rows: {len(df2)} | Filtered rows: {len(df_filtered)}")

#Transformation
# The result has the same number of rows as df2
df2["outlet_total_count"] = df2.groupby("outlet")["title"].transform("count")
print(df2[["outlet", "title", "outlet_total_count"]].head())

#Meta Methods
groups = df2.groupby("outlet")

# How many outlets are there?
print(f"Number of groups: {groups.ngroups}")

# What are the row indices for 'Reuters'?
print(groups.groups["Reuters"])

#Plotting

import matplotlib.pyplot as plt

# Plotting the count of articles for the top 5 outlets
df2.groupby("outlet")["title"].count().nlargest(5).plot(kind="bar")
plt.title("Top 5 Outlets by Article Count")
plt.show()