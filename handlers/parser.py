import re


def extract_dob(text):
    birthdate_regex = "\d{2}.\w{2}.\d{4}"
    result = re.findall(birthdate_regex, text)
    return result[0]

def extract_license_id(text):
    regex = "[a-zA-Z]{7}[0-9]{3}[a-zA-Z]{2}"
    result = re.findall(regex, text)
    return result[0]

def from_ft_to_cm(text):
    result_in_cm = ""
    num_with_dash = re.findall(" [1-9]{1}-[0-9]{1,2}", text)
    if num_with_dash:
        num_with_dash = num_with_dash[0].strip()
        feet, inch = [int(num) for num in num_with_dash.split("-")]
        result_in_cm = round(feet * 30.48 + inch * 2.54)
        if result_in_cm > 220:
            result_in_cm = round(5 * 30.48 + inch * 2.54)
    return result_in_cm