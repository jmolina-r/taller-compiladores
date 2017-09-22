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
    'RSQUAREBRACKET'
    'LESS',
    'GREATER',
    'MUCHSMALLER',
    'MUCHGREATER',
    'EQUAL',
    'INEGUAL'
    'COMMA',
    'SEMICOLON',
    'ASSIGN'
    'MULTCOMMMENT',
    'LINECOMMENT',
    'ID',
    'NUM'
)

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
t_LESS = r'\<'
t_GREATER = r'\>'
t_MUCHSMALLER = r'\<<'
t_MUCHGREATER = r'\>>'
t_EQUAL = r'\=='
t_INEGUAL = r'\<>'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ASSIGN = r'\='


reserved = {


}