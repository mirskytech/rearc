from purplex import Lexer, TokenDef


class GCodeLexer(Lexer):

    GCODE = TokenDef(r'[GM]\d+')

    AXIS = TokenDef(r'X\d+')

    INTEGER = TokenDef(r'\d+')

    LPAREN = TokenDef(r'\(')
    RPAREN = TokenDef(r'\)')

    TIMES = TokenDef(r'\*')
    DIVIDE = TokenDef(r'/')
    PLUS = TokenDef(r'\+')
    MINUS = TokenDef(r'-')

    WHITESPACE = TokenDef(r'[\s\n]+', ignore=True)
