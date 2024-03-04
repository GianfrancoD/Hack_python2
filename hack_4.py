
"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = list(s)
    for i in range(len(result)):
        remove = result
        if remove[i] in "f" or remove[i] in "n" or remove[i] in "b":
            remove[i] = ""

    return "".join(remove)
fn_hack_4("fooziman")
fn_hack_4("barziman")
fn_hack_4("qux")

