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
We speak of initialization if the right side is empty.

### Numbers
Assigning to numbers is the easiest. On initialization,
variable gets assgined `0`. Else, the value is used. Example:
`#1 <= 5 + 2` will result in `#1 == 7`,
`#2 <=` will result in `#2 == 0`

### Objects
Assigning to pure object is not directly possible, except
the right hand produces an object as result. What often
is used, is objeft initialization. It creates an empty object
without properties. Assinging numeric value to an object is
technically possible, but will result in unexpected behaviour.
Often seen: `^69 <=`

### Object properties
Initialization of an object property will always create an empty object.
To assign a number, a value has to be used in the right side.
Example: ```
:: create empty object ^1 using initialization
^1 <=

:: create number property and assign value
^1 => 1 <= 69

:: create object property using initialization
^1 => 2 <=

:: assign value to a new property of it
^1 => 2 => 3 <= 5
```

