"""This is the class that manages binary operators.
"""


import translator


class Binary(translator.Translator):
    """This translates binary operators.
    """

    def visit_BinOp(self, node):
        return (self.visit(node.left) + "." + self.visit(node.op) + 
                "(" + self.visit(node.right) + ")")

    def visit_Add(self, node):
        return "__add__"
    def visit_BitAnd(self, node):
        return "__and__"
    def visit_BitOr(self, node):
        return "__or__"
    def visit_BitXor(self, node):
        return "__xor__"
    def visit_Div(self, node):
        return "__div__"
    def visit_FloorDiv(self, node):
        return "__floordiv__"
    def visit_LShift(self, node):
        return "__lshift__"
    def visit_Mod(self, node):
        return "__mod__"
    def visit_Mult(self, node):
        return "__mul__"
    def visit_Pow(self, node):
        return "__pow__"
    def visit_RShift(self, node):
        return "__rshift__"
    def visit_Sub(self, node):
        return "__sub__"
