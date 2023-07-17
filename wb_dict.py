import re

all_wb = open("names_wb.txt").read()

# initialize lists to zip later into a dictionary
names=[]
wb=[]

# parse out  the restriction enzyme name and put it into RE list
for name in re.finditer(r"(\w)(\s)(\w)(\s)(\d{2}-\d{4})", all_wb):
    names.append(name.group(1+2))
# parse out the restriction enzyme sequence and put into cuts list    
for id in re.finditer(r"(\w)(\s)(\w)(\s)(\d{2}-\d{4})", all_wb):
    wb.append(wb.group(5))

# create a dictionary by zipping the lists    
wb_dict = dict(zip(names, wb))

print(wb_dict)
