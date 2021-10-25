from sly import Lexer

class MiLexer(Lexer):
	tokens = {
		ID, NUM, PIZQ, PDER,
		MAS, POR, IGUAL,
		PRINT, CHAU,
		PC,
	}

	ignore 			= ' \t\n'

	ID 				= r'[_a-zA-Z][_0-9a-zA-Z]*'
	ID['print'] 	= PRINT
	ID['chau']		= CHAU
	NUM 			= r'[1-9][0-9]*'

	PIZQ			= r'\('
	PDER			= r'\)'
	MAS 			= r'\+'
	POR 			= r'\*'
	IGUAL 			= r'='
	PC 				= r';'


if __name__ == '__main__':
	data = '''
		x = 3 + 42;
		a = (3+  x)*2;
		hola     = x*a;
		print hola;
		chau;
	'''
	lexer = MiLexer()
	for tok in lexer.tokenize(data):
		print(f'<{tok.type}:{tok.value}>',end=' ')
	print('')
