
from purplex import Parser, attach
from purplex import LEFT, RIGHT

from rearc.lexer import GCodeLexer


class GCodeParser(Parser):

    LEXER = GCodeLexer
    START = 'e'

    PRECEDENCE = (
        # (RIGHT, 'UMINUS'),
        # (LEFT, 'TIMES', 'DIVIDE'),
        # (LEFT, 'PLUS', 'MINUS'),
    )

    @attach('e : GCODE axes')
    def expression(self, gcode, axes):
        print("gexpression: {}|{}".format(gcode, axes))

    @attach('gcode : GCODE')
    def gcode(self, gcode):
        return gcode

    @attach('axes : axis | axes')
    def axes(self, axis):
        return axis

    @attach('axis : AXIS')
    def axis(self, axis):
        return axis


    # @attach('e : LPAREN e RPAREN')
    # def brackets(self, lparen, expr, rparen):
    #     return expr
    #
    # @attach('e : e PLUS e')
    # def addition(self, left, op, right):
    #     return left + right
    #
    # @attach('e : e MINUS e')
    # def subtract(self, left, op, right):
    #     return left - right
    #
    # @attach('e : e TIMES e')
    # def multiply(self, left, op, right):
    #     return left * right
    #
    # @attach('e : e DIVIDE e')
    # def division(self, left, op, right):
    #     return left / right
    #
    # @attach('e : MINUS e', prec_symbol='UMINUS')
    # def negate(self, minus, expr):
    #     return -expr
    #
    # @attach('e : INTEGER')
    # def number(self, num):
    #     return int(num)

"""
$ python example.py
2 + 3 * 4 - 4 = 10 ; True
-4 = -4 ; True
-4 * 2 = -8 ; True
-2 * - (1 + 1) = 4 ; True
6 / 2 * 4 - 8 * 1 = 4.0 ; True"""
