#
# Custom procedure -- remove equals from school and district code columns,
#                     or from all columns with clean_all_codes
#

import re# , math
from tabstream.error import eprint

def clean_str( s ):
    if s is None:
        return None

    if type(s) is str:
        ret =  re.sub(r"[\"=]+","", s)
        return ret
    
    return s
        
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

def clean_all_cols ( df ):
    
    ret = df.copy()
    
    for c in ret.columns:
        ret = clean_col(ret, c)
        
    return ret
