# -*- coding: cp950 -*-
'''
interpreter 範例：音樂解譯器
'''

class PlayContext:
    '''
    演奏內容
    '''
    def __int__(self):
        # 演奏文字
        self.PlayText = None


class Expression:
    def Interpret(self, context):
        if len(context.PlayText) == 0:
            return
        else:
            tmp = context.PlayText.split(' ')            
            playKey = tmp[0]
            playValue = tmp[1]

            del tmp[0]
            del tmp[0]            

            
            context.PlayText = ' '.join(tmp)
            
            self.Execute(playKey, playValue)
            
    def Execute(self, key, value):
        '''
        執行
        抽象方法，不同文法子類別，有不同的執行處理
        '''
        pass

class Note(Expression):
    __tbl = {'C':'1', 'D':'2', 'E':'3', 'F':'4', 'G':'5', 'A':'6', 'B':'7'}
    def Execute(self, key, value):
        if Note.__tbl.has_key(key):
            print '%s ' % Note.__tbl[key]
        

class Scale(Expression):
    __tbl = {'1':'低音', '2':'中音', '3':'高音'}
    def Execute(self, key, value):
        if Scale.__tbl.has_key(value):
            print '%s ' % Scale.__tbl[value]
        

class Speed(Expression):
    def Execute(self, key, value):
        if value < 500:
            print '快速'
        elif value >= 1000:
            print '慢速'
        else:
            print '中速'
            
if __name__ == '__main__':
    context = PlayContext()
    print '上海灘:'
    context.PlayText = 'O 2 E 0.5 G 0.5 A 3 E 0.5 G 0.5 D 3 E 0.5 G 0.5 A 0.5 O 3 C 1 O 2 A 0.5 G 1 C 0.5 E 0.5 D 3'
    while len(context.PlayText)>0:
        k = context.PlayText[0]
        if k == 'O':
            expression = Scale()
        elif k in ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'P']:
            expression = Note()
        elif k == 'T':
            expression = Speed()
        else:
            print context.PlayText
            raise PlayContext
        expression.Interpret(context)


        
