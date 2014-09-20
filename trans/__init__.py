"""Translation package for converting python to java script.
"""

python_builtins = """
True = true;
False = false;
None = null;
"""

import collection

def translate(s):
    """Return the python code string s as string of javascript code.
    """

    return python_builtins + collection.Collection()(s)

