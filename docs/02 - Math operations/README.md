# Math operations

## Mathematical expressions
The basic elements of an expression are
`+`, `-`, `*`, `/`, `(`, `)` and values.
The result of a mathematical expression is always an
integer, that means `10 / 4` will produce `2`.
Also, **division by zero** returns error if any number
gets divided, except if the number is zero itself,
that means `0 / 0` will produce `0`. This "feature"
will be called "anomaly" in the latter documentation.

## Get-operator
To get property of an object the get-operator `=>` is used.
For example: `^1 => 1` or `"string" => 0`.

Even mathematical expressions can be used:
`^(1 + #1) => (2 + #2)`

Get-chains are possible:
`^1 => (1 + #1) => 2 => #3`

## Assigning and initialization
To assign a value the ass-operator `<=` is used.
On the **right side** is the value to be assigned or nothing,
on the **left side** is the variable reference.
The assigning process works different for different types of variables.
We speak of **initialization** if the right side is empty.
You can **always** assign or initialize a variable, even if it is
already created, except for flags.

### Numbers
Assigning to numbers is the easiest. On initialization,
variable gets assgined `0`. Else, the **value** is used.
Example: `#1 <= 5 + 2` will result in `#1 == 7`,
`#2 <=` will result in `#2 == 0`

### Objects
Assigning to pure object is **not directly possible**,
except the right side produces an object as result.
An example for the right side object is a string.
What often is used, is **object initialization**.
It creates an **empty** object without properties.
Assinging numeric value to an object is technically
possible, but will result in unexpected behaviour.
Initialization of already created object is used to
clear the object. Often seen: `^69 <=`

### Object properties
**Initialization** of an object property will always create
an empty object. To assign a number, a **value** has to be used
in the right side. Example:
```
:: create empty object ^1 using initialization
^1 <=

:: create number property and assign value
^1 => 1 <= 69

:: create object property using initialization
^1 => 2 <=

:: assign value to a new property of it
^1 => 2 => 3 <= 5
```

### Streams
The ass-operator is used to **write** to streams. The right
side must produce a **byte** value, this value will then
be written to the stream. Initialization produces a `0`.
Creating new streams is currently **not possible**. Writing to
stream which is opened for reading, will produce an error.

### Flags
Flags are **constant** and can't be assigned or initialized with
the ass-operator. They are used for jumping, which will be
explained in '04 - Basic control flow'.

### Empty left side
This situation tells the interpreter that it's an **import statement**.
More about imports will be talked in '07' and '08'.

## Operation order
The mathematical elements of hoverfly syntax create an order
in which expressions are evaluated.
1) Expressions in brackets `(`, `)`
2) Unary `+`, `-`
3) Variable unary `#`, `^`, `&`, `!`, `@`
4) Get-operator `=>`
5) First order binary `*`, `/`
6) Second order binary `+`, `-`
7) Ass-operator `<=`

## Advanced operations
Combining integer division, anomaly and your brain,
you can represent multiple advanced operations using
native syntax of hoverfly. `(N)` - means "for natural numbers"

### Modulo (N)
This one is easy. No explanation needed.
```
:: a = 56
#1 <= 56

:: b = 3
#2 <= 3

:: c = a % b
#3 <= #1 - #1 / #2 * #2
```

### Equality
If two numbers are the same, their difference will be `0`.
Division of a number by itself will always produce `1`,
except in anomaly, it produces `0`.
```
:: a = 45
#1 <= 45

:: b = 45
#2 <= 45

:: c = int(a == b)
#3 <= 1 - (#1 - #2) / (#1 - #2)
```

### Greater or equal (N)
If a number is greater or equal, it will be at least `1` after
dividing by the other number.
```
:: a = 37
#1 <= 37

:: b = 98
#2 <= 98

:: c = (a >= b)
#3 <= (#1 / #2) / (#1 / #2)
```

### >= 0
A square of a number is always positive. Adding the number
and its square will provide a smaller number, if the
original number was negative.
```
:: a = -3
#1 <= -3

:: b = a * a
#2 <= #1 * #1

:: c = b + a
#3 <= #1 + #2

:: d = (a >= 0)
#4 <= (#3 / #2) / (#3 / #2)
```

### Other
Many other **crazy** things can be implemented,
using only these ideas. Learn, explore, widen
your mind and become a **mad scientist**!