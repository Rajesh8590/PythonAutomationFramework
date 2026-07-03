from pathlib import Path
import json

class JsonReader:

    @staticmethod
    def read(file_name):
        print("json file:",Path(__file__))
        data_path = Path(__file__).parent.parent / "data" / file_name
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)["data"]