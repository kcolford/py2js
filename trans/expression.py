import translator
import ast

class Expression(translator.Translator):

    def visit_Name(self, node):
        return node.id

    def visit_Call(self, node):
        return (self.visit(node.func) + ".__call__(" +
                ', '.join(self.visit(i) for i in node.args) + ")")

    def visit_Dict(self, node):
        pass

    def visit_UnaryOp(self, node):
        # If this is a "not" operator then we have to wrap it from the
        # outside, not the inside as we have been doing up until now.
        ret = "!Boolean" if isinstance(node.op, ast.Not) else ""

        return (ret + "(" + self.visit(node.operand) + "." +
                self.visit(node.op) + "())")

    def visit_Invert(self, node):
        return "__invert__"

    def visit_Num(self, node):
        t = ""
        if isinstance(node.n, int):
            t = "int"
        return t + "(" + str(node.n) + ")"
