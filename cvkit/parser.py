
import json
from pathlib import Path


CV_FILE = Path(__file__).parent.parent / "data" / "sy-cv-master.json"


def load():
    with CV_FILE.open(encoding="utf-8") as file:
        return json.load(file)
