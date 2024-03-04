"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = ""
    count = 0
    for i in s:
        if "o" in i:
            count += 1
            if count == 2:
                result += "o"
            else:
                result += "O"
        elif i == "i":
            result += "I"
        elif i == "u":
            result += "U"
        else:
            result += i
    return result
fn_hack_1("fooziman")
fn_hack_1("qux")
fn_hack_1("eq")
