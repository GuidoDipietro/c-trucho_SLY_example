# Simple language interpreter using SLY Lex Yacc
# https://sly.readthedocs.io/en/latest/sly.html
#################################################

from lexer import MiLexer
from sly import Parser

class MiParser(Parser):
	# debugfile = 'parser.out'

	tokens = MiLexer.tokens

	precedence = (
		('left', MAS),
		('left', POR),
	)

	def __init__(self):
		self.ids = {}

	##########
	# Raiz y recursividad

	@_(	'sentencias')
	def raiz(self, p):
		...

	@_('sentencia', 'sentencia sentencias')
	def sentencias(self, p):
		...


	##########
	# Expresiones

	@_('expr POR expr')
	def expr(self, p):
		return p.expr0 * p.expr1

	@_('expr MAS expr')
	def expr(self, p):
		return p.expr0 + p.expr1

	@_('ID')
	def expr(self, p):
		return self.ids[p.ID]

	@_('NUM')
	def expr(self, p):
		return float(p.NUM)

	@_('PIZQ expr PDER')
	def expr(self, p):
		return p.expr

	##########

	@_('ID IGUAL expr PC')
	def sentencia(self, p):
		self.ids[p.ID] = p.expr

	@_('PRINT expr PC')
	def sentencia(self, p):
		print(p.expr)

	@_('CHAU')
	def sentencia(self, p):
		print("Nos vemos!")
		exit(0)

##############################

if __name__ == "__main__":
	lexer = MiLexer()
	parser = MiParser()

	while True:
		try:
			text = input('c-trucho> ')
			result = parser.parse(lexer.tokenize(text))
		except EOFError:
			break
