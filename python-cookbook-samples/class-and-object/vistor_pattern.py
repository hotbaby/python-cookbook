
class NodeVistor(object):
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname)
        if meth is None:
            meth = self.geneic_visit
        return meth(node)
    
    def geneic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_'+type(node).__name__))


class Evaluator(NodeVistor):
    def visit_Number(self, node):
        return node.value
    
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)
    
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
    
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.rights)