# Style
There is not a lot to say about the style. You may write
the code in any way you want. But this is a little guideline
you can keep to, to write nicer code.

## Comments
When creating variables, it is a good manner to describe,
what it does, because hoverfly has no names for variables.

## Loops and other body statements
Best practice is to indent everything after the loop
definition flag until the final repeat/break statement
statement. Also better explain, why and when your loop
closes. You may use any code or even pseudecode as you
prefer. Example:
```
:: run variable
#1 <= 14
!1
  :: here is the body of the loop
  #1 <= #1 - 1
  :: if #1 == 0: break
  #0 <= #0 + (1 - #1 / #1)
  :: else: repeat
  #0 <= !1
```

## Math
I really like when any operator is wrapped
into spaces from both sides. Like this:
`#0 <= #0 + (1 - #1 / #1)`

## Final words
Thanks for reading this. I hope you enjoyed the guide
and will enjoy hoverfly language in the future!