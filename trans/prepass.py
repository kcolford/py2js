import ast


class PrePass(ast.NodeTransformer):
    """Pass over the python ast to make it easier for the translation
    pass.

    """

    def visit_AugAssign(self, node):
        return ast.copy_location(
            ast.Assign(targets=[node.target],
                       value=ast.BinOp(node.target, node.op, node.value)),
            node)
