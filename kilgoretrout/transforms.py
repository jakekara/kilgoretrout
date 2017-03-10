#
# core transformations
#


import re, json
import pandas as pd

from error import eprint

def select( df, cols_arr ):
    try:
        return df[cols_arr]
    except Exception, e:
        eprint( "Error selecting columns: " + str(e) )
        exit( 1 )

def drop( df, col_arr ):
    cols = filter( lambda x: x not in col_arr, df.columns )
    return select( df, cols )

def pretty_cols( df ):
    
    cols = map( lambda x: re.sub(
        r'[^a-zA-Z0-9_]+','_', x
    ).lower(), df.columns)
    
    ret = df.copy()
    ret.columns = cols
    
    return ret

# rename columns, given a json array of new column names
def rename_cols( df, set_str):

    if set_str is None:
        return df

    try:
        # new_cols = # json.loads(set_str)s
        new_cols = set_str.split(",")
    except:
        eprint ( set_str )
        eprint("--colnames argument must be JSON array")
        exit(1)

    if type(new_cols) is not list:
        eprint("--colnames argument must be JSON array")
        exit(1)

    if len(new_cols) != len(df.columns):
        eprint("--colnames array must have one column per table,\
excluding dropped cols")

    ret = df.copy()
    ret.columns = new_cols
    # eprint(ret.head())
    return ret
