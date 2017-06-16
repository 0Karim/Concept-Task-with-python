#Task_Switch 1


#Import Library To Task
import ply.lex as lex
import ply.yacc as yacc


#reserved Words
reserved = {'switch' : 'SWITCH' , 'case' : 'CASE' , 'default' : 'DEFAULT' , 'break' : 'BREAK'}

#Tokens in code
tokens = ['NUMBER' , 'PLUS' , 'MINUS' , 'TIMES' , 'DIVID' , 'LPAREN' , 'RPAREN' , 'LCARL' , 'RCARL' , 'ID' , 'COLON' , 'SEMICOLON' , 'EQUL' ] + list(reserved.values())

#Regualar Expression
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVID = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCARL = r'{'
t_RCARL = r'}'
t_COLON = r':'
t_SEMICOLON = r';'
t_EQUL = r'='

#Define The Regualr Expression To Numbers in code as token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Define function Regualr Expression To The token to variables
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value , 'ID')   #check for resreved word
    return t


#Define rule to keep track of line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#string contain ignored charactres
t_ignore = r' \t'

#Error Handling function that belong to lex
def t_error(t):
    print('Illegal charcter "%s"' % t.value[0])
    t.lexer.skip(1)



#Bulid Lexer
lexer = lex.lex()



#From Here Begin Our BNF Rule we start as switch stmts or empty code
def p_switch(p):
    '''
        switch : switch_stmt
              | empty
    '''


#Rule Describe what happen if empty it will empty token
def p_empty(p):
    '''
    empty :
    '''

#Rule Start To make switch code it should be 3 Cases and one Default if More Syntax Error & if less Synatx Error
def p_switch_stmt(p):
    '''
        switch_stmt : SWITCH LPAREN ID RPAREN LCARL list_code
    '''

def p_list_code(p):
    '''
        list_code : CASE var COLON stmt_list SEMICOLON BREAK SEMICOLON
                 | CASE var COLON stmt_list SEMICOLON BREAK SEMICOLON list_code
                 | default

    '''

def p_default(p):
    '''
        default : DEFAULT COLON stmt_list SEMICOLON BREAK SEMICOLON RCARL
    '''


#Rule To define variable of each case like case 'A' or case 1
def p_var(p):
    '''
        var : NUMBER
            | ID
    '''

#Rule Define stmt_list in each case statment that hold and Arithmatic expression or Assignment expression it can hold stmt or expression
def p_stmt_list(p):
    '''
        stmt_list : stmt
                 | expression
    '''

#Rule Define each stmt that contain Assignment or Expression
def p_stmt(p):
    '''
        stmt : ID EQUL expression
            | ID
    '''

#Rule Define each expression '+' or '-'
def p_expression(p):
    '''
        expression : expression PLUS term
                  | expression MINUS term
                  | term
    '''


#Rule Define each term '*' or '/'
def p_term(p):
    '''
        term : term TIMES factor
            | term DIVID factor
           | factor
    '''


#Rule Define factor as Number or epression between parnthesses '(expression)'
def p_factor(p):
    '''
        factor : NUMBER
              | LPAREN expression RPAREN
    '''

#Rule Define Error Handling in Yacc that define Error as Syntax Error in the code if the User
def p_error(p):
    if p:
        print('Syntax Error in input at "%s" !' % p.value)



#Build Yacc to check Synatx and build parser
parser = yacc.yacc()


#Parse The Code and check it's Syntax Error
parser.parse("switch(x){"
             "case A:"
             "  result = 5 + 3;"
             "  break;"
             "case B : "
             " result = 4/9;"
             "  break;"
             "case C:"
             "  result = 7;"
             "break;"
             "case D:"
             "  result = 0;"
             "break ;"
             "default : "
             "     b = 8;"
             "      break;"
             "}")




