# Special values and flags
This chapter won't be long. I will talk about the
program counter, the exit flag and flags in common,
the standart arguments object and again about the streams.

## Program counter
The hoverfly interpreter run code **line by line**,
whereby empty lines, comments and flag definitions
get **ingnored**. To internally keep track of code flow,
there exists a **program counter**. At the beginning
of each code execution the counter is set to `0`.
After each line of code it gets increased by `1`. The interpreter
**halts**, whenever the program counter **exceeds** the range of
the code lines. Main thing about all this is that the
program counter is accessible from inside the code.
It is represented through the `#0` number variable.
It can be read and set just like a **normal variable**, except
after each line of code, the counter gets altered.
This can be used to implement basic **control flow** in hoverfly.
While it is possible to directly change it using assignment,
like this: `#0 <= 10`, it is rather recommended to use
flags to jump.

## Flags
Flags in common are interesting things. They are being defined
before all the rest of the code gets executed. Their definition
is simply writing down `!` and a number as the name for the flag.
An example for a flag definition is `!10` or `!-12`.

## Exit flag
As already mentioned earlier, the interpreter halts, whenever
the range of code lines gets exceeded. That means, if there
are 10 lines of code in the file, programm will exit, once
reached the state `#0 == 10`. But you can also jump below the
minimum level of `0`. First intuitive guess is to set the
program counter to `-1`. However after setting it, the
interpreter will increase the counter, which will land on a
`0` again and begin to run the code from the start. Therefore
the program counter should be set to `-2` to exit the program
surely. Since there are many important variables with the value
`0`, the exit flag is also `!0`, which does not have to be defined,
and simply equals the value `-2`.

## Standart arguments object
Whenever you write your code, do not use the `^0` object
for calculations. While this one is not needed to follow,
it is best practice to do so. The object `^0` will be later
used as an argumnets and return value container for importing
and functions. In the best case just don't use it before
learning about imports and functions.

## Streams
Their functionality has been explained earlier already.
Now about their value:
* `&0` - stdout, open for writing
* `&1` - stdin, open for reading
* `&2` - stderr, open for writing
