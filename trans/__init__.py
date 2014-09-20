"""Translation package for converting python to java script.
"""

python_builtins = """
True = true;
False = false;
None = null;

function Dict(keys, values) {
   var ret = {};
   for (var i=0; i<keys.length; i++) {
      ret[keys[i]._to_js_string] = ret[values[i]];
   }
}

"""

import collection

def translate(s):
    """Return the python code string s as string of javascript code.
    """

    return python_builtins + collection.Collection()(s)

