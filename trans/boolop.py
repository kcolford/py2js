import translator

class BoolOp(translator.Translator):
    """Translates boolean operations into java script.
    """

    def visit_BoolOp(self, node):
        return ("(" + self.visit(node.op).join(map(self.visit, node.values)) 
                + ")")
    def visit_And(self, node):
        return " && "
    def visit_Or(self, node):
        return " || "
