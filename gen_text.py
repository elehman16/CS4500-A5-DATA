# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:01:28 2020

@author: Eric Lehman
"""

def string_to_mb(s):
    """ String size to MB. """
    return len(s.encode('utf-8')) / 1000000

def gen_data(mb_size, num_columns):
    column = '1,' * num_columns + '\n'
    column_bytes = string_to_mb(column)
    num_rows = int(mb_size / column_bytes) + 1        
    return column * num_rows

def main(mb_size):
    f = 'datafile_{}MB.txt'.format(mb_size)
    str_data = gen_data(mb_size, num_columns=10)
    with open(f, 'w') as tmp: tmp.write(str_data)
    
for i in range(1, 11): main(i * 10)
    