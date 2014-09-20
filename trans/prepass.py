import ast


class PrePass(ast.NodeTransformer):
    """Pass over the python ast to make it easier for the translation
    pass.

    """

    def visit_AugAssign(self, node):
        pass
