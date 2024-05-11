import pandas as pd

# 15 - 29
data_young_thousands = pd.read_csv("datasets/byAge/sport_young_thousands.csv")
data_young_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_young_thousands = data_young_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_young_thousands.reset_index(inplace=True)
pivot_data_young_thousands.columns.name = None
#print(pivot_data_young_thousands)
pivot_data_young_thousands.to_csv("datasets/byAge-processed/sport_young_thousands.csv", index=False)

data_young_percentage = pd.read_csv("datasets/byAge/sport_young_percentage.csv")
data_young_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_young_percentage = data_young_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_young_percentage.reset_index(inplace=True)
pivot_data_young_percentage.columns.name = None
#print(pivot_data_young_percentage)
pivot_data_young_percentage.to_csv("datasets/byAge-processed/sport_young_percentage.csv", index=False)

# 30 - 64
data_middle_thousands = pd.read_csv("datasets/byAge/sport_middle_thousands.csv")
data_middle_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_middle_thousands = data_middle_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_middle_thousands.reset_index(inplace=True)
pivot_data_middle_thousands.columns.name = None
#print(pivot_data_middle_thousands)
pivot_data_middle_thousands.to_csv("datasets/byAge-processed/sport_middle_thousands.csv", index=False)

data_middle_percentage = pd.read_csv("datasets/byAge/sport_middle_percentage.csv")
data_middle_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_middle_percentage = data_middle_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_middle_percentage.reset_index(inplace=True)
pivot_data_middle_percentage.columns.name = None
#print(pivot_data_middle_percentage)
pivot_data_middle_percentage.to_csv("datasets/byAge-processed/sport_middle_percentage.csv", index=False)

# 65 +
data_old_thousands = pd.read_csv("datasets/byAge/sport_old_thousands.csv")
data_old_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_old_thousands = data_old_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_old_thousands.reset_index(inplace=True)
pivot_data_old_thousands.columns.name = None
#print(pivot_data_old_thousands)
pivot_data_old_thousands.to_csv("datasets/byAge-processed/sport_old_thousands.csv", index=False)

data_old_percentage = pd.read_csv("datasets/byAge/sport_old_percentage.csv")
data_old_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "age", "unit"], inplace=True)
pivot_data_old_percentage = data_old_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_old_percentage.reset_index(inplace=True)
pivot_data_old_percentage.columns.name = None
#print(pivot_data_old_percentage)
pivot_data_old_percentage.to_csv("datasets/byAge-processed/sport_old_percentage.csv", index=False)