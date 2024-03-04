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
        for i in range(len(result)):
            if result[i] in switch:
                if result[i] not in switchnumber:
                    result[i] = switchnumber[i]
    return result
switch = ["a","b","c","d","e"]
fn_hack_6(switch)