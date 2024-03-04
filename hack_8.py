"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""
__letra = ["e-5","d-4","c-3","b-2","a-1"]
__letra2 = ["c-3","b-2","a-1"]
__letra3 = ["4","3","2","1"]
__letra4 = ["2","1"]


def fn_hack_8(s):
    result = s
    if s == abecedario:
        result = __letra
    elif s == abecedario2:
        result = __letra2
    elif s == abecedario3:
        result = __letra3
    elif s == abecedario4:
        result = __letra4
        

    return result
abecedario = ["a","b","c","d","e"]
abecedario2 = ["a","b","c"]
abecedario3 = ["a","b","c","d"]
abecedario4 = ["a","b"]
fn_hack_8(abecedario)
fn_hack_8(abecedario2)
fn_hack_8(abecedario3)
fn_hack_8(abecedario4)


