"""
Created on Tue Jul 19 17:59:51 2022

@author: lbush
"""

import re

file = open("wb_ex.txt").read()

wb = re.findall(r"\d{2}(-)\d{4}", file)
print(wb)

file.close()