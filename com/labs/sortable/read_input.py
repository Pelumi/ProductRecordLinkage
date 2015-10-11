__author__ = 'pelumi'

from  textblob import TextBlob
import pandas as pd

PRODUCTS_FILE = "../../../data/products.txt"
LISTINGS_FILE = "../../../data/listings.txt"
all_manufacturers = []
all_model_numbers = []
families = []

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

def find_manufacurer(title, set):
    tokens = extract_tokens(title)
    for token in tokens:
        #print(token)
        if token in set:
            print(token)
            return token

def extract_tokens(title):
    #take to lower case
    blob = TextBlob(title).lower()
    #TODO extract bigrams and trigrams also
    #bigrams = blob.ngrams(2)
    #trigrams = blob.ngrams(3)
    #unigrams = blob.ngrams(1)
    return blob.words

def describe_data(df):
    print df.describe(percentiles=True)

def products_with_2_propertie(df, property1="manufacturer", value1="", property2="family", value2=""):
    print df.loc[(df[property1] == value1) & (df[property2] == value2)]

def products_with_property(df, property="manufacturer", value=""):
    print df.loc[(df[property] == value) & (df["family"] == "IXUS") ]

def create_data_hash():
    global all_manufacturers, families, all_model_numbers
    all_manufacturers = set(pd.unique(products_df["manufacturer"].str.lower().ravel()))
    #print(all_manufacturers)
    all_model_numbers = set(pd.unique(products_df["model"].str.lower().ravel()))
    families = set(pd.unique(products_df["family"].str.lower().ravel()))

    # print all_manufacturers
    # print(all_model_numbers)
    # print ("Total manufacturers is: ", all_manufacturers.size)
    # print ("Total families is: ", families.size)
    # print ("Total models is: ", all_model_numbers.size)

products_df = loadJsonToDf(PRODUCTS_FILE)
create_data_hash()
#describe_data(products_df)
#listings_df = loadJsonToDf(LISTINGS_FILE)

find_manufacurer("Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)", all_model_numbers)
#products_with_property(products_df, "manufacturer", "Canon")

