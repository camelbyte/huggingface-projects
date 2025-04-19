import requests
import pandas as pd 
import matplotlib.pyplot as plt


# TODO: 
""" 
    1. Fetch Trump favorability poll data from Github and use pandas to read it. 
    2. Create a pivot table with date as index, response as columns, and pct_estimate as values.
    3. Sort it 
    4. Plot the data using matplotlib with date on x-axis and favorability % on y-axis. 

    5. Add a title and labels to the axes. 
    6. Show the plot.
    7. Expand the project features and functionality to include more columns with different data types 
    to generate insight and analysis. --- Add highest read news articles on each day and compare it to 
    the favorability rating to determine what was in the news in the days prior to the poll. 
    8. Add a feature to compare the favorability rating with other candidates.

"""

def get_data():
    """
    Fetch Trump favorability polling data directly from the raw GitHub CSV.
    Returns a pandas DataFrame.
    """
    raw_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/polls/old_model/donald_trump_favorability_old_model.csv"
    res = requests.get(raw_url)
    if res.status_code != 200:
        raise Exception("Failed to fetch data from Github")
    df = pd.read_csv(raw_url)
    print(df.head())
    return df


# ✅ Fix: assign df
df = get_data()

# Now df is defined and accessible
pivot = df.pivot(index="date", columns="response", values="pct_estimate").sort_index()

pivot.plot(figsize=(12, 6), title="Donald Trump Favorability Over Time")
plt.ylabel("Favorability %")
plt.grid(True)
plt.show()

