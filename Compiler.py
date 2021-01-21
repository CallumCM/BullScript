import Alexer
import Error
import Token
import CompilerFunctions as funcs
import Dicts

class Compiler:
	current_line = 0
	def strip_ignored(tokens):
		token = 0
		while token < len(tokens):
			if tokens[token].type == 'IGNORED':
				del tokens[token]
				token -= 1
			token += 1
		return tokens

	def evaluate_expressions(tokens):
		token = 0
		reEval = False
		while token < len(tokens):
			v = [tokens, token, reEval]
			if tokens[token].type == "COMMENT": v=funcs.CompilerFunctions.comment(tokens, token)
			elif tokens[token].type == "ARITH": v=funcs.CompilerFunctions.arith(tokens,token)
			elif tokens[token].type == "LPAR": v=funcs.CompilerFunctions.lpar(tokens,token)
			elif tokens[token].type == "RFUNCTION": v=funcs.CompilerFunctions.rfunction(tokens, token)
			elif tokens[token].type == "EQUALS": v=funcs.CompilerFunctions.equals(tokens, token)
			elif tokens[token].type == "OUT": v=funcs.CompilerFunctions.out(tokens, token)
			elif tokens[token].type == "STR": v=funcs.CompilerFunctions.str(tokens, token)
			elif tokens[token].type=="NEWLINE"and(reEval or v[2]):break
			tokens = v[0]; token = v[1]; reEval = reEval or v[2]
			token += 1
		return [tokens, reEval]

	def errorCatcher(tokens):
		token = 0
		isErr = False
		
		while tokens[token] != None:
			if tokens[token][1] != None:
				isErr = True
			token += 1
		return isErr

	def compile(self, code):
		err = False
		alexer = []
		if isinstance(code, str):
			alexer = Alexer.evalBS(code)
		elif isinstance(code, array):
			alexer = code
		if alexer[1]: return [alexer[0], True]
		tokens = alexer[0]
		tokens = Compiler.strip_ignored(tokens)
		reEval = True
		iters = 0
		while reEval:
			if iters > 50: tokens.append(Token.Token("ERR",Error.StackOverflowError(tokens))); return [tokens, True]
			a = Compiler.evaluate_expressions(tokens)
			tokens = a[0]
			reEval = a[1]
			iters += 1
		compiled_code = tokens
		if tokens[-1].type == "ERR": err = True
		return [compiled_code, err]