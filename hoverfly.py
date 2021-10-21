class Token :
  def __init__ ( self, value, t ) :
    self.value = value
    self.type = t

  def __str__ ( self ) :
    return "{}".format ( self.value )

def asi ( j ) :
  assert -2_147_483_647 <= j <= 2_147_483_647

def lexer ( f ) :
  import re
  d = f
  for s in re.findall ( r'''(?x)(?<!\\)".*?(?<!\\)"''', f ) :
    c = 0
    for a in strings : c += 1
    st = [ * bytes ( eval ( s ), "utf8" )]
    st.append ( 0 )
    string = { }
    for a, b in enumerate ( st ) :
      string [ a ] = b
    strings [ c ] = string
    f = f.replace ( s, "@{}".format ( c ), 1 )
    d = d.replace ( s, "", 1 )
  if "@" in d :
    raise Exception ( "Invalid syntax" )
  current = ""
  tokens_ = [ ]
  for i in f :
    if i in "+-*/()@#^&" :
      if current :
        tokens_.append ( current )
        current = ""
      tokens_.append ( i )
    elif i in "0123456789" :
      current += i
    elif i == "=" :
      if current :
        tokens_.append ( current )
      current = i
    elif i == ">" :
      current += i
      tokens_.append ( current )
      current = ""

  if current :
    tokens_.append ( current )

  tokens = [ ]
  for i in tokens_ :
    match i :
      case "(" : t = "LBR"
      case ")" : t = "RBR"
      case "+" : t = "ADD"
      case "-" : t = "SUB"
      case "*" : t = "MUL"
      case "/" : t = "DIV"
      case "@" : t = "STN"
      case "#" : t = "NUM"
      case "^" : t = "OBJ"
      case "&" : t = "STR"
      case "=>" : t = "GET"
      case _ :
        i = int ( i )
        asi ( i )
        t = "VAL"
    tokens.append ( Token ( i, t ))
  tokens.append ( Token ( None, "END" ))
  return tokens

class Parser :
  def __init__ ( self, tokens ) :
    self.tokens = tokens
    self.n ( )

  def n ( self ) :
    self.current = self.tokens.pop ( 0 )

  def parse ( self ) :
    if self.current.type == "END" :
      return None
    res = self.expr ( )
    if self.current.type != "END" :
      raise Exception ( "Invalid syntax" )
    return res

  def expr ( self ) :
    res = self.term ( )
    while self.current.type != "END" and self.current.type in [ "ADD", "SUB" ] :
      token = self.current
      self.n ( )
      res = BinOp ( res, token, self.term ( ))
    return res

  def term ( self ) :
    res = self.getter ( )
    while self.current.type != "END" and self.current.type in [ "MUL", "DIV" ] :
      token = self.current
      self.n ( )
      res = BinOp ( res, token, self.getter ( ))
    return res

  def getter ( self ) :
    res = self.factor ( )
    while self.current.type != "END" and self.current.type == "GET" :
      token = self.current
      self.n ( )
      res = BinOp ( res, token, self.factor ( ))
    return res

  def factor ( self ) :
    token = self.current

    if token.type == "LBR" :
      self.n ( )
      res = self.expr ( )
      if self.current.type != "RBR" :
        raise Exception ( "Invalid syntax" )
      self.n ( )
      return res
    elif token.type == "VAL" :
      self.n ( )
      return Val ( token )
    elif token.type in [ "NUM", "OBJ", "STN", "STR", "SUB", "ADD" ] :
      self.n ( )
      return UnOp ( token, self.factor ( ))
    else :
      raise Exception ( "Invalid syntax" )

class Reference :
  def __init__ ( self, place, reference ) :
    self.place = place
    self.reference = reference

  def __str__ ( self ) :
    return "{}[{}]".format ( self.place, self.reference )

class BinOp :
  def __init__ ( self, left, token, right ) :
    self.left = left
    self.token = token
    self.right = right

  def __str__ ( self ) :
    return "({}{}{})".format ( self.left, self.token, self.right )

class UnOp :
  def __init__ ( self, token, right ) :
    self.token = token
    self.right = right

  def __str__ ( self ) :
    return "({}{})".format ( self.token, self.right )

