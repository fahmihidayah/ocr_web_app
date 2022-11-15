import easyocr
from pathlib import Path

def extract_data(image_path):
    BASE_DIR = Path(__file__).resolve().parent.parent
    image = str(BASE_DIR.absolute()) + "/media/" + image_path
    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
    result = reader.readtext(image)
    return result