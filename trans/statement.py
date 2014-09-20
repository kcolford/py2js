import translator


class Statement(translator.Translator):
    """
    """

    def visit_Assert(self, node):
        pass

    def visit_Assign(self, node):
        return (self.visit(node.targets) + " = " +
                self.visit(node.value) + ';')
    def visit_Print(self, node):
        return ("console.log(" + self.visit(node.values) + ");")

    def visit_If(self, node):
        return ("if (" + self.visit(node.test) + ") {" +
                ' '.join(self.visit(i) for i in node.body) + "} else {" +
                ' '.join(self.visit(i) for i in node.orelse) + "}")
