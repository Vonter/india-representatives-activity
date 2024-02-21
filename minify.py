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

# Add columns related to debate and question categories in the CSV
def add_categories_csv(data):
    for representative in data:
        category = {}

        for debate in representative["Activity"]["Debates"]:
            key = "Debates ({})".format(debate["Debate Type"]).title()
            if key in category:
                category[key] +=  1
            else:
                category[key] =  1
        for question in representative["Activity"]["Questions"]:
            key = "Questions ({})".format(question["Ministry or Category"]).title()
            if key in category:
                category[key] +=  1
            else:
                category[key] =  1

        for categoryName, count in category.items():
            representative[categoryName] = count

        del representative["Activity"]

    return data

def build_csvs():
    directory_path = './json'
    json_files = glob.glob(os.path.join(directory_path, '**/*.json'), recursive=True)
    
    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        data = add_categories_csv(data)

        df = pd.DataFrame(data)
        pattern = r'Debate|Question'
        df.fillna(0, inplace=True)
        df.loc[:, df.columns.str.contains(pattern)] = df.loc[:, df.columns.str.contains(pattern)].astype(int)

        csv_file_path = json_file.replace('json', 'csv')
        df.to_csv(csv_file_path, index=False, sep=";", quoting=csv.QUOTE_ALL)

def merge_csvs_in_directory(directory):
    directory_path = './csv/{}'.format(directory)
    csv_files = glob.glob(os.path.join(directory_path, '**/*.csv'), recursive=True)

    dataframes = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file, sep=";", quoting=csv.QUOTE_ALL)
        dataframes.append(df)
    merged_dataframe = pd.concat(dataframes, ignore_index=True)

    pattern = r'Debate|Question'
    merged_dataframe.fillna(0, inplace=True)
    merged_dataframe.loc[:, merged_dataframe.columns.str.contains(pattern)] = merged_dataframe.loc[:, merged_dataframe.columns.str.contains(pattern)].astype(int)

    merged_dataframe.to_csv("{}.csv".format(directory_path), index=False, sep=";", quoting=csv.QUOTE_ALL)

def merge_csvs():
    merge_csvs_in_directory("Lok Sabha")

def minify():
    build_csvs()
    merge_csvs()

if __name__ == "__main__":
    minify()
