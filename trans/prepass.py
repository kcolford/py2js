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

    def visit_Compare(self, node):
        assert len(node.ops) == len(node.comparators)
        
        ret = [node.left]
        for i in range(len(node.ops)):
            ret[-1] = ast.BinOp(ret[-1], node.ops[i], node.comparators[i])
            ret.append(node.comparators[i])
        return ast.copy_location(
            ast.BoolOp(ast.And(), ret),
            node)
    
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.NotIn):
            return ast.copy_location(
                ast.UnaryOp(ast.Not(),
                            ast.BinOp(node.left, ast.In(), node.right)),
                node)
        
        return node
