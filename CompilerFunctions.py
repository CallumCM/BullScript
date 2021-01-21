import Function
import Dicts
import Error
import Token
import Compiler

class CompilerFunctions:

	def comment(tokens, token):
		reEval = False
		del tokens[slice(token, -1)]
		return [tokens, token, reEval]

	def arith(tokens, token):
		reEval = False
		if (tokens[token-1].type == "INT" or tokens[token-1].type == "FLOAT") and (tokens[token+1].type == "INT" or tokens[token+1].type == "FLOAT"):
			a = tokens[token - 1].value
			b = tokens[token + 1].value
			typ = "INT"
			if tokens[token-1].type=="FLOAT"or tokens[token+1].type=="FLOAT": typ = "FLOAT"
			tokens[token].type = typ
			op = tokens[token].value
			if op == "+":
				tokens[token].value = a + b
			elif op == "-":
				tokens[token].value = a - b
			elif op == "*":
				tokens[token].value = a * b
			elif op == "/" and tokens[token + 1].type != "":
				tokens[token].value = a / b
			elif op == "^":
				tokens[token].value = a ** b
			elif op == "%" or op == "mod":
				tokens[token].value = a % b
			del tokens[token-1]
			del tokens[token]
			token -= 1
		elif tokens[token-1].type == "LITSTR" and tokens[token+1].type == "LITSTR":
			a = tokens[token - 1].value
			b = tokens[token + 1].value
			tokens[token].type = "LITSTR"
			tokens[token].value = a + b
			del tokens[token-1]
			del tokens[token]
			token -= 1
		else:
			reEval = True
		return [tokens, token, reEval]

	def lpar(tokens, token):
		reEval = False
		if(tokens[token-1].type == "ITEM"): return [tokens, token, reEval]
		if tokens[token+1].type in Dicts.classes and tokens[token+2].type == "RPAR":
			del tokens[token]
			del tokens[token+1]
			token -= 1
		else:
			reEval = True
		return [tokens, token, reEval]

	def rfunction(tokens, token):
		reEval = False
		name = ""
		args = []
		code = []
		if tokens[token+1].type == "STR":
			if tokens[token].value == "def":
				tokens[token].value = "NONE"
				name = tokens[token+1].value
				del tokens[token+1]
			if tokens[token+1].type == "LPAR":
				del tokens[token+1]
				i = token+1
				while i < len(tokens):
					if tokens[i].type == "STR":
						args.append(tokens[i].value)
						del tokens[i]
						i -= 1
					elif tokens[i].type == "RPAR": del tokens[i]; break
					i += 1
				if tokens[token+1].type == "LBRACE":
					del tokens[token+1]
					i = token+1
					j = i
					while i < len(tokens):
						if tokens[i].type == "NEWLINE":
							code.append(tokens[slice(j,i)])
							del tokens[slice(j,i)]
							i = j
						elif tokens[i].type == "RBRACE":
							code.append(tokens[slice(j,i-1)])
							del tokens[slice(j,i+1)]
							break
						i += 1
					Dicts.func[name]=(Function.Function(args,code))
					del tokens[token]
					token -= 1
		else: reEval = True
		return [tokens, token, reEval]

	def equals(tokens, token):
		reEval = False
		if tokens[token-1].type == "STR" and tokens[token+1].type in Dicts.classes and (len(tokens)==token+2 or tokens[token+2].type == "NEWLINE"):
			Dicts.var[tokens[token-1].value]=tokens[token+1]
			del tokens[slice(token-1,token+2)]
			token -= 1
		else: reEval = True
		return [tokens, token, reEval]

	def out(tokens, token):
		reEval = False
		if tokens[token+1].type in Dicts.classes:
			output = str(tokens[token+1].value)
			output.replace('§9', '\033[94m')
			print(output)
			del tokens[slice(token,token+2)]
		else: reEval = True
		return [tokens, token, reEval]

	def str(tokens, token):
		reEval = False
		args = []
		var = Dicts.var.get(tokens[token].value, None)
		if  tokens[token+1].type == "LPAR":
			del tokens[token+1]
			i = token+1
			while i < len(tokens):
				if tokens[i].type == "STR":
					args.append(tokens[i].value)
					del tokens[i]
					i -= 1
				elif tokens[i].type == "RPAR": del tokens[i]; break
				i += 1
			func = Dicts.func.get(tokens[token].value, None)
			if func == None: tokens.append(Token.Token("ERR", Error.UndefinedFunctionError(tokens[token].value)))
			
		elif tokens[token + 1].type == "EQUALS":
			return [tokens, token, reEval]
		elif var != None:
			tokens[token] = var
		else: tokens.append(Token.Token("ERR", Error.UndefinedVariableError(tokens[token].value))); 
		return [tokens, token, reEval]