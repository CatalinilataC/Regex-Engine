#!/usr/bin/env python
import sys
import pickle

from antlr4 import *
from GramatikLexer import GramatikLexer
from GramatikListener import GramatikListener
from GramatikParser import GramatikParser


import sys, io
import string
from regex import RegEx
from regular_expression import RegularExpression
from nfa import NFA
from dfa import DFA


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

alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def rename_states(target, reference):
    off = max(reference.states) + 1
    target.start_state += off
    target.states = set(map(lambda s: s + off, target.states))
    target.final_states = set(map(lambda s: s + off, target.final_states))
    new_delta = {}
    for (state, symbol), next_states in target.delta.items():
        new_next_states = set(map(lambda s: s + off, next_states))
        new_delta[(state + off, symbol)] = new_next_states

    target.delta = new_delta


def new_states(*nfas):
    state = 0
    for nfa in nfas:
        m = max(nfa.states)
        if m >= state:
            state = m + 1

    return state, state + 1

def re_to_nfa(re):
    """Convert a Regular Expression to a Nondeterminstic Finite Automaton"""
    # TODO Thompson's algorithm
    alpha = alf
    EMPTY_SET = 0
    EMPTY_STRING = 1
    SYMBOL = 2
    STAR = 3
    CONCATENATION = 4
    ALTERNATION = 5
    if re.type == EMPTY_SET:
      return NFA(alpha, {0, 1}, 0, {1}, {})
    elif re.type == EMPTY_STRING:
      return NFA(alpha, {0, 1}, 0, {1}, {(0, ""): {1}} )
    elif re.type == SYMBOL:
      return NFA(alpha, {0, 1}, 0, {1}, {(0, re.symbol): {1}} )
    elif re.type == ALTERNATION:
      NFAs = re_to_nfa(re.lhs)
      NFAr = re_to_nfa(re.rhs)
      rename_states(NFAs, NFAr)
      start, end = new_states(NFAs, NFAr)
      all_states = {start, end}
      all_states = all_states.union(NFAs.states)
      all_states = all_states.union(NFAr.states)
      all_delta = NFAs.delta
      all_delta.update(NFAr.delta)
      all_delta.update({(start, "") : {NFAs.start_state, NFAr.start_state} } )
      f1 = NFAs.final_states.pop()
      f2 = NFAr.final_states.pop()
      NFAs.final_states.add(f1)
      NFAr.final_states.add(f2)
      all_delta.update({(f1, "") : {end} } )
      all_delta.update({(f2, "") : {end} } )
      return NFA(alpha, all_states, start, {end}, all_delta)
    elif re.type == CONCATENATION:
        NFAs = re_to_nfa(re.lhs)
        NFAr = re_to_nfa(re.rhs)
        rename_states(NFAs, NFAr)
        start, end = new_states(NFAs, NFAr)
        all_states = {start, end}
        all_states = all_states.union(NFAs.states)
        all_states = all_states.union(NFAr.states)
        all_delta = NFAs.delta
        all_delta.update(NFAr.delta)
        f1 = NFAs.final_states.pop()
        NFAs.final_states.add(f1)
        all_delta.update({(start, "") : {NFAs.start_state} } )
        all_delta.update({(f1, "") : {NFAr.start_state} } )
        f2 = NFAr.final_states.pop() 
        NFAr.final_states.add(f2)
        all_delta.update({(f2, "") : {end} } )
        return NFA(alpha, all_states, start, {end}, all_delta)
    elif re.type == STAR:
        NFAs = re_to_nfa(re.lhs)
        start, end = new_states(NFAs)
        all_states = {start, end}
        all_states = all_states.union(NFAs.states)
        all_delta = NFAs.delta
        all_delta.update({(start, ""):{end, NFAs.start_state} })
        f1 = NFAs.final_states.pop()
        NFAs.final_states.add(f1)
        all_delta.update({(f1, "") : {NFAs.start_state, end} } )
        return NFA(alpha, all_states, start, {end}, all_delta)

e_any = None
def re_any():
	alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	e = RegularExpression(2, "a")
	for i in range(1, len(alf)):
		e = RegularExpression(5, e, RegularExpression(2, alf[i]))
	return e



