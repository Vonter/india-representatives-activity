import csv
import glob
import json
import logging
import os
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Aggregate legislative activity by activity type
def aggregate_json(data, activityType):
    aggregated = []

    try:
        for representative in data:
            for activity in representative["Activity"][activityType]:
                activity["Representative"] = representative["Name"]
                aggregated.append(activity)
    except:
        logging.error("Failed to aggregate {} activities".format(activityType))

    return aggregated

# Build CSVs with legislative activity of every representative aggregated by activity type
def build_csvs():
    directory_path = './json'
    json_files = glob.glob(os.path.join(directory_path, '**/*.json'), recursive=True)

    try:
        for json_file in json_files:
            with open(json_file, 'r') as file:
                data = json.load(file)
                for activityType in ["Debates", "Questions", "Private Member Bills"]:
                    dataFrame = pd.DataFrame(aggregate_json(data, activityType))

                    # Convert first column of dataFrame to datetime format
                    try:
                        dataFrame.iloc[:,  0] = pd.to_datetime(dataFrame.iloc[:,  0], format="%d.%m.%Y")
                    except:
                        dataFrame.iloc[:,  0] = pd.to_datetime(dataFrame.iloc[:,  0], format="%Y-%m-%d")

                    for column in dataFrame.select_dtypes(include=['object']):
                        dataFrame[column] = dataFrame[column].apply(
                            lambda x: x.replace('\n', ' ') if isinstance(x, str) else x
                        )
                    dataFrame = dataFrame.sort_values(by=dataFrame.columns[0], ascending=False)

                    csv_file_directory = os.path.join("activity", "{}".format(activityType), "{}".format(json_file.split("/")[2]))
                    os.makedirs(csv_file_directory, exist_ok=True)

                    csv_file_path = os.path.join(csv_file_directory, json_file.split("/")[-1].replace("json", "csv"))
                    dataFrame.to_csv(csv_file_path, index=False, sep=";", quoting=csv.QUOTE_ALL)
    except:
        logging.error("Failed to process {}".format(json_file))
        raise

def aggregate():
    build_csvs()

if __name__ == "__main__":
    aggregate()
