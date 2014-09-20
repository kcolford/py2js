"""This is the collection of all the other translator classes.
"""

import binary
import translator
import expression

class Collection(translator.Translator, binary.Binary, expression.Expression):
    """The final front end of the translation routines.
    """

    pass
