"""This is the collection of all the other translator classes.
"""

import binary
import boolop
import classes
import expression
import statement

class Collection(binary.Binary,
                 boolop.BoolOp,
                 classes.Classes,
                 expression.Expression,
                 statement.Statement):
    """The final front end class of the translation routines.
    """

    pass
