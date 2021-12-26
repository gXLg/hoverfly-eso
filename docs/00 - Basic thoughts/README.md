# Basic thoughts
Before creating the language, I really liked
the look of **redirecting** values like sometimes
in C++. This inspired me to design a new and
unique language syntax which later was called
hoverfly.

But with small to none experience of parsing syntax
trees, it fast became clear to me to be an impossible
task to implement it. That said I decided to start
with **easy syntax** and move onward until I create a perfect
language. In theory.

In practice, I created a very easy abstract syntax...
and I liked it. That's why there is only one
version of hoverfly, and yet an **esoteric** one.

I named it hoverfly, because there exists an inscet called
with that name. It mimics a bee to not be eaten or attacked.
This is my beloved insect. The name itself is actually not
connected to the language, I chose it just because I can.

Hoverfly is a **turing complete** and **very simple** language,
but in order to achieve great things, great code
must be written.

Hoverfly is purely **imperative**. Not like in 'normal'
languages is the variable system. The variables
aren't called with names but with **numbers**. That allows
a tricky system of dynamic variable references and
complex mathematical expressions.

The interpreting of hoverfly code is run in several steps:
1) Code gets splitted into lines
2) Empty lines or comments get removed
3) Each line gets lexed and parsed
4) Line after line, code gets executed
This aprocah has some advantages: syntax errors occure
before some operations are made, code easily gets interpreted
multiple times on branching.

In the process of learning hoverfly you will be
surprised by the simplicity and in the same time
complexity of it. Good luck learning hoverfly
**as your new beloved esoteric language**!