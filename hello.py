import ply.lex as lex
import ply.yacc as yacc
import  re
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'FOR',
    'ID',
    'EQUALE' ,
    'GREATER' ,
    'SMALLER' ,
    'TRUE',
    'SEMICOLOMN',
    'plus_plus',
    'minus_minus'

]
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_FOR = 'for'
t_ID = r'[a-z] [^for]'
t_EQUALE = r'\='
t_GREATER = r'\>'
t_SMALLER = r'\<'
t_TRUE = "true"
t_SEMICOLOMN = r'\;'
t_plus_plus = '\++'
t_minus_minus ='\--'
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out


# Give the lexer some input
data = input()
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

def p_forstmt(p):
    ''' for_stmt : FOR LPAREN  INIT  SEMICOLOMN   LOGICEXP  SEMICOLOMN ASSIMENT  RPAREN '''

def p_assimenr(p) :
  ''' ASSIMENT : ID EQUALE TERM PLUS EXPRESSION
                | ID EQUALE TERM MINUS EXPRESSION
                | ID EQUALE EXPRESSION
                | ID plus_plus
                | ID minus_minus
   '''

def p_init (p) :
    ''' INIT : ID EQUALE TERM PLUS EXPRESSION
             | ID EQUALE TERM MINUS EXPRESSION
             | ID EQUALE EXPRESSION
             | ID
    '''

def p_logic_expression(p) :
    '''LOGICEXP : ID GREATER EXPRESSION
                 | ID SMALLER EXPRESSION
                 | ID GREATER EQUALE EXPRESSION
                 | ID SMALLER EQUALE EXPRESSION
                 | ID EQUALE EQUALE EXPRESSION
                 | TRUE

     '''

def p_expression(p):
    ''' EXPRESSION : EXPRESSION PLUS TERM
                    | EXPRESSION MINUS  TERM
                    | TERM
    '''

def p_TERM(p):
    '''TERM : ID TIMES FACTOR
            | ID MINUS FACTOR
            | FACTOR
            | ID
    '''

def p_FACTOR(p) :
    ''' FACTOR : NUMBER TIMES NUMBER
               | NUMBER DIVIDE NUMBER
               | NUMBER

    '''

def p_error(p):
    print("Syntax error !")

# Build the parser
parser = yacc.yacc()


result = parser.parse(data)
print(result)











