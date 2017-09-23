#-----------------------------------------------------------------------------
# scanner.py
#
# Nombre: Jorge Molina Rojas
# Ingenieria Civil en Computación e Informática
# Universidad Católica del Norte, Antofagasta, Chile.
#
# El trabajo del analizador lexico o scanner, es transdormar un flujo de caracteres
# en un flojo de tokers. Los tokes a evaluar son los siguientes:
# -key words: ELSE IF INT VOID RETURN WHILE
# -simbolos especiales: + - * / < <= > >= == <> = ( ) [ ] { } ! ? </ /> , ;
# -identificador (ID)
# -números (NUM)
# -----------------------------------------------------------------------------
import ply.lex as lex

# lista de los nombres de los tokens
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LSQUAREBRACKET',
    'RSQUAREBRACKET',
    'LESS',
    'GREATER',
    'MUCHSMALLER',
    'MUCHGREATER',
    'EQUAL',
    'INEGUAL',
    'COMMA',
    'SEMICOLON',
    'ASSIGN',
    'MULTCOMMMENT',
    'LINECOMMENT',
    'ID',
    'NUM'
)

#listado de palabras reservadas (key: valor )
reserved = {
    'else': 'ELSE',
    'if': 'IF',
    'int': 'INT',
    'void': 'VOID',
    'return': 'RETURN',
    'while': 'WHILE'
}

tokens = tokens+tuple(reserved.values())

# Reglas de las expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_LESS = r'<'
t_GREATER = r'\>'
t_MUCHSMALLER = r'\<<'
t_MUCHGREATER = r'\>>'
t_EQUAL = r'\=='
t_INEGUAL = r'\<>'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ASSIGN = r'='

t_MULTCOMMMENT = r'<\/(\s*|.*?)*\/>'
t_LINECOMMENT = r'((\?|!).*)'

# Regla que contiene caracteres ignorados (espacios y tabs)
t_ignore  = ' \t'


def t_ID (t):
    r'[A-Za-z]((_?[a-zA-Z]+)*_?([a-z0-9])+)?'
    # El método get () devuelve un valor para la key dada. Si la key no está disponible en el diccionario, entonces devuelve el valor predeterminado 'ID'.
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# Regla de manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_NUM(t):
    r'(0[0-9])|[1-9][0-9]+'
    t.value = int(t.value)
    return t

# Construir el lexer
lexer = lex.lex()

# Dar al analizador léxico algún input
lexer.input('<a_=a''8')

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # no hay mas input
    print(tok)

