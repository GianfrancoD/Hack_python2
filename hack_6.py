"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s.copy()
    switchnumber = ["1","-","3","-","5"]
    if not result:
        result = ["0"]
    else:
        for i in range(len(result)+1):
            if i.__mod__(2) == 0:
                result[i-1:i+1] = "-"
            else:
                result[i-1:i+1] = [str(i)]
    return result

fn_hack_6(["a","b","c","d","e"])