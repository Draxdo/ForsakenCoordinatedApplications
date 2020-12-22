try:
	import sys
	import math
	import os
	import threading

	balance = 0

	constants = {
		
	}

	class char:
		def __init__(self, v):
			if len(v) == 0:
				self.v = [v]
			else:
				self.v = [v[0]]
		def __add__(self, other):
			x = []
			for i in self.v:
				x.append(i)
			for i in other.v:
				x.apend(i)
			return x
		def __repr__(self):
			string = ""
			for i in self.v:
				string += i
			return string

	def restore_ptr():
		global pointer
		pointer += balance - 1

	def push(v):
		global pointer, balance
		pointer -= 1
		stack[pointer] = v
		balance += 1

	def pop():
		global pointer, balance
		x = stack[pointer]
		pointer += 1
		balance -= 1
		return x

	def add():
		x = pop()
		y = pop()
		push(x + y)

	def sub():
		x = pop()
		y = pop()
		push(x - y)

	def flush():
		sys.stdout.flush()

	def fout():
		p = pop()
		f = pop()
		x = pop()
		if p not in ['a', 'w']:
			quit("Unknown protocol '" + p + "'")
		try:
			with open(f, p) as file:
				file.write(x)
		except:
			quit("FileError while writing!")

	def fin():
		f = pop()
		b = pop()
		try:
			with open(f, 'r') as file:
				push(file.read(f, b))
		except:
			quit("FileError while reading!")

	def system():
		x = pop()
		os.system(x)

	def chdir():
		x = pop()
		os.chdir(x)

	def remove():
		x = pop()
		try:
			os.remove(x)
		except:
			quit("Error whilst removal!")

	def makefile():
		x = pop()
		try:
			with open(x, 'w') as fw:
				fw.write('')
		except:
			quit("Error whilst file creation!")

	def getcwd():
		push(os.getcwd())

	def write():
		f = pop()
		x = pop()
		if f == "stdout":
			sys.stdout.write(x)
		elif f == "stderr":
			sys.stderr.write(x)

	def stdin():
		s = pop()
		push(sys.stdin.read(s))

	def to_int():
		try:
			x = pop()
			push(int(x))
		except:
			quit("Can't convert this type to type 'int'!")

	def to_str():
		try:
			x = pop()
			push(str(x))
		except:
			quit("Can't convert this type to type 'str'!")

	def newline():
		print('\n', end='')

	def mul():
		x = pop()
		y = pop()
		push(x * y)

	def div():
		x = pop()
		y = pop()
		push(x / y)

	def mod():
		x = pop()
		y = pop()
		push(x % y)

	def argv():
		arg = argv[0:]
		x = pop()
		push(arg[x])

	def add_to():
		x = pop()
		n = pop()
		if isinstance(n, dict):
			s = pop()
			n[x] = s
		elif isinstance(n, list):
			n.append(x)
		push(n) 

	def put():
		try:
			x = pop()
			x = x[0]
			push(x)
			push("stdout")
			write()
			push(0)
		except:
			print("Exception ignored: RUNTIMEERROR: STACK PTR BASED OVERFLOWERR")
			push(1)

	def puts():
		try:
			x = pop()
			for i in x:
				push(i)
				put()
			push(0)
		except Exception as e:
			print("Exception ignored: RUNTIMEERROR: STACK PTR BASED OVERFLOWERR")
			push(1)

	def cin():
		try:
			push(1)
			stdin()
			x = ""
			pop(x)
			push(ord(x))
		except:
			print("Exception ignored: RUNTIMEERROR: STDIN ERR")
			push(1)

	def itoa():
		x = pop()
		push(chr(int(x)))

	def atoi():
		x = pop()
		push(ord(str(x)))

	def sizeof():
		x = pop()
		push(len(x))