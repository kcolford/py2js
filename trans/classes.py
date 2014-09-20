import translator
import ast


class Classes(translator.Translator):
    """This translates class definitions into java script.
    """

    def visit_ClassDef(self, node):
        ret = ""
        ret += "function _Py2JS_" + node.name + "() {"
        ret += ' '.join(self.visit(i) for i in node.body)
        for i in get_ids(node):
            ret += "this." + i + " = function () { " + \
                   i + "(this, arguments);};"
        ret += "}"
        ret += node.name + " = type.__call__(" + node.name + ", ["
        ret += ', '.join(self.visit(i) for i in node.bases)
        ret += "], new _Py2JS_" + node.name + "()"
        ret += ")"
        return ret

class Modules(translator.Translator):
    """This translates module definitions into java script.
    """

    def visit_Module(self, node):
        sym = symtable.symtable(node, "", "exec")
        ret = ""
        ret += "function _Py2JS_module_def() {"
        ret += ' '.join(self.visit(i) for i in node.body)
        for i in sym.get_identifiers():
            ret += "this." + i + " = " + i + ";"
        ret += "}"
        return ret

def get_ids(node):
    """Get the identifiers in an AST object.
    """

    class walker(ast.NodeVisitor):
        out = []
        def __call__(self, node):
            self.visit(node)
            return self.out
        def visit_FunctionDef(self, node):
            self.out.append(node.name)
        def visit_Assign(self, node):
            self.visit(node.targets)
        def visit_Name(self, node):
            self.out.append(node.id)
    
    return walker()(node)

