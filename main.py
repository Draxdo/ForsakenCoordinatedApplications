# version stuff
major = '1'
minor = '4'
patch = '2'

version = major + '.' + minor + '.' + 'patch'







# imports

import os
import sys











# globals

currentFunc = None
funcs = {
}
builtInFuncs = [
	'add',
	'sub',
	'output',
	'flush',
	'newline',
	'write',
	'stdin',
	'to_int',
	'to_str',
	'argv',
	'div',
	'mul',
	'restore_ptr',
	'add_to'
]
structs = {
}
comparators = [
	'==',
	'<=',
	'=<',
	'>=',
	'=>',
	'!='
]
constants = {

}

lineno = 0
inScruct = False
ints = ['pointer']
strs = []
mainDef = False
currentFuncReturnType = None
inif = 0
currentStruct = None











# code

def worksAsDub(s):
	try:
		x = float(s)
		return True
	except:
		return False
	return False


def worksAsInt(s):
	try:
		x = int(s)
		return True
	except:
		return False
	return False

def furtherAnalysis(l):
	global currentFunc, currentFuncReturnType, funcs, inif, structs, lineno
	if l[0] == '}':
		if inif > 0:
			inif -= 1
		elif currentFunc != None:
			currentFunc = None
			currentFuncReturnType = None
		else:
			quit("SyntaxWarning: No scope to end with '}'! Lineno: " + str(lineno))
	elif l[0] == 'call' and currentFunc != None:
		if l[1] in builtInFuncs or l[1] in funcs:
			funcs[currentFunc].append(('\t'*inif) +l[1] + '()')
		elif l[1] == '@':
			funcs[currentFunc].append(('\t'*inif) +'foo = pop()\n\tfoo()')
		else:
			quit("NameError: Function {" + l[1] + "} is undefined!")
	elif l[0] == 'return':
		if currentFuncReturnType == 'int' and currentFunc != None:
			if l[1] in ints or worksAsInt(l[1]):
				funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\treturn None")
			else:
				quit("TypeError: Function {" + currentFunc + "} supposed to return an integer!")
		elif currentFuncReturnType == 'str' and currentFunc != None:
			if l[1] in strs or l[1][0] == '"':
				funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\treturn None")
			else:
				quit("TypeError: Function {" + currentFunc + "} supposed to return an string!")
		elif currentFunc != None:
			funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\treturn None")
		else:
			quit('SyntaxError: Must be in a fuction to return!')
	elif l[0] == 'intf' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'int'
	elif l[0] == 'strf' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'str'
	elif l[0] == 'autof' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'auto'
	elif l[0] == 'push':
		funcs[currentFunc].append(('\t'*inif) +'push(' + l[1] + ')')
	elif l[0] == 'pop':
		funcs[currentFunc].append(('\t'*inif) +l[1] + ' = pop()')
	elif l[0] == 'str':
		if l[2][0] == '"' or l[2] in strs:
			funcs[currentFunc].append(('\t'*inif) +l[1] + ' = ' + l[2])
			strs.append(l[1])
		else:
			quit('TypeError: var {' + l[1] + '} needs to be an str!')
	elif l[0] == 'int':
		if worksAsInt(l[2]) or l[2] in ints:
			funcs[currentFunc].append(('\t'*inif) +l[1] + ' = ' + l[2])
			ints.append(l[1])
		else:
			quit('TypeError: var {' + l[1] + '} needs to be an int!')
	elif l[0] == 'auto':
			funcs[currentFunc].append(('\t'*inif) + l[1] + ' = ' + l[2])
	elif l[0] == '//':
		pass
	elif l[0] == 'if' and l[2] in comparators and l[4] == '{':
		funcs[currentFunc].append(('\t'*inif) + 'if ' + l[1] + ' ' + l[2] + ' ' + l[3] + ':')
		inif += 1
	elif l[0] == 'else if' and l[2] in comparators and l[4] == '{':
		funcs[currentFunc].append(('\t'*inif) + 'elif ' + l[1] + ' ' + l[2] + ' ' + l[3] + ':')
		inif += 1
	elif l[0] == 'while' and l[2] in comparators and l[4] == '{':
		funcs[currentFunc].append(('\t'*inif) + 'while ' + l[1] + ' ' + l[2] + ' ' + l[3] + ':')
		inif += 1
	elif l[0] == 'else' and l[1] == '{':
		funcs[currentFunc].append(('\t'*inif) + 'else:')
		inif += 1
	elif l[0] == '':
		pass
	else:
		quit('PostSyntaxError: Unknown statement: Lexer dump {' + str(l) + '}')

def sCreation(l):
	global structs, currentStruct
	name = l[0]
	if name == '}':
		currentStruct = None
		inScruct = False
	else:
		structs[currentStruct].append(name)



def cmpl(l):
	global mainDef, currentFunc, currentFuncReturnType, funcs, structs, currentStruct, inScruct, lineno
	lineno += 1
	o = l
	l = l.strip().replace('\t', '').split('  ')
	if mainDef:
		furtherAnalysis(l)
	#elif inScruct:
	#	sCreation(l)
	#elif l[0] == 'structure' and l[2] == '{':
	#	structs[l[1]] = []
	#	currentStruct = l[1]
	#	inScruct = True
	elif l[0] == 'intf' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'int'
		mainDef = True
	elif l[0] == 'strf' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'str'
		mainDef = True
	elif l[0] == 'autof' and currentFunc == None and l[2] == '{':
		funcs[l[1]] = []
		currentFunc = l[1]
		currentFuncReturnType = 'auto'
		mainDef = True
	elif l[0] == 'using':
		m = os.getcwd()
		os.chdir('libs')
		name = l[1][0:]
		print('Importing ' + os.getcwd() + '/' + name + '...')
		mainDef = True
		with open(name, 'r') as file:
			for l in file:
				l = l.replace('\n', '')
				cmpl(l.replace('\t', '')) 
		mainDef = False
		os.chdir(m)
	elif l[0] == '':
		pass
	elif l[0] == '//':
		pass
	else:
		quit('SyntaxError: Unknown statement: Lexer dump {' + str(l) + '}')

def cmpf(f):
	global funcs
	with open(f, 'r') as file:
		for l in file:
			try:
				cmpl(l)
			except IndexError:
				pass
	with open(f.replace('.hxa', '1.py'), 'w') as file:
		file.write('global pointer\npointer = 9999\nstack = [0' + (',0 '*9999) + ']\n\n')
		with open('utils/baseFuncs.py', 'r') as fno:
			for l in fno:
				file.write(l)
		for func in funcs:
			file.write('\n\ndef ' + func + '():')
			for l in funcs[func]:
				file.write('\n\t'+l)
			if func == 'main':
				file.write('\n\texit_hxa_code_var = pop()\n\texit(exit_hxa_code_var)')
		for struct in structs:
			file.write('\n\nclass ' + struct + ':')
			for l in structs[struct]:
				file.write('\n\t'+l)
		file.write('\n\nmain()')

if __name__ == '__main__':
	cmpf(sys.argv[1])