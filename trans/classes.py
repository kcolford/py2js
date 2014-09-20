import translator
import symtable


class Classes(translator.Translator):
    """This translates class definitions into java script.
    """

    def visit_ClassDef(self, node):
        sym = symtable.symtable(node, "", "exec")
        ret = ""
        ret += "function _Py2JS_" + node.name + "() {"
        ret += ' '.join(self.visit(i) for i in node.body)
        for i in sym.get_identifiers():
            ret += "this." + i + " = " + i + ";"
        ret += "}"
        ret += node.name + " = type.__call__(" + node.name + ", ["
        ret += ', '.join(self.visit(i) for i in node.bases)
        ret += "], new _Py2JS_" + node.name + "()"
        ret += ")"

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
