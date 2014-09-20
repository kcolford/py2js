import translator
import ast

class Expression(translator.Translator):

    def visit_Name(self, node):
        return node.id

    def visit_Call(self, node):
        return (self.visit(node.func) + ".__call__(" +
                self.visit(node.args) + ")")

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

    def visit_Str(self, node):
        return "String(" + repr(node.s) + ")"

    def visit_Lambda(self, node):
        return ("function (" + self.visit(node.args) + ") {" +
                self.visit(node.body))

    def visit_IfExpr(self, node):
        return ("(" + self.visit(node.test) + " ? " +
                self.visit(node.body) + " : " + self.visit(node.orelse) + 
                ")")


