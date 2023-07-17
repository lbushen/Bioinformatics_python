import re

#QA_text = input("Enter text file for parsing workbook ids: ")

QA = open("wb_ex.txt").read().strip()

QA_wb =[]

for wb in re.findall(r"(\d{2,3}-\d{4})", QA):
    QA_wb.append(wb)

wb_part = []
names = []

#wb_names = input("Enter text file for parsing workbook ids and reviewers: ")

file = open("names_wb.txt").read().strip()

for i in re.findall(r"(\d{2,3}-\d{4})", file):
    wb_part.append(i)

for id in re.finditer(r"(\D*\s{1}\D*)", file):
    names.append(id.group(1).strip())
  

wb_dict = dict(zip(names,wb_part))

print(wb_dict)

'''
x = 0      
for key, value in wb_dict.items():
    for i in QA_wb:
        if i in value:
            x = 1
            if x == 1:
                print(key, value)
        
'''

