import Token
import Error
import Dicts

DIGITS = '0123456789'
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
XCHARS = '\\ \".,/?\';:[]{}()#`~!@#$%^&*_+-=§'

class Alexer:
	def __init__(self, text):
		self.text = text
		self.pos = -1
		self.current_char = None
		self.advance()
		self.error = None

	def advance(self):
		self.pos += 1
		self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

	def make_tokens(self):
		val = None
		#while self.current_char != None:
		if self.current_char != None:
			if Dicts.type.get(self.current_char, None) != None:
				val = Token.Token(Dicts.type.get(self.current_char, None), self.current_char)
			else:
				self.error = Error.IllegalCharException(self.current_char)
				val = "err"
		self.advance()
		return val
	def make_number(self):
		num_str = ''
		dot_count = 0
		while self.current_char != None and self.current_char in DIGITS + '.':
		  if self.current_char == '.':
		    if dot_count == 1: break
		    dot_count += 1
		    num_str += '.'
		  else:
		    num_str += self.current_char
		  self.advance()
		if dot_count == 0:
		  return Token.Token("INT", int(num_str))
		else:
		  return Token.Token("FLOAT", float(num_str))

	def make_string(self):
		string = ''
		while self.current_char != None and self.current_char in CHARS:
			string += self.current_char
			self.advance()
		type = Dicts.type.get(string, "STR")
		return Token.Token(type, string)

	def make_literal_string(self):
		string = ''
		self.advance()
		while self.current_char != None and self.current_char in CHARS + DIGITS + XCHARS:
			if self.current_char == '\"' and string[-1] != "\\": break
			string += self.current_char
			self.advance()
		self.advance()
		return Token.Token("LITSTR", string)

def evalBS(text):
	alexer = Alexer(text)
	tokens = []
	error = False
	while alexer.current_char != None:
		if alexer.current_char in DIGITS:
			tokens.append(alexer.make_number())
		elif alexer.current_char in CHARS:
			tokens.append(alexer.make_string())
		elif alexer.current_char == "\"":
			tokens.append(alexer.make_literal_string())
		else:
			tokens.append(alexer.make_tokens())
		if tokens[-1] == "err":
			error = True
			tokens[-1] = Token.Token("ERR", alexer.error)
			break
	if tokens[-1].type != "ERR": tokens.append(Token.Token("NEWLINE","\n"))
	return [tokens, error]