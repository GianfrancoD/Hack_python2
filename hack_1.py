"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    for i in range(0,len(result),3):
        e = result[i:i+3]
        if len(e).__mod__(2) != 0:
           result = result[:i] + f"{e[0]}{e[1].upper()}{e[2]}" + result[i+3:]
    return result
fn_hack_1("fooziman")
fn_hack_1("qux")
fn_hack_1("eq")
