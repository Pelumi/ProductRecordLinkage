__author__ = 'pelumi'

import pandas as pd

PRODUCTS_FILE = "../../../data/products.txt"
LISTINGS_FILE = "../../../data/listings.txt"

def loadJsonToDf(filename):
    # read the entire file into a python array
    with open(filename, 'rb') as f:
        data = f.readlines()

    # remove the trailing "\n" from each line
    data = map(lambda x: x.rstrip(), data)
    data_json_str = "[" + ','.join(data) + "]"

    # now, load it into a pandas data frame
    df = pd.read_json(data_json_str)
    return df

products_df = loadJsonToDf(PRODUCTS_FILE)
listings_df = loadJsonToDf(LISTINGS_FILE)

print products_df.head(10)
print listings_df.head(10)

all_manufacturers = pd.unique(products_df.manufacturer.ravel())
all_model_numbers = pd.unique(products_df.model.ravel())
families = pd.unique(products_df.family.ravel())

print all_manufacturers
print ("Total manufacturers is: ", all_manufacturers.size)
print ("Total families is: ", families.size)
print ("Total models is: ", all_model_numbers.size)