"""
EMPTY_SET = 0
EMPTY_STRING = 1
SYMBOL = 2
STAR = 3
CONCATENATION = 4
ALTERNATION = 5"""
def regex_to_re(reg):
	e = None
	#print(reg.type)
	if reg.type == SYMBOL_SIMPLE:
		return RegularExpression(2, reg.symbol)
	if reg.type == CONCATENATION:
		return RegularExpression(4, regex_to_re(reg.lhs), regex_to_re(reg.rhs))
	if reg.type == ALTERNATION:
		return RegularExpression(5, regex_to_re(reg.lhs), regex_to_re(reg.rhs))
	if reg.type == SYMBOL_ANY:
		return e_any
	if reg.type == STAR:
		return RegularExpression(3, regex_to_re(reg.lhs))
	if reg.type == PLUS:
		return RegularExpression(4, regex_to_re(reg.lhs), 
		RegularExpression(3, regex_to_re(reg.lhs) ) ) # concatenare dintre e si e*
	if reg.type == MAYBE:
		return RegularExpression(5, RegularExpression(1), regex_to_re(reg.lhs) ) # niciuna sau una
	if reg.type == RANGE:
		x,y = reg.range
		aux = regex_to_re(reg.lhs)
		if x == y:
			e = aux
			for i in range(0, x - 1):
				e = RegularExpression(4, e, aux)
		elif x != -1 and y != -1:
			aux2 = aux
			for i in range(x - 1):
				aux2 = RegularExpression(4, aux2, aux)
			e = aux2
			for i in range(y - x):
				aux2 = RegularExpression(4, aux2, aux)
				e = RegularExpression(5, e, aux2)
		elif x == -1:
			aux = regex_to_re(reg.lhs)
			aux2 = aux
			e = RegularExpression(1)
			for i in range(y):
				e = RegularExpression(5, e, aux2)
				aux2 = RegularExpression(4, aux2, aux)
		else:
			aux = regex_to_re(reg.lhs)
			aux2 = aux
			for i in range(x - 1):
				aux2 = RegularExpression(4, aux2, aux)
			e = RegularExpression(4, aux2, RegularExpression(3, aux))
	if reg.type == SYMBOL_SET:
		for i in reg.symbol_set:
			if e == None:
				if isinstance(i, str):
					e = RegularExpression(2, i)
				elif isinstance(i, tuple):
					e = RegularExpression(2, i[0])
					for j in range((ord(i[0]) + 1), (ord(i[1]) + 1)  ):
						e = RegularExpression(5, e, RegularExpression(2, str(chr(j)) )  )
			else:
				if isinstance(i, str):
					e = RegularExpression(5, e , RegularExpression(2, i))
				elif isinstance(i, tuple):
					for j in range((ord(i[0]) ), (ord(i[1]) + 1)  ):
						e = RegularExpression(5, e, RegularExpression(2, str(chr(j)) )  )
					


	return e

def eps_closure(state, NFA):
	rez = set()
	if (state, '') in NFA.delta:
		rez = rez.union(NFA.delta[(state, '')])
	iterated_states = dict.fromkeys(NFA.states, 0)
	ok = True
	while ok:
		ok = False
		for i in rez:
			if iterated_states[i] == 0:
				ok = True
				iterated_states[i] = 1
				if (i, '') in NFA.delta :
					rez = rez.union(NFA.delta[(i, '')])
	return rez

def symb_closure(state, NFA, sym):
	rez = set()
	#rez.add(state)
	#rez = rez.union(eps_closure(state, NFA))
	if (state, sym) in NFA.delta:
		rez = rez.union(NFA.delta[(state, sym)])
	iterated_states = dict.fromkeys(NFA.states, 0)
	ok = True
	while ok:
		ok = False
		for i in rez:
			if iterated_states[i] == 0:
				ok = True
				rez = rez.union(eps_closure(i, NFA))
				iterated_states[i] = 1
	return rez
