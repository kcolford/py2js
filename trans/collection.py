"""This is the collection of all the other translator classes.
"""

import binary
import boolop
import expression
import statement

class Collection(binary.Binary,
                 boolop.BoolOp
                 expression.Expression,
                 statement.Statement):
    """The final front end class of the translation routines.
    """

    pass
