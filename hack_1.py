"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    for i in range(0, len(s), 3):
        txt = s[i:i+3]
        if len(txt) % 2 != 0:
            result = result[:i] + f"{txt[0]}{txt[1].upper()}{txt[2]}" + result[i+3:]
    return result
fn_hack_1("fooziman")
fn_hack_1("qux")
fn_hack_1("eq")
