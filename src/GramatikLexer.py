# Generated from Gramatik.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("S\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6")
        buf.write("\17A\n\17\r\17\16\17B\3\20\6\20F\n\20\r\20\16\20G\3\21")
        buf.write("\5\21K\n\21\3\22\6\22N\n\22\r\22\16\22O\3\22\3\22\2\2")
        buf.write("\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2\62;\4\2C\\")
        buf.write("c|\5\2\13\f\17\17\"\"\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2")
        buf.write("\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63")
        buf.write("\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\279\3\2\2\2\31;\3")
        buf.write("\2\2\2\33=\3\2\2\2\35@\3\2\2\2\37E\3\2\2\2!J\3\2\2\2#")
        buf.write("M\3\2\2\2%&\7*\2\2&\4\3\2\2\2\'(\7+\2\2(\6\3\2\2\2)*\7")
        buf.write("]\2\2*\b\3\2\2\2+,\7_\2\2,\n\3\2\2\2-.\7,\2\2.\f\3\2\2")
        buf.write("\2/\60\7-\2\2\60\16\3\2\2\2\61\62\7A\2\2\62\20\3\2\2\2")
        buf.write("\63\64\7}\2\2\64\22\3\2\2\2\65\66\7\177\2\2\66\24\3\2")
        buf.write("\2\2\678\7/\2\28\26\3\2\2\29:\7.\2\2:\30\3\2\2\2;<\7~")
        buf.write("\2\2<\32\3\2\2\2=>\7\60\2\2>\34\3\2\2\2?A\t\2\2\2@?\3")
        buf.write("\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\36\3\2\2\2DF\t\2")
        buf.write("\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H \3\2\2\2")
        buf.write("IK\t\3\2\2JI\3\2\2\2K\"\3\2\2\2LN\t\4\2\2ML\3\2\2\2NO")
        buf.write("\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2QR\b\22\2\2R$\3")
        buf.write("\2\2\2\7\2BGJO\3\b\2\2")
        return buf.getvalue()


class GramatikLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PARD = 1
    PARI = 2
    PARPD = 3
    PARPI = 4
    AST = 5
    PLS = 6
    INTR = 7
    ACD = 8
    ACI = 9
    MINUS = 10
    VIRG = 11
    OR = 12
    ANYTHING = 13
    NUMBER = 14
    NUMBERZ = 15
    SYMBOL = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'*'", "'+'", "'?'", "'{'", "'}'", 
            "'-'", "','", "'|'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "PARD", "PARI", "PARPD", "PARPI", "AST", "PLS", "INTR", "ACD", 
            "ACI", "MINUS", "VIRG", "OR", "ANYTHING", "NUMBER", "NUMBERZ", 
            "SYMBOL", "WS" ]

    ruleNames = [ "PARD", "PARI", "PARPD", "PARPI", "AST", "PLS", "INTR", 
                  "ACD", "ACI", "MINUS", "VIRG", "OR", "ANYTHING", "NUMBER", 
                  "NUMBERZ", "SYMBOL", "WS" ]

    grammarFileName = "Gramatik.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


