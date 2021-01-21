import Compiler
import re
compiler = Compiler.Compiler()
LoadMethod = input("LoadFromSource> ")
if re.search("^[tTsS]", LoadMethod):
	while True:
		text = input("BS> ")
		if text == "stop": break
		result = compiler.compile(text)
		if result[1]:
			print(result[0][-1].value.as_string())
elif re.search("^[eEfF]", LoadMethod):
	with open("./main.bs") as f:
		text = f.read()
	result = compiler.compile(text)
	if result[1]:
		print(result[0][-1].value.as_string())