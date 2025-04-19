from datasets import load_dataset 

dataset = load_dataset("imdb", split="test[:100]")
col = dataset.column_names

print(col)

df = dataset.to_pandas()

print(df.head())

