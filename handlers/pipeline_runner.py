import re
import os

import pandas as pd

from handlers.extractor import extract_text_from_image
from handlers.parser import extract_dob, extract_license_id, from_ft_to_cm


columns = ["First Name", 
            "Last Name", 
            "DOB", 
            "Address",
            "Sex",
            "Eye Color",
            "Height (cm)",
            "Weight(lbs)",	
            "License #"]

def run_pipeline(image_path, save_out=False):
    """Runs the pipeline to extract all predefined types of data

    Args:
        image_path (str): absolute path to an image
        save_out (bool): save as csv or not 
    Returns:
        df (DataFrame object): df with extracted data
        extracted_text (str): raw extracted text
    """
    sample = {column: ["Not identified"] for column in columns}
    extracted_text, entities = extract_text_from_image(image_path)
    dob = extract_dob(extracted_text)
    id_ = extract_license_id(extracted_text)
    height = from_ft_to_cm(extracted_text)
    weight = re.findall("[a-zA-Z, ]{1}1[0-9]{2} ", extracted_text)[0].strip()
    if weight[0].isalpha():
        weight = weight[1:]
    
    # NOT SCALABLE => to be replaced by a custom NER model
    for i, entity in enumerate(entities):
        check_for_num = entity.startswith("1") or entity.startswith("+")
        if check_for_num and len(entity.split()) < 4 and "°" not in entity:
            name = entity.replace("1", "").replace("+", "").strip()
            sample["First Name"] = [name]
        elif entity.startswith("2"):
            last_name = entity.replace("2", "").strip()
            sample["Last Name"] = [last_name]
        elif entity.startswith("8"):
            address = entity.replace("8", "")
            if not entities[i+1][0].isdigit():
                address += entities[i+1].replace("{", "").strip()
            sample["Address"] = [address]
        elif "sex" in entity.lower():
            sex = entity.split()[0].replace("Sex", "")
            sex = re.sub("\d+", "", sex)
            sample["Sex"] = [sex]
        elif "eyes" in entity.lower():
            eyes = entity.split()[-1]
            sample["Eye Color"] = [eyes]
    
    sample["DOB"] = [dob]
    sample["Height (cm)"] = [height]
    sample["Weight(lbs)"] = [weight]
    sample["License #"] = [id_]
    df = pd.DataFrame.from_dict(sample)
    if save_out:
        os.mkdirs("data/outputs/", exists_ok=True)
        df.to_csv("data/outputs/out.csv", index=False)
    return df, extracted_text