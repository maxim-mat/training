import json

class JsonDataParser:

    @staticmethod
    def parse_data_from_file(filename):
        with open(filename , 'r') as file:
            data = json.load(file)
        return data
