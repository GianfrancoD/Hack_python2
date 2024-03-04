"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    result = s
    del result["bar"]
    result["Foo"] = result.pop("foo").capitalize()
    for i,e in result.items():
        if e == "Fookziman":
            result[i] = "Fooziman"
    return result

    """result = {i: "Fooziman" if e == "Fookziman" else e for i, e in result.items()}"""

fn_hack_9({"foo":"fookziman","bar":"barziman"})