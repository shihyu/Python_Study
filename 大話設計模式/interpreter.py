# -*- coding: cp950 -*-


class Context:
    def __init__(self):
        self.Input = None
        self.Output = None
        
class AbstractExpression:
    def Interpret(self, context):
        pass
    
class TerminalExpression(AbstractExpression):
    def Interpret(self, context):
        print '終端解釋器'
    
class NonTerminalExpression(AbstractExpression):        
    def Interpret(self, context):
        print '非終端解釋器'


if __name__ == '__main__':
    context = Context()
    list = []
    list.append( TerminalExpression() )
    list.append( NonTerminalExpression() )
    list.append( TerminalExpression() )
    list.append( TerminalExpression() )

    for exp in list:
        exp.Interpret(context)
