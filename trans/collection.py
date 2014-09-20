"""This is the collection of all the other translator classes.
"""

import binary
import translator
import expression
import statement

class Collection(statement.Statement,
                 binary.Binary,
                 expression.Expression):
    """The final front end of the translation routines.
    """

    pass
