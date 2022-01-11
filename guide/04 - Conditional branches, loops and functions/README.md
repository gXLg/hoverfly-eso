# Conditional branches, loops and functions
## Jumping
**Jumping** was already explained in the previous chapter.
Jumping is an **absolute** movement of the program counter.
If can be used to exit the program with `!0` flag or
make an infinite unconditional cycle.

## Branching
While the result is the same and the program counter
gets altered, the principe behind **branching** is another
as behind jumping. In branching, the offset is made
**relative** to some factors as variables. For example
this line of code would fall under the category of
branching: `#0 <= #0 + #1`, while this is another
example for jumping: `#0 <= !3`. Relative jumps as this
one - `#0 <= #0 + 10` - are not clearly jump or branch,
because they do not depend on any other factors as
the program counter itself, but they are aslo not an
absolute jump.

## Conditional branching
The definition of jumping excludes any conditions,
because it will be made without depending on
anything else. That's why branching is used for
conditions implementation. The idea behind
**conditional branching** is that the program counter gets
altered depending on a value. This value is expressing
the result of a condition, for example, the equality:
```
#1 <= 45
#2 <= 45
#3 <= (#2 - #1)/(#2 - #1)
```
Here the number `#3` holds the value for condition `#1 == #2`.
The conditional branch with that one would be
```
#0 <= !(10 + #3)
```
If `#3` has `0`, then the branching will be made to
flag `!10`, if `#3` has `1`, then the branching will
be made to flag `!11`. Another point to remember is,
that after executing the part under flag `!10`, you
have to jump till end of the code under flag `!11`. This
complete case would look like this (indents only for style):
```
#1 <= 45
#2 <= 45
#3 <= (#2 - #1)/(#2 - #1)
#0 <= !(10 + #3)
!10
  :: some code here if #1 == #2
  #0 <= !12

!11
  :: some code here if #1 != #2

!12
:: code goes on
```
This is a full implementation of an if-statement.
When doing multiple of such statements, don't forget
to use **new flags** for each condition. Even though there
is no error when a flag gets defined twice, only the
last definition of the flags actually counts.

## Loops
Loops are nothing special. They are just if statememts
with one of the bodies jumping back to the start of the loop.
An example for a `while #1 != 0` loop:
```
#1 <= 12
!1
  #1 <= #1 - 1
  #0 <= #0 + (1 - #1 / #1)
  #0 <= !1
```
Here the branching occures if `#1` is `0`. Then it branches
outside of the loop, else jump to begin of loop will be made
and the variable will be decreased once again.

## Functions
The functions exist only in theory. I haven't used them
myself yet. Basic thing for functions is that they in best
case should be defined at the end of the file with an exit
statement before, so that the code inside does not get
executed. The implementation of functions could consist of
a stack, which stores the last position of program counter
before jumping to the function, and a stack counter, which
stores the amount of entries in the stack. This is needed
because the code inside a function can also call another
function. As already talked about in last chapter, arguments
should be passed over the `^0` object. Calling a function
would be made as following:
1) Arguments are set up in the `^0` object
2) Increasing stack counter
3) Setting new stack entry to the program counter + 1
4) Jumpin to the function
Returning would be made very similar:
1) Return value is set into `^0`
2) Getting stack entry
3) Decreasing stack counter
4) Jumping to the get entry point
Code example for sum function:
```
:: setting up stack
^1 <=
^1 => 0 <= 0

:: setting up arguments
^0 <=
^0 => 1 <= 24
^0 => 2 <= 45
:: function call
^1 => 0 <= (^1 => 0) + 1
^1 => (^1 => 0) <= #0 + 1
#0 <= !1000

:: exit before the functions
#0 <= !0



:: the function
!1000
  :: saving function result
  #1 <= (^0 => 0) + (^0 => 1)
  ^0 <=
  ^0 => 1 <= #1

  :: returning
  #1 <= ^1 => (^1 => 0)
  ^1 => 0 <= (^1 => 0) - 1
  #0 <= #1
```
As expected, the function returns `69`.
One more problem would be to correclty store
all variables inside the function, to not conflict with
the rest of the code. My suggestion for this is to use
the stack in negative side to store variables.
However it does not seem to be an easy solution, so
the recursion function aren't easy to implement.
I won't go very deep into details here, just an example
of how to implement recursive fibonacci:
```
:: setup stack
^1 <=
^1 => 0 <= 0

:: call fibonacci(10)
^0 <=
^0 => 1 <= 10
^1 => 0 <= (^1 => 0) + 1
^1 => (^1 => 0) <= #0 + 1
#0 <= !1000
<= lib:io/putnat
:: prints '89'



:: exit()
#0 <= !0



:: fibonacci(a)
!1000

  ^1 => -(^1 => 0) <=
  ^1 => -(^1 => 0) => 1000 <= ^0 => 1
  :: store if 0
  ^1 => -(^1 => 0) => 1001 <= (^1 => -(^1 => 0) => 1000) / (^1 => -(^1 => 0) => 1000)
  :: store if 1
  ^1 => -(^1 => 0) => 1000 <= (^1 => -(^1 => 0) => 1000) - 1
  ^1 => -(^1 => 0) => 1002 <= (^1 => -(^1 => 0) => 1000) / (^1 => -(^1 => 0) => 1000)
  :: OR operation
  ^1 => -(^1 => 0) => 1001 <= (^1 => -(^1 => 0) => 1001) * (^1 => -(^1 => 0) => 1002)

  :: jump to 1001 if any of them else 1002
  #0 <= !(1001 + (^1 => -(^1 => 0) => 1001))

  !1001
    ^1 => -(^1 => 0) => 1002 <= 1
    #0 <= !1003

  !1002
    :: call fibonacci(a-1)
    ^0 <=
    ^0 => 1 <= ^1 => -(^1 => 0) => 1000
    ^1 => 0 <= (^1 => 0) + 1
    ^1 => (^1 => 0) <= #0 + 1
    #0 <= !1000

    :: save result in 1002
    ^1 => -(^1 => 0) => 1002 <= ^0 => 1

    :: call fibonacci(a-2)
    ^0 <=
    ^0 => 1 <= (^1 => -(^1 => 0) => 1000) - 1
    ^1 => 0 <= (^1 => 0) + 1
    ^1 => (^1 => 0) <= #0 + 1
    #0 <= !1000

    :: add result in 1002
    ^1 => -(^1 => 0) => 1002 <= (^0 => 1) + ^1 => -(^1 => 0) => 1002

  !1003
    :: return 1002
    ^0 <=
    ^0 => 1 <= (^1 => -(^1 => 0) => 1002)
    ^1 => -(^1 => 0) => 1003 <= ^1 => (^1 => 0)
    ^1 => 0 <= ^1 => 0 - 1
    #0 <= ^1 => -((^1 => 0) + 1) => 1003
```
Yes, I have friends. No, I don't need help. Thanks.
In python it takes just two lines:
```py
fibo = lambda a: 1 if a in [0, 1] else fibo(a - 1) + fibo(a - 2)
fibo(10)
```
