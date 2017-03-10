#
# Custom procedure -- add a district_code column based on a school_code column
#                     required cols: school_code, district, school
#

from kilgoretrout.error import eprint
import json

def district_code( df, district_name ):

    if type(district_name) is not str or district_name is None:
        return None
    
    match = df[df["school"] == district_name]

    if len(match.index) > 1:
        eprint("Multiple entries found for " + district_name)
        eprint(match.to_json(orient="records"))
        return None

    if len(match.index) <= 0:
        eprint("No entries found for " + district_name)
        return None

    return str(match.iloc[0]["school_code"]).zfill(7)

def add_district_code( df ):

    ret = df.copy()
    
    required = ["school_code","district","school"]

    for r in required:
        if r not in ret.columns:
            raise Exception("Missing column " + r)

    ret["district_code"] = ret.apply(
        lambda x: district_code( ret, x["district"] ), axis=1).astype(str)

    return ret
