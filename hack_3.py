"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    a = "@"
    e = "3"
    i = "¡"
    o = "0"
    u = "v"
    listados = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v', 'm' : 'm', 'z' : 'z', 'r' : 'r'}
    result = ""
    for e in s:
        if e in listados:
            result += listados[e]
        else:
            result += e.upper()
    
    return result
fn_hack_3("fooziman")
fn_hack_3("barziman")
fn_hack_3("3q")
fn_hack_3("qu")
fn_hack_3("qux")

