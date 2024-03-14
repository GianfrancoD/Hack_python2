"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""
def fn_hack_8(s):
    result = s
    ls = []
    par = len(result).__mod__(2)
    if par == 0:
        for index, value in enumerate(result):
            result = str(index+1)
            ls.append(result)
    if par == 1:
        for i, e in enumerate(result):
            result = str(e) + "-" + str(i+1)
            ls.append(result)
    result = ls[::-1]
    return result

print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))


