import sys
import math

balance = 0

constants = {
	
}

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