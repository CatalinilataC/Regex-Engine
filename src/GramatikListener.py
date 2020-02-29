
# Generated from Gramatik.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramatikParser import GramatikParser
else:
    from GramatikParser import GramatikParser

from regex import RegEx


EMPTY_STRING = 0
SYMBOL_SIMPLE = 1
SYMBOL_ANY = 2
SYMBOL_SET = 3
MAYBE = 4
STAR = 5
PLUS = 6
RANGE = 7
CONCATENATION = 8
ALTERNATION = 9


# This class defines a complete listener for a parse tree produced by GramatikParser.
class GramatikListener(ParseTreeListener):

    def __init__(self):
        self.e1 = None
        self.e2 = None
        self.stack = []
        self.n1 = -1
        self.n2 = -1
        self.setin = set()
        self.nrpar = 0
        self.parstack = []
    # Enter a parse tree produced by GramatikParser#startRule.
    def enterStartRule(self, ctx:GramatikParser.StartRuleContext):
        pass

    # Exit a parse tree produced by GramatikParser#startRule.
    def exitStartRule(self, ctx:GramatikParser.StartRuleContext):
        self.e1 = self.stack.pop(0)


    # Enter a parse tree produced by GramatikParser#numar.
    def enterNumar(self, ctx:GramatikParser.NumarContext):
        self.stack.append(RegEx(SYMBOL_SIMPLE, str(ctx.NUMBER())))

    # Exit a parse tree produced by GramatikParser#numar.
    def exitNumar(self, ctx:GramatikParser.NumarContext):
        pass


    # Enter a parse tree produced by GramatikParser#sau.
    def enterSau(self, ctx:GramatikParser.SauContext):
        pass

    # Exit a parse tree produced by GramatikParser#sau.
    def exitSau(self, ctx:GramatikParser.SauContext):
        e1 = self.stack.pop()
        e2 = self.stack.pop()
        e = RegEx(ALTERNATION, e2, e1)
        self.stack.append(e)

    # Enter a parse tree produced by GramatikParser#concat.
    def enterConcat(self, ctx:GramatikParser.ConcatContext):
        pass

    # Exit a parse tree produced by GramatikParser#concat.
    def exitConcat(self, ctx:GramatikParser.ConcatContext):
        if len(self.stack) > 1:
            e1 = self.stack.pop()
            e2 = self.stack.pop()
            e = RegEx(CONCATENATION, e2, e1)
            self.stack.append(e)


    # Enter a parse tree produced by GramatikParser#simbol.
    def enterSimbol(self, ctx:GramatikParser.SimbolContext):
        self.stack.append(RegEx(SYMBOL_SIMPLE, str(ctx.SYMBOL())))

    # Exit a parse tree produced by GramatikParser#simbol.
    def exitSimbol(self, ctx:GramatikParser.SimbolContext):
        pass


    # Enter a parse tree produced by GramatikParser#anything.
    def enterAnything(self, ctx:GramatikParser.AnythingContext):
        self.stack.append(RegEx(SYMBOL_ANY))

    # Exit a parse tree produced by GramatikParser#anything.
    def exitAnything(self, ctx:GramatikParser.AnythingContext):
        pass
    # Enter a parse tree produced by GramatikParser#range.
    def enterRange(self, ctx:GramatikParser.RangeContext):
        self.stack.append(RegEx(SYMBOL_SIMPLE, str(ctx.SYMBOL())))

    # Exit a parse tree produced by GramatikParser#range.
    def exitRange(self, ctx:GramatikParser.RangeContext):
        pass
        # Enter a parse tree produced by GramatikParser#plus.
    def enterPlus(self, ctx:GramatikParser.PlusContext):
        pass

    # Exit a parse tree produced by GramatikParser#plus.
    def exitPlus(self, ctx:GramatikParser.PlusContext):
        aux = RegEx(SYMBOL_SIMPLE, str(ctx.SYMBOL()))
        self.stack.append(RegEx(PLUS, aux))
        # Enter a parse tree produced by GramatikParser#star.
    def enterStar(self, ctx:GramatikParser.StarContext):
        pass

    # Exit a parse tree produced by GramatikParser#star.
    def exitStar(self, ctx:GramatikParser.StarContext):
        aux = RegEx(SYMBOL_SIMPLE, str(ctx.SYMBOL()))
        self.stack.append(RegEx(STAR, aux))


    # Enter a parse tree produced by GramatikParser#maybe.
    def enterMaybe(self, ctx:GramatikParser.MaybeContext):
        pass

    # Exit a parse tree produced by GramatikParser#maybe.
    def exitMaybe(self, ctx:GramatikParser.MaybeContext):
        aux = RegEx(SYMBOL_SIMPLE, str(ctx.SYMBOL()))
        self.stack.append(RegEx(MAYBE, aux))

      # Enter a parse tree produced by GramatikParser#acco.
    def enterAcco(self, ctx:GramatikParser.AccoContext):
        pass

    # Exit a parse tree produced by GramatikParser#acco.
    def exitAcco(self, ctx:GramatikParser.AccoContext):
        e = self.stack.pop()
        self.stack.append(RegEx(RANGE, e, (self.n1, self.n2) ))


    # Enter a parse tree produced by GramatikParser#caz1.
    def enterCaz1(self, ctx:GramatikParser.Caz1Context):
        self.n2 = int(str(ctx.NUMBER()))
        #print("caz1")

    # Exit a parse tree produced by GramatikParser#caz1.
    def exitCaz1(self, ctx:GramatikParser.Caz1Context):
        pass


    # Enter a parse tree produced by GramatikParser#caz2.
    def enterCaz2(self, ctx:GramatikParser.Caz2Context):
        self.n1 = int(str(ctx.NUMBER()))

    # Exit a parse tree produced by GramatikParser#caz2.
    def exitCaz2(self, ctx:GramatikParser.Caz2Context):
        pass


    # Enter a parse tree produced by GramatikParser#caz3.
    def enterCaz3(self, ctx:GramatikParser.Caz3Context):
        self.n1 = int(str(ctx.NUMBER(0)))
        self.n2 = int(str(ctx.NUMBER(1)))

    # Exit a parse tree produced by GramatikParser#caz3.
    def exitCaz3(self, ctx:GramatikParser.Caz3Context):
        pass


    # Enter a parse tree produced by GramatikParser#caz4.
    def enterCaz4(self, ctx:GramatikParser.Caz4Context):
        self.n2 = int(str(ctx.NUMBER()))
        self.n1 = self.n2

    # Exit a parse tree produced by GramatikParser#caz4.
    def exitCaz4(self, ctx:GramatikParser.Caz4Context):
        pass
    # Enter a parse tree produced by GramatikParser#interv.
    def enterInterv(self, ctx:GramatikParser.IntervContext):
        pass
        

    # Exit a parse tree produced by GramatikParser#interv.
    def exitInterv(self, ctx:GramatikParser.IntervContext):
        #print("exitInterv")
        self.stack.append(RegEx(SYMBOL_SET, self.setin))

    # Enter a parse tree produced by GramatikParser#interval.
    def enterInterval(self, ctx:GramatikParser.IntervalContext):
        if ctx.MINUS() != None:
            if ctx.SYMBOL(0) != None:
                self.setin.add((str(ctx.SYMBOL(0)) , str(ctx.SYMBOL(1))))
            else:
                self.setin.add( (str(ctx.NUMBER(0)), str(ctx.NUMBER(1)))) 
        else:
            if ctx.SYMBOL() != None:
                self.setin.add(str(ctx.SYMBOL(0)))
            else:
                self.setin.add(str(ctx.NUMBER(0)))

    # Exit a parse tree produced by GramatikParser#interval.
    def exitInterval(self, ctx:GramatikParser.IntervalContext):
        pass

        # Enter a parse tree produced by GramatikParser#paranteze.
    def enterParanteze(self, ctx:GramatikParser.ParantezeContext):
        self.nrpar += 1

    # Exit a parse tree produced by GramatikParser#paranteze.
    def exitParanteze(self, ctx:GramatikParser.ParantezeContext):
        pass
        # Enter a parse tree produced by GramatikParser#parantMaybe.
    def enterParantMaybe(self, ctx:GramatikParser.ParantMaybeContext):
        pass

    # Exit a parse tree produced by GramatikParser#parantMaybe.
    def exitParantMaybe(self, ctx:GramatikParser.ParantMaybeContext):
        aux = self.stack.pop()
        self.stack.append(RegEx(MAYBE, aux))

       # Enter a parse tree produced by GramatikParser#parantAst.
    def enterParantAst(self, ctx:GramatikParser.ParantAstContext):
        pass

    # Exit a parse tree produced by GramatikParser#parantAst.
    def exitParantAst(self, ctx:GramatikParser.ParantAstContext):
        aux = self.stack.pop()
        self.stack.append(RegEx(STAR, aux))

            # Enter a parse tree produced by GramatikParser#parantPls.
    def enterParantPls(self, ctx:GramatikParser.ParantPlsContext):
        pass

    # Exit a parse tree produced by GramatikParser#parantPls.
    def exitParantPls(self, ctx:GramatikParser.ParantPlsContext):
        aux = self.stack.pop()
        self.stack.append(RegEx(PLUS, aux))

        # Enter a parse tree produced by GramatikParser#intervAdvanced.
    def enterIntervAdvanced(self, ctx:GramatikParser.IntervAdvancedContext):
        pass

    # Exit a parse tree produced by GramatikParser#intervAdvanced.
    def exitIntervAdvanced(self, ctx:GramatikParser.IntervAdvancedContext):
        self.stack.append(RegEx(SYMBOL_SET, self.setin))
        aux = self.stack.pop()
        self.stack.append(RegEx(STAR, aux))



