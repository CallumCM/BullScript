type = {
  "+": "ARITH",
	"-": "ARITH",
	"*": "ARITH",
	"/": "ARITH",
	"^": "ARITH",
	"%": "ARITH",
	"mod": "ARITH",
  "(": "LPAR",
	")": "RPAR",
	"{": "LBRACE",
	"}": "RBRACE",
	"=": "EQUALS",
	";": "NEWLINE",
	"\n": "NEWLINE",
	" ": "IGNORED",
	"	": "IGNORED",
	"def": "RFUNCTION",
	"function": "RFUNCTION",
	"out": "OUT",
	"print": "OUT",
	"#": "COMMENT",
	"//": "COMMENT",
	"COMMENT:": "COMMENT"
}
var = {}
func = {}
classes = ["INT","LITSTR","FLOAT"]