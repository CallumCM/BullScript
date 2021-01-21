import Compiler
class Function:
	def __init__(self, args, code):
		self.args = args
		self.code = code

	def invoke(self, args):
		code = self.code
		for i in args:
			code.insert(0, self.args[i] + "=" + args[i])
		Compiler.Compiler.compile(code)