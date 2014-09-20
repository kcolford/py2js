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
        return ("console.log(" +
                ', '.join(self.visit(i) for i in node.values) + 
                ");")

    def visit_If(self, node):
        return ("if (" + self.visit(node.test) + ") {" +
                ' '.join(self.visit(i) for i in node.body) + "} else {" +
                ' '.join(self.visit(i) for i in node.orelse) + "}")

    def visit_FunctionDef(self, node):
        return ("function " + node.name + "(" + self.visit(node.args) + 
                ") {" + ' '.join(map(self.visit, node.body)) + "};")
