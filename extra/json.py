import json
import logging
import os.path

logging.basicConfig(level=logging.INFO)

def load_user_data(file_name):
    absolute_path = os.path.abspath(file_name)
    logging.info(f"Attempting to load file from: {absolute_path}")


    if not os.path.isfile(file_name):
        logging.error(f"Error: {file_name} does not exist.")
        return {}


    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            logging.info(f"Data loaded successfully from {file_name}.")
            return data

    except FileNotFoundError:
        logging.info(f"Error: {file_name} not found.")
        return {}

    # except json.JSONDecodeError:
    #     logging.error(f"Error: Failed to decode Json from {file_name}.")
    #     return {}


file_name = "data.json"
load_user_data(file_name)

