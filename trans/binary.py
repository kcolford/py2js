"""This is the class that manages binary operators.
"""


import ast
import translator


class Binary(translator.Translator):
    """This translates binary operators.
    """

    def visit_BinOp(self, node):
        # With the "in" operator, we have to swap the left and right
        # operands.
        if isinstance(node.op, ast.In):
            node.left, node.right = node.right, node.left

        # This requires special treatment because we have to use the
        # builtin === operator of java script.
        if isinstance(node.op, ast.Is):
            return self.visit(node.left) + ' === ' + self.visit(node.right)
        elif isinstance(node.op, ast.IsNot):
            return self.visit(node.left) + ' !== ' + self.visit(node.right)

        return (self.visit(node.left) + "." + self.visit(node.op) + 
                "(" + self.visit(node.right) + ")")

    visit_Compare = visit_BinOp

    # Begin arithmetic.
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
    # Begin comparision operators.
    def visit_Eq(self, node):
        return "__eq__"
    def visit_Gt(self, node):
        return "__gt__"
    def visit_GtE(self, node):
        return "__ge__"
    def visit_In(self, node):
        return "__contains__"
    def visit_Lt(self, node):
        return "__lt__"
    def visit_LtE(self, node):
        return "__le__"
    def NotEq(self, node):
        return "__ne__"
