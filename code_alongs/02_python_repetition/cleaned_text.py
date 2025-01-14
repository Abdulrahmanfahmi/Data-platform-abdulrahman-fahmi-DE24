import re
from pathlib import path


print("this is path of this script")

data_path = (path(__file__).parent /"data")

with open(data_path /"ml_text_raw.txt", "r")as file: raw_text = file.read()
print(file.read())

text_fixed_spacing = re.sub(r"\s+", " ", raw_text)
text_fixed_spacing 

text_fixed_spacing.split(". ")

[text.strip().capitalize() for text in 

text_fixed_spacing.split(". ")] 

print(text_fixed_spacing)