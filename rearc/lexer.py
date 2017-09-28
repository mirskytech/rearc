from purplex import Lexer, TokenDef


class GCodeLexer(Lexer):

    GCODE = TokenDef(r'[GM][0-9]{1,3}')

    INTEGER = TokenDef(r'\d+')

    LPAREN = TokenDef(r'\(')
    RPAREN = TokenDef(r'\)')

    TIMES = TokenDef(r'\*')
    DIVIDE = TokenDef(r'/')
    PLUS = TokenDef(r'\+')
    MINUS = TokenDef(r'-')

    WHITESPACE = TokenDef(r'[\s\n]+', ignore=True)
