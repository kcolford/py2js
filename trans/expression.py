import translator

class Expression(translator.Translator):
    
    def visit_Call(self, node):
        return (self.visit(node.func) + ".__call__(" + 
                ', '.join(self.visit(i) for i in node.args) + ")")
    def visit_Dict(self, node):
        pass
