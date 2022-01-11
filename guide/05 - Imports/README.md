# Imports
Imports in hoverfly have following syntax:
```
<= <source>:<path>
```
`source` can currently be `base` or `lib`.
In base imports, `path` is relative to
the executed hoverfly file. In `lib` -
to the hoverfly interpretor path + `/lib`.
The file to be imported, must have a `.fly`
extension, which does not get specified in
the import path. An import works as following:
the code get read into memory and parsed.
After one time importing a file, the
interpreter will keep its' parsed tree
in cache for the runtime. After parsing, the
code gets executed as were run in single file.
The difference is, the objects from the previous
code are kept. That means the imported code can
read and write into objects, that were defined in
original code. This is used to store arguments
and return value, as earlier mentioned,
in the `^0` object.

## Libs
There are currently a lot of predefined libs
in the `/lib` folder. Keep your repo updated,
to qlways have the newest libs. Currently,
they use a help format, which look like this:
```
:: args
::   <argument>: <explanation>
::   [...]
:: return
::   <argument>: <explanation>
::   [...]
```
It is pretty self-explanatory. I will explain
one example though. This is the help header
of `lib:io/puts` library:
```
:: args
::   0 : string
:: return
::   0.1 : string len
```
Here the lib uses `^0` to store
the string object. In the end, the length
of the string is returned in `^0 => 1`.