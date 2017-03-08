#
# Custom procedure -- remove equals from school and district codes
#

import re
from tabstream.error import eprint

def clean_str( s ):
    return re.sub(r"[\"=]+","", s)

def clean_col( df, col ):
    if col not in df.columns:
        eprint ("Column not found: " + col )
        return df
    
    ret = df.copy()

    ret[col] = ret.apply(lambda x: clean_str(x[col]),axis=1)
    
    return ret
    
def clean_code_cols ( df ):

    ret = df.copy()
    
    ret = clean_col( ret, "school_code" )
    ret = clean_col( ret, "district_code" )
    
    return ret
