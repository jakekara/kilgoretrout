from tabstream.error import eprint
from clean_code_cols import clean_code_cols as ccc

registry = {
    "clean_code_columns":ccc
}


def do_procedure( df, p ):
    if p not in registry:
        eprint( "Procedure not found: " + str(p) )
        exit(1)

    return registry[p](df)

def do_procedures( df, p_arr ):
    ret = df
    for p in p_arr:
        ret = do_procedure( ret , p )

    return ret
