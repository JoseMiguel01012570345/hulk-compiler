import production_class_representation as pcr

def binary_opt(self:pcr.binary_opt):
    return [ self.left_node , self.right_node ]

def var(self:pcr.variable):
    return [None]

def brackets(self:pcr.ASTNode):
    return [self.expression]

def replacement(self:pcr.ASTNode):
    return [self.replacement]

