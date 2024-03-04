"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s.copy()
    switchnumber = ["1",2,"3",4,"5"]
    if not result:
        result = [0]
    else:
        for i in range(len(result)):
            if result[i] in switch:
                if result[i] not in switchnumber:
                    result[i] = switchnumber[i]
    return result
switch = ["a","b","c","d","e"]
fn_hack_7(switch)