class Val :
  def __init__ ( self, token ) :
    self.token = token
    self.value = token.value

  def __str__ ( self ) :
    return str ( self.token )

class Interpreter :
  def __init__ ( self, node ) :
    self.root = node

  def eval ( self, ref = False ) :
    return self.visit ( self.root, ref )

  def visit ( self, node, ref = False ) :
    if not node : return None
    name = "visit" + type ( node ).__name__
    visiting = getattr ( self, name, self.ex )
    return visiting ( node, ref )

  def ex ( self, node, ref ) :
    raise Exception ( "Invalid Node Visitor visit{}".format (
      type ( node ).__name__ ))

  def visitBinOp ( self, node, ref ) :
    match node.token.type :
      case "ADD" :
        j = self.visit ( node.left ) + self.visit ( node.right )
        asi ( j )
        return j
      case "SUB" :
        j = self.visit ( node.left ) - self.visit ( node.right )
        asi ( j )
        return j
      case "MUL" :
        j = self.visit ( node.left ) * self.visit ( node.right )
        asi ( j )
        return j
      case "DIV" :
        l, r = self.visit ( node.left ), self.visit ( node.right )
        if l == r == 0 :
          return 0
        j = l / r
        j = int ( j )
        asi ( j )
        return j
      case "GET" :
        if ref :
          return Reference ( self.visit ( node.left ), self.visit ( node.right ))
        else :
          return self.visit ( node.left ) [ self.visit ( node.right )]

  def visitUnOp ( self, node, ref ) :
    match node.token.type :
      case "NUM" :
        r = self.visit ( node.right )
        if ref : return Reference ( "numbers", r )
        else : return numbers [ r ]
      case "OBJ" :
        r = self.visit ( node.right )
        if ref : return Reference ( objects, r )
        else : return objects [ r ]
      case "STN" :
        r = self.visit ( node.right )
        if ref : return Reference ( "strings", r )
        else : return strings [ r ]
      case "STR" :
        r = self.visit ( node.right )
        if ref : return Reference ( "streams", r )
        else : return ord ( streams [ r ].read ( 1 ))
      case "SUB" :
        r = self.visit ( node.right )
        if ref : raise Exception ( "Asked for reference from unary number operator" )
        else : return ( - r )
      case "ADD" :
        r = self.visit ( node.right )
        if ref : raise Exception ( "Asked for reference from unary number operator" )
        else : return r

  def visitVal ( self, node, ref ) :
    return node.value

numbers = { 0 : 0 }
objects = { }
streams = { 0 : open ( "/dev/stdin", "rb" ),
            1 : open ( "/dev/stdout", "wb" ),
            2 : open ( "/dev/stderr", "wb" )}
strings = { }

def quit ( ) :
  for s in streams :
    streams [ s ].close ( )
  exit ( 0 )

from sys import argv
try :
  file = argv [ 1 ]
  with open ( file, "r" ) as f :
    code = f.read ( )
except :
  print ( "No file" )
  quit ( )

if code.strip ( ) == "&?" :
  for s in streams :
    print ( s, streams [ s ])
  quit ( )

code = [ c for c in code.split ( "\n" )]
code = [ c for c in code if c ]
prepar = [ ]
for line in code :

  left, right = line.split ( "<=" )
  left_t = lexer ( left )
  left_p = Parser ( left_t )
  left_pd = left_p.parse ( )

  right_t = lexer ( right )
  right_p = Parser ( right_t )
  right_pd = right_p.parse ( )

  prepar.append ( [ left_pd, right_pd ])

while 0 <= numbers [ 0 ] < len ( prepar ) :

  left, right = prepar [ numbers [ 0 ]]
  inter_l = Interpreter ( left )
  source = inter_l.eval ( True )

  inter_r = Interpreter ( right )
  result = inter_r.eval ( )

  if source.place == "numbers" :
    numbers [ source.reference ] = int ( result or 0 )
  elif source.place == "strings" :
    strings [ source.reference ] = result or [ ]
  elif source.place == "streams" :
    streams [ source.reference ].write ( bytes ( [ result or 0 ]))
  else :
    source.place [ source.reference ] = result or { }

  numbers [ 0 ] += 1

quit ( )
