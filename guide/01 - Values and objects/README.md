# Values and objects

## Values
As to begin with, I will start with the most basic
part of hoverfly - **values**.

A value is everything expressing **numerical** data.
A value can be:
* number or char
* mathematical expression

A **number** is simply a 64-bit signed **integer**,
e.g. `-42069`, `5400` or `3`. A **char** is one letter
enclosed into single quotes, e.g. `'e'` or `'\n'`.

A **mathematical expression** is a row of operations
and other values. One simple example is
`(-1 + 2) / 4 + 3 * 10`.

## Variables
A **variable** is a **prefixed** value. This is the biggest
difference between hoverfly and most other languages.
The variable prefix is handled as a unary operator by the
interpreter. It can be one of `#`, `^`, `&` and `!` for
numbers, objects, streams and flags respectively.
Internally, hoverfly uses prefix `@` for strings,
which may not be used in the source code.

Numbers and flags variables are the only values under variables.

## Math using variables
Not a lot to explain, just an example: `#4 + #1 * 2 - #(1 - #3)`

## Objects
An **object** in hoverfly is a data type, which has **properties**.
The property name of an object is a value, the property data is
either a value or another object.

A **string** will be written in double quotes in hoverfly and
is of type object. Its properties stand for indexes of the string.
For example the string `"bebra"` has properties `0`, `1`, `2`,
`3`, `4` and `5` for `'b'`, `'e'`, `'b'`, `'r'`, `'a'` and
the null terminator respectively.

## Streams
Using stream in a mathematical expression **reads** one byte
from the stream. Reading from stream which is open for writing,
will produce an error.

## References
Referencing uncreated variables or not assigned object properties
will result in an interpreter error.

## Comments
It may be useful to know, how to create comments in the
hoverfly source code. It's simple, just use double colon
at start of line. Whitespace on begin of the line is always ignored.
`:: Happy coding!`