import pandas as pd

# MALE
data_male_thousands = pd.read_csv("datasets/bySex/sport_male_thousands.csv")
data_male_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_male_thousands = data_male_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_male_thousands.reset_index(inplace=True)
pivot_data_male_thousands.columns.name = None
#print(pivot_data_male_thousands)
pivot_data_male_thousands.to_csv("datasets/bySex-processed/sport_male_thousands.csv", index=False)

data_male_percentage = pd.read_csv("datasets/bySex/sport_male_percentage.csv")
data_male_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_male_percentage = data_male_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_male_percentage.reset_index(inplace=True)
pivot_data_male_percentage.columns.name = None
#print(pivot_data_male_percentage)
pivot_data_male_percentage.to_csv("datasets/bySex-processed/sport_male_percentage.csv", index=False)

# FEMALE
data_female_thousands = pd.read_csv("datasets/bySex/sport_female_thousands.csv")
data_female_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_female_thousands = data_female_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_female_thousands.reset_index(inplace=True)
pivot_data_female_thousands.columns.name = None
#print(pivot_data_female_thousands)
pivot_data_female_thousands.to_csv("datasets/bySex-processed/sport_female_thousands.csv", index=False)

data_female_percentage = pd.read_csv("datasets/bySex/sport_female_percentage.csv")
data_female_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_female_percentage = data_female_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_female_percentage.reset_index(inplace=True)
pivot_data_female_percentage.columns.name = None
#print(pivot_data_female_percentage)
pivot_data_female_percentage.to_csv("datasets/bySex-processed/sport_female_percentage.csv", index=False)

# TOTAL
data_total_thousands = pd.read_csv("datasets/total/sport_total_thousands.csv")
data_total_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_total_thousands = data_total_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_total_thousands.reset_index(inplace=True)
pivot_data_total_thousands.columns.name = None
#print(pivot_data_total_thousands)
pivot_data_total_thousands.to_csv("datasets/total-processed/sport_total_thousands.csv", index=False)

data_total_percentage = pd.read_csv("datasets/total/sport_total_percentage.csv")
data_total_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "sex", "unit"], inplace=True)
pivot_data_total_percentage = data_total_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_total_percentage.reset_index(inplace=True)
pivot_data_total_percentage.columns.name = None
#print(pivot_data_total_percentage)
pivot_data_total_percentage.to_csv("datasets/total-processed/sport_total_percentage.csv", index=False)
