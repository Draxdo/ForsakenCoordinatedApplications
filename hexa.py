#!/usr/bin/env python3
# version stuff
major = '1'
minor = '6'
patch = '8'

version = major + '.' + minor + '.' + patch







# imports

import os
import sys











# globals

currentFunc = None
path = ''
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
	'add_to',
	'fout',
	'fin',
	'system',
	'chdir',
	'remove',
	'makefile',
	'getcwd',
	'puts',
	'put',
	'cin',
	'itoa',
	'atoi',
	'sizeof'
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




lineno = 0
inScruct = False
ints = ['pointer']
strs = []
mainDef = False
currentFuncReturnType = None
inif = 0
currentStruct = None
privates = []
scopeP = []
changing = []
bools = []
dubs = []
consts = {}
threads = []
upper = []
funcargs = {}









# code

def worksAsDub(s):
	try:
		x = float(s)
		return True
	except:
		return False
	return False
	
def realLen(s):
	return len(s) - 1
	
def getLast(s):
	return s[realLen(s)]
	

def worksasarr(s):
	if realLen(s) >= 1:
		f = s[0]
		l = getLast(s)
		if f == "[" and l == "]":
			return True
		else: 
			return False
	else:
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
	global currentFunc, currentFuncReturnType, funcs, inif, structs, lineno, version, scopeP, changing, threads
	if l[0] == 'intf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'int'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'int'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'strf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'str'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'str'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'doublef' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'dub'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'dub'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'boolf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'bool'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'bool'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'autof' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'auto'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'auto'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == '}':
		if inif > 0:
			inif -= 1
		elif currentFunc != None:
			currentFunc = None
			currentFuncReturnType = None
			mainDef = False
		else:
			quit("SyntaxWarning: No scope to end with '}'! Lineno: " + str(lineno))
	elif l[0] == 'call' and currentFunc != None:
		if l[1] in builtInFuncs or l[1] in funcs:
			if l[1] in privates and l[1] not in scopeP:
				quit('Function <' + l[1] + '> is not accessible in this scope!')
			elif l[1] in privates and l[1] in scopeP:
				if l[1] in threads:
					funcs[currentFunc].append(('\t'*inif) + "threading._start_new_thread(" +l[1] + ', '+ l[2]+' )')
				else:
					funcs[currentFunc].append(('\t'*inif) +l[1] + l[2])
			else:
				if l[1] in threads:
					funcs[currentFunc].append(('\t'*inif) + "threading._start_new_thread(" +l[1] + ', '+ l[2]+')')
				else:
					funcs[currentFunc].append(('\t'*inif) +l[1] + l[2])
		elif l[1] == '@':
			funcs[currentFunc].append(('\t'*inif) +'foo = pop()\n\tfoo' + l[2])
		else:
			quit("NameError: Function {" + l[1] + "} is undefined!")
	elif l[0] == 'return':
		if currentFuncReturnType == 'int' and currentFunc != None:
			if l[1] in ints or worksAsInt(l[1]):
				funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\t\treturn None")
			else:
				quit("TypeError: Function {" + currentFunc + "} supposed to return an integer!")
		elif currentFuncReturnType == 'str' and currentFunc != None:
			if l[1] in strs or l[1][0] == '"':
				funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\t\treturn None")
			else:
				quit("TypeError: Function {" + currentFunc + "} supposed to return an string!")
		elif currentFunc != None:
			funcs[currentFunc].append(('\t'*inif) +"push(" + l[1] + ")\n\treturn None")
		else:
			quit('SyntaxError: Must be in a fuction to return!')
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
	elif l[0] == 'bool':
		if l[2] in ['True', 'False', 'None']:
			funcs[currentFunc].append(('\t'*inif) +l[1] + " = " + l[2])
		elif l[2] in bools:
			funcs[currentFunc].append(('\t'*inif) + l[1] + " = " + l[2])
		else:
			quit('TypeError: var {' + l[1] + '} needs to be a bool!')
	elif l[0] == 'int':
		if worksAsInt(l[2]) or l[2] in ints:
			funcs[currentFunc].append(('\t'*inif) +l[1] + ' = ' + l[2])
			ints.append(l[1])
		else:
			quit('TypeError: var {' + l[1] + '} needs to be an int!')
	elif l[0] == 'double':
		if worksAsDub(l[2]) or l[2] in dubs:
			funcs[currentFunc].append(('\t'*inif) +l[1] + ' = ' + l[2])
			dubs.append(l[1])
		else:
			quit('TypeError: var {' + l[1] + '} needs to be an double!')
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
	elif l[0] == '!getver':
		funcs[currentFunc].append(('\t'*inif) + "push('" + version + "')")
	elif l[0] == '@private':
		if currentFunc not in privates:
			privates.append(currentFunc)
		else:
			quit("Function <" + currentFunc + '> already declared as private!')
	elif l[0] == '@changing':
		if currentFunc not in changing:
			changing.append(currentFunc)
		else:
			quit("Function <" + currentFunc + "> is already a changing function!")
	elif l[0] == '@thread':
		if currentFunc not in threads:
			threads.append(currentFunc)
		else:
			quit("Function <" + currentFunc + "> is already a thread function!")
	elif l[0] == '!include':
		if l[1] not in scopeP and l[1] in funcs:
			 scopeP.append(l[1])
		elif l[1] in funcs:
			quit("Function <" + l[1] + '> already declared in this scope!')
		else:
			quit("Function <" + l[1])
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
	global mainDef, currentFunc, currentFuncReturnType, funcs, structs, currentStruct, inScruct, lineno, scopeP, changing, funcargs
	lineno += 1
	o = l
	l = l.strip().replace('\t', '').split('  ')
	if mainDef:
		furtherAnalysis(l)
	elif l[0] == 'intf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'int'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'int'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'define' and l[1] not in consts and l[1] not in dubs and l[1] not in strs and l[1] not in ints and l[1] not in bools:
		upper.append(l[1] + " = " + l[2])
		bools.append(l[1])
		strs.append(l[1])
		ints.append(l[1])
		dubs.append(l[1])
		print("Defined constant {" + l[1] + "}")
	elif l[0] == 'doublef' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'dub'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'dub'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'strf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'str'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'str'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'boolf' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'bool'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'bool'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'autof' and currentFunc == None and l[2] == '{':
		if l[1] not in funcs:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'auto'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		elif l[1] in funcs and l[1] in changing:
			funcs[l[1]] = []
			currentFunc = l[1]
			currentFuncReturnType = 'auto'
			scopeP = []
			funcargs[l[1]] = l[3]
			mainDef = True
		else:
			quit("Static function <" + l[1] + "> already exists!")
	elif l[0] == 'using':
		m = os.getcwd()
		os.chdir(path + '/libs')
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
	global funcs, upper, funcargs
	try:
		with open(f, 'r') as file:
			for l in file:
				try:
					cmpl(l)
				except IndexError:
					pass
	except FileNotFoundError as e:
		quit("Specified file does not exist!")
	with open(f.replace('.hxa', '.py'), 'w') as file:
		file.write('global pointer\npointer = 9999\nstack = [0' + (',0 '*9999) + ']\n\n')
		with open(path + '/utils/baseFuncs.py', 'r') as fno:
			for l in fno:
				file.write(l)
		for l in upper:
			file.write(l)
		for func in funcs:
			file.write('\n\n\tdef ' + func + funcargs[func] + ':')
			for l in funcs[func]:
				file.write('\n\t\t'+l)
		for struct in structs:
			file.write('\n\n\tclass ' + struct + ':')
			for l in structs[struct]:
				file.write('\n\t\t'+l)
		file.write('\nexcept:\n\tquit("Segmentation fault (core dumped)")\n\nmain()')

if __name__ == '__main__':
	cmpf(sys.argv[1])