#idee: din prima stare a nfa ului obtin eps_closure pt ea si va reprezenta prima stare din dfa
#pastrez dictionar in care am ca key {stare1, .. stareN} iar valoarea va fi starea din dfa
#
def nfa_to_dfa(NFA):
	nrstare = 1
	dic = {}
	transitions = {}
	q0 = eps_closure(NFA.start_state, NFA)
	l = (list(q0))
	l.append(NFA.start_state)
	l.sort()
	queue = []
	act_state = tuple(l)
	queue.append(act_state)
	dic[act_state] = nrstare
	nrstare += 1
	while len(queue) > 0: # calculates states and transitions of dfa
		act_state = queue.pop(0)
		for i in alf:
			multimi = set()
			for j in act_state:
				aux = symb_closure(j, NFA, i)
				multimi = multimi.union(aux)

			if len(multimi) > 0:
				aux = list(multimi)
				aux.sort()
				aux = tuple(aux)
				if not aux in dic:
					queue.append(aux)
					dic[aux] = nrstare
					nrstare += 1
				transitions[( dic[act_state], i ) ] = dic[aux]
			else:
				transitions[(dic[act_state], i) ] = 0 #sink state is 0

	#calc final states of dfa
	finale = set()
	toate = {0}
	for i in dic:
		ok = False
		toate.add(dic[i])
		for j in i:
			if j in NFA.final_states:
				ok = True

		if ok == True:
			finale.add(dic[i])
	return DFA(alf, toate, 1, finale, transitions)



def simulate_dfa(dfa, word):
	q = dfa.start_state
	ok = False
	for i in word:
		if i not in alf:
			continue
		if (q, i) in dfa.delta:
			q = dfa.delta[(q, i)]
		else:
			ok = True
			break
	if ok == False and (q in dfa.final_states):
		print("True")
	else: print("False")




if __name__ == "__main__":
    e_any = re_any()
    valid = (len(sys.argv) == 4 and sys.argv[1] in ["RAW", "TDA"]) or \
            (len(sys.argv) == 3 and sys.argv[1] == "PARSE")
    if not valid:
        sys.stderr.write(
            "Usage:\n"
            "\tpython3 main.py RAW <regex-str> <words-file>\n"
            "\tOR\n"
            "\tpython3 main.py TDA <tda-file> <words-file>\n"
            "\tOR\n"
            "\tpython3 main.py PARSE <regex-str>\n"
        )
        sys.exit(1)
    f = open("text.txt","w+")
    if sys.argv[1] == "TDA":
        tda_file = sys.argv[2]
        with open(tda_file, "rb") as fin:
            parsed_regex = pickle.loads(fin.read())
    else:
        regex_string = sys.argv[2]
        f.write(regex_string);
        f.write("\n")
        f.close()
        # TODO "regex_string" conține primul argument din linia de comandă,
        # șirul care reprezintă regexul cerut. Apelați funcția de parsare pe el
        # pentru a obține un obiect RegEx pe care să-l stocați în
        # "parsed_regex"
        #
        # Dacă nu doriți să implementați parsarea, puteți ignora această parte.

        
        parsed_regex = None
        stream = FileStream("text.txt")
        lexer = GramatikLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = GramatikParser(stream)
        tree = parser.start()
        printer = GramatikListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        parsed_regex = printer.e1


        if sys.argv[1] == "PARSE": 
            print(str(parsed_regex))
            sys.exit(0)


    # În acest punct, fie că a fost parsat, fie citit direct ca obiect, aveți
    # la dispoziție variabila "parsed_regex" care conține un obiect de tip
    # RegEx. Aduceți-l la forma de Automat Finit Determinist, pe care să puteți
    # rula în continuare.
    ex = regex_to_re(parsed_regex)
    nfa = re_to_nfa(ex)
    #nfa.to_graphviz()
    dfa = nfa_to_dfa(nfa)
    #dfa.to_graphviz()

    with open(sys.argv[3], "r") as fin:
        content = fin.readlines()

    for word in content:
        # TODO la fiecare iterație, "word" conținue un singur cuvânt din
        # fișierul de input; verificați apartenența acestuia la limbajul
        # regexului dat și scrieți rezultatul la stdout.
        
        simulate_dfa(dfa, word)
        pass

