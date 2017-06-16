import ply.lex as lex
import ply.yacc as yacc
import sys

# Reserved Words
reserved = { 'for' : 'FOR' }



# List of token names
tokens = ['NUMBER' ,
          'PLUS' ,
          'MINUS' ,
          'TIMES' ,
          'DIVISION' ,
          'LPAREN' ,
          'RPAREN' ,
          'ID' ,
          'COMMA' ,
          'SEMICOLON' ,
          'EQUL' , 
          'LESSTHAN' ,
          'GREATERTHAN' ,
          'INCREMENT',
          'DECREMENT',
          'OPEQUAL',
          'INT',
          'FLOAT'] + list(reserved.values())


# Regualar Expression
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUL = r'='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_INT = 'int'
t_FLOAT = 'float'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


def t_INCREMENT(t):
    r'\+{2}'
    t.value = int(t.value)
    return t


def t_DECREMENT(t):
    r'-{2}'
    t.value = int(t.value)
    return t



def t_OPEQUAL(t):
    r'[-+*/><=!]='
    t.value = int(t.value)
    return t


#Define rule to keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    

#String contain ignored characters
    t_ignore  = ' \t'
    
    
#Error handling function
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
    
# Build the lexer
    lexer = lex.lex()    
    
# Store a new input string
    data = input()
    lexer.input(data)
    
    
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
        
        

#==========================================================================================


def p_forstmt(p):
    '''
    for_stmt : FOR LPAREN INIT SEMICOLON CONDITION SEMICOLON ASSIGNMENT
             | FOR LPAREN TYPE INIT SEMICOLON CONDITION SEMICOLON ASSIGNMENT
    '''
    
    
def p_init(p):
    '''
    init : VAR
         | VAR COMMA INIT
    '''
    
def p_var(p):
    '''
    var : ID EQUAL NUM
        | EXPRESSION
        | ID
    '''
    
def p_expression(p):
    '''
    expression : ID PLUS EQUAL NUM
               | ID MINUS EQUAL NUM
               | ID MULTIPLY EQUAL NUM
               | ID DIVIDE EQUAL NUM
               | ID EQUAL ID PLUS NUM
               | ID EQUAL ID MINUS NUM
               | ID EQUAL ID MULTIPLY NUM
               | ID EQUAL ID DIVIDE NUM
    '''
    

def p_condition(p):
    '''
    condition : ID GREATERTHAN NUM
              | ID LESSTHAN NUM
              | ID GREATERTHANOREQUAL NUM
              | ID LESSTHANOREQUAL NUM
              | ID EQUALEQUAL NUM
              | ID NOTEQUAL NUM
    '''
    
    
def p_increment(p):
    '''
    increment : PLUS PLUS ID
              | ID PLUS PLUS
              | MINUS MINUS ID
              | ID MINUS MINUS
    '''
    
    
def p_assignment(p):
    '''
    assinment : increment
              | expression
    '''
    
    
def p_type(p):
    '''
    type : INT 
         | FLOAT
    '''
    
def p_error(p):
    print('Syntax Error in input !')
    
    
    parser = yacc.yacc()