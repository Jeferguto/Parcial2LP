# Generated from Complex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,51,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,3,2,39,8,2,1,2,3,2,42,
        8,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,0,1,2,6,0,2,4,6,8,10,0,2,1,0,
        2,3,1,0,4,5,49,0,12,1,0,0,0,2,21,1,0,0,0,4,41,1,0,0,0,6,43,1,0,0,
        0,8,45,1,0,0,0,10,48,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,
        0,0,0,15,16,6,1,-1,0,16,17,5,6,0,0,17,18,3,2,1,0,18,19,5,7,0,0,19,
        22,1,0,0,0,20,22,3,4,2,0,21,15,1,0,0,0,21,20,1,0,0,0,22,31,1,0,0,
        0,23,24,10,4,0,0,24,25,5,4,0,0,25,30,3,2,1,5,26,27,10,3,0,0,27,28,
        5,5,0,0,28,30,3,2,1,4,29,23,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,
        31,29,1,0,0,0,31,32,1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,38,3,6,
        3,0,35,36,3,10,5,0,36,37,3,8,4,0,37,39,1,0,0,0,38,35,1,0,0,0,38,
        39,1,0,0,0,39,42,1,0,0,0,40,42,3,8,4,0,41,34,1,0,0,0,41,40,1,0,0,
        0,42,5,1,0,0,0,43,44,7,0,0,0,44,7,1,0,0,0,45,46,3,6,3,0,46,47,5,
        1,0,0,47,9,1,0,0,0,48,49,7,1,0,0,49,11,1,0,0,0,5,21,29,31,38,41
    ]

