import pandas as pd

# Primary
data_primary_thousands = pd.read_csv("datasets/byEducation/sport_primary_thousands.csv")
data_primary_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_primary_thousands = data_primary_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_primary_thousands.reset_index(inplace=True)
pivot_data_primary_thousands.columns.name = None
#print(pivot_data_primary_thousands)
pivot_data_primary_thousands.to_csv("datasets/byEducation-processed/sport_primary_thousands.csv", index=False)

data_primary_percentage = pd.read_csv("datasets/byEducation/sport_primary_percentage.csv")
data_primary_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_primary_percentage = data_primary_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_primary_percentage.reset_index(inplace=True)
pivot_data_primary_percentage.columns.name = None
#print(pivot_data_primary_percentage)
pivot_data_primary_percentage.to_csv("datasets/byEducation-processed/sport_primary_percentage.csv", index=False)

# Secondary
data_secondary_thousands = pd.read_csv("datasets/byEducation/sport_secondary_thousands.csv")
data_secondary_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_secondary_thousands = data_secondary_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_secondary_thousands.reset_index(inplace=True)
pivot_data_secondary_thousands.columns.name = None
#print(pivot_data_secondary_thousands)
pivot_data_secondary_thousands.to_csv("datasets/byEducation-processed/sport_secondary_thousands.csv", index=False)

data_secondary_percentage = pd.read_csv("datasets/byEducation/sport_secondary_percentage.csv")
data_secondary_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_secondary_percentage = data_secondary_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_secondary_percentage.reset_index(inplace=True)
pivot_data_secondary_percentage.columns.name = None
#print(pivot_data_secondary_percentage)
pivot_data_secondary_percentage.to_csv("datasets/byEducation-processed/sport_secondary_percentage.csv", index=False)

# Tertiary
data_tertiary_thousands = pd.read_csv("datasets/byEducation/sport_tertiary_thousands.csv")
data_tertiary_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_tertiary_thousands = data_tertiary_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_tertiary_thousands.reset_index(inplace=True)
pivot_data_tertiary_thousands.columns.name = None
#print(pivot_data_tertiary_thousands)
pivot_data_tertiary_thousands.to_csv("datasets/byEducation-processed/sport_tertiary_thousands.csv", index=False)

data_tertiary_percentage = pd.read_csv("datasets/byEducation/sport_tertiary_percentage.csv")
data_tertiary_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_tertiary_percentage = data_tertiary_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_tertiary_percentage.reset_index(inplace=True)
pivot_data_tertiary_percentage.columns.name = None
#print(pivot_data_tertiary_percentage)
pivot_data_tertiary_percentage.to_csv("datasets/byEducation-processed/sport_tertiary_percentage.csv", index=False)

# No response
data_noResponse_thousands = pd.read_csv("datasets/byEducation/sport_noResponse_thousands.csv")
data_noResponse_thousands.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_noResponse_thousands = data_noResponse_thousands.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_noResponse_thousands.reset_index(inplace=True)
pivot_data_noResponse_thousands.columns.name = None
#print(pivot_data_noResponse_thousands)
pivot_data_noResponse_thousands.to_csv("datasets/byEducation-processed/sport_noResponse_thousands.csv", index=False)

data_noResponse_percentage = pd.read_csv("datasets/byEducation/sport_noResponse_percentage.csv")
data_noResponse_percentage.drop(columns=["OBS_FLAG", "LAST UPDATE", "DATAFLOW", "freq", "isced11", "unit"], inplace=True)
pivot_data_noResponse_percentage = data_noResponse_percentage.pivot_table(index="geo", columns = "TIME_PERIOD", values="OBS_VALUE")
pivot_data_noResponse_percentage.reset_index(inplace=True)
pivot_data_noResponse_percentage.columns.name = None
#print(pivot_data_noResponse_percentage)
pivot_data_noResponse_percentage.to_csv("datasets/byEducation-processed/sport_noResponse_percentage.csv", index=False)