# -----------------------------------------------------------------------------
# scanner.py
#
# Nombre: Jorge Molina Rojas
# Ingeniería Civil en Computación e Informática
# Universidad Católica del Norte, Antofagasta, Chile.
#
# El trabajo del analizador léxico o scanner, es transformar un flujo de caracteres
# en un flojo de tokers. Los tokes a evaluar son los siguientes:
# -key words: ELSE IF INT VOID RETURN WHILE
# -simbolos especiales: + - * / < <= > >= == <> = ( ) [ ] { } ! ? </ /> , ;
# -identificador (ID)
# -números (NUM)
# -----------------------------------------------------------------------------
from os import scandir, getcwd
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

# listado de palabras reservadas (key: valor )
reserved = {
    'else': 'ELSE',
    'if': 'IF',
    'int': 'INT',
    'void': 'VOID',
    'return': 'RETURN',
    'while': 'WHILE'
}

tokens = tokens + tuple(reserved.values())

# Reglas de las expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_LESS = r'<'
t_GREATER = r'\>'
t_MUCHSMALLER = r'\<='
t_MUCHGREATER = r'\>='
t_EQUAL = r'\=='
t_INEGUAL = r'\<>'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='

t_MULTCOMMMENT = r'<\/(\s*|.*?)*\/>'
t_LINECOMMENT = r'(\?|!).*'


# Regla que contiene caracteres ignorados (espacios y tabs)
t_ignore = ' [\t\'\n]*'


def t_ID(t):
    r'([A-Za-z](_?[a-zA-Z0-9]+)*_?([a-z0-9])+|[a-z])|(?i)else|(?i)if|(?i)int|(?i)void|(?i)return|(?i)while'
    # El método get () devuelve el 'valor' para la 'key' dada. Si la key no está disponible en el diccionario,
    # entonces devuelve el valor predeterminado 'ID'.
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# Regla de manejo de errores
list_error = []
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    list_error.append(str(t.value[0])) #agrega el valor del error a una lista
    t.lexer.skip(1)



def t_NUM(t):
    r'(0[0-9])|[1-9][0-9]+'
    t.value = int(t.value)
    return t


# retorna lista de archivos de ejemplos ubicados en el directorio 'file'
def listarArchivos(ruta=getcwd() + '\\file'):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def lecturaArchivo(rutaArch):
    archivo = open(rutaArch,'r')
    lineas = archivo.read()
    archivo.close()
    print('-----------------CÓDIGO----------------------')
    print(lineas)
    print('---------------------------------------------\n')
    print('Análisis Léxico')
    return lineas


def getcodigo():
    print(getcwd())
    print('-------------------------------------------')
    print('        TALLER COMPILADORES: SCANNER')
    print('-------------------------------------------')
    print('Estos son los archivos de prueba disponibles en la carpeta \'file\':')

    list_Arch=listarArchivos()
    if len(list_Arch)==0:
        print('No se encuentran archivos de prueba :(')
    else:
        #imprimir lista de archivos disponibles en la carpeta 'file'
        for arch in list_Arch:
            print(arch)
        #seleccionar archivo
        file_name = input('Favor de ingresar el nombre del archivo a utilizar:\n')
        while (file_name in list_Arch)!= True:
            print('Archivo no encontrado..\n')
            file_name = input('Favor de ingresar el nombre del archivo a utilizar:\n')

        #ruta del archivo seleccionado
        rutaArch=getcwd() + '\\file\\'+file_name
        #obtener código fuente del archivo
        codigofuente=lecturaArchivo(rutaArch)

    return (codigofuente)


codigofuente = getcodigo()

# Construir el lexer
lexer = lex.lex()

# Dar al analizador léxico algún input
lexer.input(codigofuente)

#archivo salida: 'tokens.txt'
arch_salida = open('tokens.txt','w')
arch_salida.write('Token'+'  '+ 'Valor \n')
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # no hay mas input
    print(tok)
    #escritura en el archivo de salida
    arch_salida.write(str(tok.type)+"  "+ str(tok.value) + '\n')


arch_salida.write('Caracteres Ilegales: \n')

for error in list_error:
    arch_salida.write(error+'\n')

arch_salida.close()
