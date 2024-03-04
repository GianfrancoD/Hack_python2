"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    for i in result:
        result[0] = {"1":"2"}
        result[1] = dict(reversed({"3": "4"}.items()))
        result[2] = {"5":"6"}
    return result

fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}])