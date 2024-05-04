import re

def sanitize_input(input_string):
    # Remove everything but capital English letters
    sanitized_string = re.sub(r'[^A-Za-z0-9 !?.]', '', input_string)
    return sanitized_string