__author__ = 'pelumi'

import pandas as pd

PRODUCTS_FILE = "../../../data/products.txt"
LISTINGS_FILE = "../../../data/products.txt"

# read the entire file into a python array
with open(PRODUCTS_FILE, 'rb') as f:
    data = f.readlines()

# remove the trailing "\n" from each line
data = map(lambda x: x.rstrip(), data)
data_json_str = "[" + ','.join(data) + "]"

# now, load it into pandas
products_df = pd.read_json(data_json_str)

print products_df.head(10) # df.name.ravel()

all_manufacturers = pd.unique(products_df.manufacturer.ravel())




print all_manufacturers
print all_manufacturers.size