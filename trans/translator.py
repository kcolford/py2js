"""The Translator class that all classes will inheirit from.
"""

import ast
import prepass


class Translator(ast.NodeVisitor):
    """The base class that all translations inheirit from.
    """

    def __call__(self, code):
        """Walk over the code and create java script
        """

        if isinstance(code, str) or isinstance(code, unicode):
            code = ast.parse(code)

        code = prepass.PrePass().visit(code)

        return self.visit(code)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node.
        """

        return ' '.join(self.visit(i) for i in ast.iter_child_nodes(node))
        
    def visit(self, node):
        if isinstance(node, list):
            assert False
        return ast.NodeVisitor.visit(self, node)

