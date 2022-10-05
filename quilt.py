def createQuilt(h, w):
    mat = [[0 for x in range(w)] for y in range(h)] 
    return mat

def A():
    q = createQuilt(2,2)
    q[0][0] = '/'
    q[0][1] = '/'
    q[1][0] = '/'
    q[1][1] = '+'
    return q

def B():
    q = createQuilt(2,2)
    q[0][0] = '-'
    q[0][1] = '-'
    q[1][0] = '-'
    q[1][1] = '-'
    return q

def turn(q):
    originalH = len(q)
    originalW = len(q[0])
    newQ = createQuilt(originalW, originalH)
    for i in range(originalW):
        for j in range(originalH):
            if q[j][i] == '-':
                newQ[i][originalH-j-1]='|'
            elif q[j][i] == '|':
                newQ[i][originalH-j-1]='-'
            elif q[j][i] == '/':
                newQ[i][originalH-j-1]='\\'
            elif q[j][i] == '\\':
                newQ[i][originalH-j-1]='/'
            else:
                newQ[i][originalH-j-1]=q[j][i]
    return newQ

def sew(q1, q2):
    q1H = len(q1)
    q1W = len(q1[0])
    q2H = len(q2)
    q2W = len(q2[0])
    newQ = createQuilt(q1H, q1W + q2W)
    for i in range(len(newQ)):
        for j in range(len(newQ[0])):
            if j<q1W :
                newQ[i][j] = q1[i][j]
            else: 
                newQ[i][j] = q2[i][j-q1W]
    return newQ

def printQuilt(q):
    for i in range(len(q)):
        for j in range(len(q[0])):
            print(q[i][j], end =" ")
        print('\n')



tokens = ('TURN', 'SEW', 'LPAREN', 'RPAREN', 'COMA', 'PUNTOCOMA', 'A', 'B')

# Tokens
t_ignore = ' \t\n'
t_TURN = 'turn'
t_SEW = 'sew'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PUNTOCOMA = r';'
t_COMA = r','
t_A = r'A'
t_B = r'B'


def t_error(t):
    print("Syntax Error at '%s'" % t.value)

#Build the Lexer
from types import NoneType
import ply.lex as lex
lex.lex()

#Parsing Rules
def p_lista_declaracion(t):
    '''lista_declaracion : declaracion
                         | declaracion lista_declaracion'''
       
        
def p_declaracion(t):
    'declaracion : quilt PUNTOCOMA'
    t[0]=t[1]
    print("Quilt")
    if t[0] is not None:
        printQuilt(t[0])

def p_quilt(t):
    '''quilt : A
             | B
             | TURN LPAREN quilt RPAREN
             | SEW LPAREN quilt COMA quilt RPAREN'''
    if t[1] == 'A':
        t[0] = A()
    elif t[1] == 'B':
        t[0] = B()
    elif t[1] == 'turn':
        t[0] = turn(t[3])
    elif t[1] == 'sew':
        if len(t[3]) != len(t[5]):
            print("Error: Alturas diferentes")
            return
        elif len(t[3]) == len(t[5]):
            t[0]=sew(t[3],t[5])
    

def p_error(t):
    print("Syntax error in input '%s'! at line %d" % (t.value, t.lexer.lineno_for_token(t)))

import ply.yacc as yacc
yacc.yacc()

myFile = open("archivo.txt")
yacc.parse(myFile.read())

lexer = lex
with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)
 
            for token in lexer:
                if token.type == 'path':
                    print("Path Correct: ", token.value)
 
        except EOFError:
            break


