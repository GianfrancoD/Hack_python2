"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(s):
    result = list(s)
    listas = ["o", "i", "a", "u"]

    result = [i for i in result if i not in listas]

    return "".join(result)
fn_hack_2("fooziman")
fn_hack_2("barziman")
fn_hack_2("qux")
