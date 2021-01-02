# HexaLang or Hexa
Pronounced ɛks-ah

# Basic Hexa Program Layout

Hexa programs are structured very similar to that of C or C++. Having a main function with curly braces around the code contained inside of it.

```
intf  main  {  ()
	<code>
}
```

# Hello, World!

Writing to the screen without a library is a major pain. That's why Hexa stdlib comes out of the box with a library containing a function to print to the screen. I will show you both ways in case you needed to use the harder way.

### Easy way

```
using  stdout.hxa

intf  main  {  ()
	push  "Hello, World!"
	call  printl
}
```

### Hard way

```
intf  main  {  ()
	push  "Hello, World!"
	push  "stdout"
	call  write
	call  flush
	call  newline
}
```

# What are pushes and pops?

If you saw that last code, you might have saw the commands `push` and `pop`.

Hexa is a completely stack-based language meaning that to get much done you must get yourself comfortable with the stack.

The stack is a Last In-First Out or LIFO data structure.

The stack is just like a stack of anything really you can put an item on top of the stack by using the syntax `push  <value/variable>` and take the item on top of the stack off by using the syntax `pop  <variable>` and it will store that value in the variable specified.

# Variables

Here are the data types in Hexa.

- int
- str
- bool
- auto
- double
- functions are also a type

In future updates this list is sure to get updates with things such as 'char', 'struct', and 'arr'.

Variable definition 

```
<type>  <name>  <value>
```

So, for example.

```
int  x  2
```

Strings look like this:

```
str  y  "Hello"
```

Bools look like this

```
bool  z  True
//  or
bool  z  False
```

Auto's look like this

```
auto  x  <anything that fits the other types can go here>
```

Doubles look like this

```
double  y  0.5
```