class ComplexParser ( Parser ):

    grammarFileName = "Complex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'i'", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INT", "FLOAT", "PLUS", 
                      "MINUS", "LPAREN", "RPAREN", "WS" ]

    RULE_expr = 0
    RULE_complexExpr = 1
    RULE_complejo = 2
    RULE_real = 3
    RULE_imaginary = 4
    RULE_signo = 5

    ruleNames =  [ "expr", "complexExpr", "complejo", "real", "imaginary", 
                   "signo" ]

    EOF = Token.EOF
    T__0=1
    INT=2
    FLOAT=3
    PLUS=4
    MINUS=5
    LPAREN=6
    RPAREN=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complexExpr(self):
            return self.getTypedRuleContext(ComplexParser.ComplexExprContext,0)


        def EOF(self):
            return self.getToken(ComplexParser.EOF, 0)

        def getRuleIndex(self):
            return ComplexParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ComplexParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.complexExpr(0)
            self.state = 13
            self.match(ComplexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexParser.RULE_complexExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComplejoSimpleExprContext(ComplexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplexExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complejo(self):
            return self.getTypedRuleContext(ComplexParser.ComplejoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplejoSimpleExpr" ):
                listener.enterComplejoSimpleExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplejoSimpleExpr" ):
                listener.exitComplejoSimpleExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplejoSimpleExpr" ):
                return visitor.visitComplejoSimpleExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisExprContext(ComplexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplexExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ComplexParser.LPAREN, 0)
        def complexExpr(self):
            return self.getTypedRuleContext(ComplexParser.ComplexExprContext,0)

        def RPAREN(self):
            return self.getToken(ComplexParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesisExpr" ):
                listener.enterParentesisExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesisExpr" ):
                listener.exitParentesisExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesisExpr" ):
                return visitor.visitParentesisExpr(self)
            else:
                return visitor.visitChildren(self)


    class SumaExprContext(ComplexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplexExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complexExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexParser.ComplexExprContext)
            else:
                return self.getTypedRuleContext(ComplexParser.ComplexExprContext,i)

        def PLUS(self):
            return self.getToken(ComplexParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaExpr" ):
                listener.enterSumaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaExpr" ):
                listener.exitSumaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaExpr" ):
                return visitor.visitSumaExpr(self)
            else:
                return visitor.visitChildren(self)


    class RestaExprContext(ComplexExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplexExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complexExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ComplexParser.ComplexExprContext)
            else:
                return self.getTypedRuleContext(ComplexParser.ComplexExprContext,i)

        def MINUS(self):
            return self.getToken(ComplexParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestaExpr" ):
                listener.enterRestaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestaExpr" ):
                listener.exitRestaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestaExpr" ):
                return visitor.visitRestaExpr(self)
            else:
                return visitor.visitChildren(self)



    def complexExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplexParser.ComplexExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_complexExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = ComplexParser.ParentesisExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(ComplexParser.LPAREN)
                self.state = 17
                self.complexExpr(0)
                self.state = 18
                self.match(ComplexParser.RPAREN)
                pass
            elif token in [2, 3]:
                localctx = ComplexParser.ComplejoSimpleExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.complejo()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ComplexParser.SumaExprContext(self, ComplexParser.ComplexExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_complexExpr)
                        self.state = 23
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 24
                        self.match(ComplexParser.PLUS)
                        self.state = 25
                        self.complexExpr(5)
                        pass

                    elif la_ == 2:
                        localctx = ComplexParser.RestaExprContext(self, ComplexParser.ComplexExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_complexExpr)
                        self.state = 26
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 27
                        self.match(ComplexParser.MINUS)
                        self.state = 28
                        self.complexExpr(4)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComplejoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplexParser.RULE_complejo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealConImaginarioExprContext(ComplejoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplejoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def real(self):
            return self.getTypedRuleContext(ComplexParser.RealContext,0)

        def signo(self):
            return self.getTypedRuleContext(ComplexParser.SignoContext,0)

        def imaginary(self):
            return self.getTypedRuleContext(ComplexParser.ImaginaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealConImaginarioExpr" ):
                listener.enterRealConImaginarioExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealConImaginarioExpr" ):
                listener.exitRealConImaginarioExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealConImaginarioExpr" ):
                return visitor.visitRealConImaginarioExpr(self)
            else:
                return visitor.visitChildren(self)


    class SoloImaginarioExprContext(ComplejoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplexParser.ComplejoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def imaginary(self):
            return self.getTypedRuleContext(ComplexParser.ImaginaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoloImaginarioExpr" ):
                listener.enterSoloImaginarioExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoloImaginarioExpr" ):
                listener.exitSoloImaginarioExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSoloImaginarioExpr" ):
                return visitor.visitSoloImaginarioExpr(self)
            else:
                return visitor.visitChildren(self)



    def complejo(self):

        localctx = ComplexParser.ComplejoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_complejo)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ComplexParser.RealConImaginarioExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.real()
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.signo()
                    self.state = 36
                    self.imaginary()


                pass

            elif la_ == 2:
                localctx = ComplexParser.SoloImaginarioExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.imaginary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ComplexParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ComplexParser.FLOAT, 0)

        def getRuleIndex(self):
            return ComplexParser.RULE_real

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)




    def real(self):

        localctx = ComplexParser.RealContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_real)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImaginaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def real(self):
            return self.getTypedRuleContext(ComplexParser.RealContext,0)


        def getRuleIndex(self):
            return ComplexParser.RULE_imaginary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImaginary" ):
                listener.enterImaginary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImaginary" ):
                listener.exitImaginary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImaginary" ):
                return visitor.visitImaginary(self)
            else:
                return visitor.visitChildren(self)




    def imaginary(self):

        localctx = ComplexParser.ImaginaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_imaginary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.real()
            self.state = 46
            self.match(ComplexParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ComplexParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ComplexParser.MINUS, 0)

        def getRuleIndex(self):
            return ComplexParser.RULE_signo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigno" ):
                listener.enterSigno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigno" ):
                listener.exitSigno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigno" ):
                return visitor.visitSigno(self)
            else:
                return visitor.visitChildren(self)




    def signo(self):

        localctx = ComplexParser.SignoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_signo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.complexExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def complexExpr_sempred(self, localctx:ComplexExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




