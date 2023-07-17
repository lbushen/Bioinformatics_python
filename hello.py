import re

file = open("wb_ex.txt").read()

wb = re.findall(r"(\d{2}-\d{4})", file)
string=str(wb)

wb_ids = open("wb_ids.txt", "w")



wb_ids.write(string)



all_wb = open("names_wb.txt").read().strip("\n")

# initialize lists to zip later into a dictionary
names=[]
wb=[]

# parse out  the restriction enzyme name and put it into RE list
for name in re.finditer(r"(\w*)(\s)(\d{2}-\d{4})", all_wb):
    names.append(name.group(1))
# parse out the restriction enzyme sequence and put into cuts list    
for id in re.finditer(r"(\w*)(\s)(\d{2}-\d{4})", all_wb):
    wb.append(wb.group(3))

# create a dictionary by zipping the lists    
wb_dict = dict(zip(names, wb))

wb_ids.close()

wb_file = open("wb_ids.txt").read().strip

print(wb_file)




