# Gramatica del lenguaje simple c-trucho

```ebnf
raiz		:=	sentencias

sentencias	:=	sentencia
			|	sentencia sentencias

sentencia 	:=	ID IGUAL expr PC
			|	PRINT expr PC
			|	CHAU

expr		:=	expr POR expr
			|	expr MAS expr
			|	ID
			|	NUM
			|	PIZQ expr PDER
```

---

```python
precedence = (
	('left', MAS),
	('left', POR),
)
```