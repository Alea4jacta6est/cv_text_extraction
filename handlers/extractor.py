from itertools import chain

import pytesseract


def extract_text_from_image(image_path: str):
    """Extracts text from images and splits into 
    logical entities

    Args:
        image_path (str): a path to image

    Returns:
        extracted_text (str), entities (list of strings)
    """
    extracted_text = pytesseract.image_to_string(image_path, lang = "eng")
    entities = [ent for ent in extracted_text.split("\n\n") if ent and ent != "  "]
    entities = list(chain(*[ents.split("\n") for ents in entities]))
    return extracted_text, entities