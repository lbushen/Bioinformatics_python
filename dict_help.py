# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 21:43:51 2022

@author: lbush
"""

Renzyme = {
           'EcoRI':r'GATTC',
           'AvaII':r'GG(A|T)CC'
           }

Renzyme = {
           'EcoRI':'GATTC',
           'AvaII':r'GGWCC'
           }
# printing the value from a key   
print(Renzyme['AvaII'])


# adding key/value to a dictionary
Renzyme['BisI'] = r'GC[ATGC]GC'

# printing all the keys of dictionary Renzyme
for key in Renzyme.keys():
    print(key)

#create empty dictionary    
aaseq = {}

# add key/values to the empty dictionar
aaseq['noAcid'] = "kateadk"
aaseq['noAcid2'] = 'mvarr'

print(aaseq)

print(aaseq.items())

# print all the values in dictionary aaseq
for values in aaseq.values():
    print (values)


