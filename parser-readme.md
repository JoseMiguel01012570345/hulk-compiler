
# HULK PROGRAMMING LANGUAGE

# Function caLL

- $F -> cP \space|\space cN \space|\space cT$
- $P -> ( p )$
- $T -> F$
- $N ->( )$

# Strings

- $T -> T@T \space|\space F@T \space|\space T@@T \space|\space F@@T$
- $E -> T@E \space|\space F@E \space|\space T@@E \space|\space F@@E$

# Expression_block

- $O -> EE  \space | \space O \$ 2O \space|\space T\$2 O \space|\space OE \space|\space OB \space|\space O \$2 b | b \$2 E \space|\space ME \space|\space EM \space|\space OM \space|\space MO \space|\space OQ \space|\space Q\$2$
- $O -> E \$2 M \space|\space M \$2 O | \space O \space T$
- $O -> O \$2 E \space|\space E \$2 b  \space|\space E \$2 O \space|\space O \$2 | O; | E \$2 E | b \$2 b | O \$2 M$
- $b -> \{ O \} \space|\space \{ E \} \space|\space \{ B \} \space|\space \{ \} \space|\space b \$2 \space| \space \{ b \} \space|\space \{ T \}$
- $B -> b;$
- $T -> T \$2 $
- $E -> E \$2 \space|\space B$
- $E -> \$2 ; \$3 | E;$
- $b -> { M }$
- $E -> T;$
- $T -> T.E \space|\space F.E \space|\space T.T | F.T |$
- $E -> T.E$

# Literals

- $T -> let\space  T \space|\space T:T$
- $E -> let\space E \space|\space T:E$
- $p -> T \space , \space \$2 \space  T \space|\space T \space , \space \$2 p$
- $T -> T:=T$
- $E -> T:=E$
- $T -> T=T$
- $E -> T=E$
- $T -> T \space as\space  T \space|\space F \space as\space  T \space|\space T \space as\space  E$
- $E -> T \space as\space  E$
- $E -> T;\$2$
- $T -> ( T )$

# booleans

- $T -> T \& T \space | \space  F \& T \space | \space  T | T \space| \space F | T \space | \space  T != T  \space | \space  F != T  \space | \space T>T \space|\space  F>T  \space|\space T<T \space|\space F<T \space|\space  T<=T \space|\space F<=T \space|\space
            T>=T \space|\space F>=T \space|\space T==T \space|\space F==T \space|\space
            TisT \space|\space F\space is\space T$

- $E -> T\&E \space|\space T|E \space|\space T!=E \space|\space
            T>E  \space|\space T<E \space|\space T<=E \space|\space
            T>=E \space|\space T==E \space|\space
            T\space is\space E$

# numbers

- $T ->  T+T \space|\space T+T \space|\space T-T \space|\space  T*T \space|\space T/T \space|\space T/T \space|\space T^T \space|\space T\%T \space|\space T**T$
- $T ->  T\$2+T \space|\space T\$2+T \space|\space T\$2-T \space|\space  T\$2*T \space|\space T\$2/T \space|\space T\$2/T \space|\space T\$2^T \space|\space T\$2\%T \space|\space T\$2**T$
- $E ->  T\$2+E \space|\space T\$2+E \space|\space T\$2-E \space|\space  T\$2*E \space|\space T\$2/E \space|\space T\$2/E \space|\space T\$2^E \space|\space T\$2\%E \space|\space T\$2**E$
- $E ->  T+E \space|\space F+E \space|\space T-E \space|\space  T*E \space|\space T/E \space|\space T/E \space|\space T^E \space|\space TE$

- $T ->  T-=T \space|\space T+=T \space|\space T/=T [T,*=,T] , [T,--]  , [T,++]]]$
- $T ->  T-=T \space|\space T+=T \space|\space T/=T \space|\space T*=T \space|\space T-- \space|\space T++$
- $E ->  T-=E \space|\space T+=E \space|\space T/=E \space|\space T*=E \space|\space E-- \space|\space E++ \space|\space E** \space|\space E**E$

# IN

- $p -> p\$2$
- $T ->  T\space in\space T \space|\space T\$2\space in\space T \space|\space p\$2inT \space|\space p\$2\space in\space p \space|\space p\space in\space T \space|\space p\space inp\space$
- $T ->  T\$2$
- $E ->  T\space in\space E \space|\space T\$2\space in\space E \space|\space T\space in\space b \space|\space T\$2inb \space|\space p\$2\space in\space E \space|\space pinE \space|\space p\space in\space b \space|\space p\$2\space in\space b$

# For

- $E ->  for\space T\$2B \space|\space for\space T\$2E \space|\space forTE$
- $E ->  for\space T\$2b$

# conditional

- $if -> if\space T\$2E \space|\space if\space T\$2b \space|\space if\space T\$2B \space|\space if\$2 \space|\space if T \$2 T$
- $elif -> if\space elif\space T\$2E \space|\space if\space elif\space T\$2b \space|\space if\space elif\space T\$2B \space|\space elif\$2 \space|\space if\space elif\space  T \$2 T$
- $E -> if\space else\space E \space|\space ifelseb \space|\space ifelseB$
    
- $E -> elif\space else\space E \space|\space elif\space else\space b \space|\space elif\space else\space B$

- $T -> elif \space else \space T | if \space else \space T$

# While

- $E ->  while \space T\$2B \space|\space while \space T\$2E \space|\space while\space T\space E$
- $E -> while \space T \space \$2 \space b$ 

- $E -> while \space T \space \$2 \space B | while \space T \space \$2 \space E \space | \space while \space T \space E \space$
- $E -> while \space T \space \$2 \space b$

# function

   ["M" , [ ["function","T","$2","=>","$2","E"] , ["function","T","$2",":","T" ,"=>","$2","E"] 
            ,["function","T","$2","=>","$2","b"] ,["function","T","$2",":","T","=>","$2","b"] ,
             [ 'function', 'T',"$2", ':', 'T', 'b'],['function', 'T', '$2', 'b', ],['function', 'T', '$2' ,'E', ],
             ['T', '$2', '=>', '$2', 'E'],['T', '$2' , 'E'],['T', '$2', 'b',],['T', '$2', ':' , 'T' , '=>', '$2', 'E'],
             ['T', '$2', ':', 'E'],['T', '$2', ':', 'T', 'b'],
            ]],
    
    ["M",[["M","$2"],["M","$2","M"],["M",";"],["M","M"]]]
    
# types

- $M -> \space type \space T \space \$2 \space b \space | \space type \space T \space \$2 \space inherits \space T \space \$2 \space b | \space type \space T \space b \space | \space type \space T \space inherits \space T \space b$

- $T -> \space new \space F \space$

# protocols

- $M -> protocol \space T \space \$2 \space b$
- $M -> protocol \space T \space \$2 \space extends \space T \space \$2 \space b$
- $M -> protocol \space T \space b$
- $M -> protocol \space T \space extends \space T \space b$

# vector

- $T -> [T||T] \space | \space [p] | \space T[T]$

# Procedence

 * Arithmetic Operations
 * Comparison Operations
 * Logical Operations
 * Assignment Operations
 * Control Flow Operations
 * Function Calls
 * Array and List Operations
 * String Operations
 * Object and Class Operations
 * Accessing properties (object.property)
 * Type Conversion

# Reduction Strategy -> GRADIENT PARSER

  This parser tries to model operator procedence using a grammar of the for $<G,P>$ where in $G$ exist pairs of the form $X-> Y$ where $X$ is non-terminal and $Y$ is a sentence . In $P$ if $\alpha\in P$ and $\beta\in P$ , such that $\aleph>\beta$ or $\beta<\alpha$ is the procedece of each operator.

## Strategy

    Shift: ++ , --
    Shift: -+
    Reduce: -+

if an `operator procedence` is that $\alpha>\beta$ for some $\alpha$ and $\beta$ then in string of the form $W \alpha W \beta W$ we reduce to $\alpha$ once we compare procedence between $\alpha$ and $\beta$ , if the case where oposite , $\alpha<\beta$ or $\alpha=\beta$ , we shift to next `token`

e.j : let x := y + 4;

The token are `let` , `x` , `:=` , `y` , `+` , `4` , `;` if the operator precedence is

- `+`
- `:=`
- `;`
- `$`

GRAMMAR :

- $S -> \$E\$$
- $E -> let  E$
- $E -> T := E$
- $E -> T := E$
- $E -> T + E$

we build the string in a default form `$` `let` `x` `:=` `y` `+` `4` `;` `$` and replace all non keywords and operator language to a default for `T`

The automaton iterate to state in that of token `:=` and compares procedence to `$`, as it is higher , we shift to the next operator token , in this case `+`. As can be seen , its higher so we shift again to operator token `;`. Reach this state, automaton determines it is time for reduction , so it `reduces` the string back to the operator that makes it do another `shift` . So it reduces to operator token `+` because it has a lower procedence , so the string remainds in the form:

|  `$` `let` `T` `:=` `T` `+` `E`   | $E -> T ;$

And again we go back to operator token `:=`:

|  `$` `let` `T` `:=` `E` | $E -> T + E$

| `$` `let` `E` | $E -> T := E$

| `$` `E` | $E -> let  E$

At this time we `shift` because we have reached `$`

| `$` `E` `$`

| `S` | $S -> \$E\$$

# HULK

In `HULK` programming languaje we used operator procedence in a form

### Procedence according to operator
  
- $[,(,\{$
- $],)$
- $c$
- $\}$
- $as$
- $\% , **$ , ^
- $*,/$
- $+,-$
- $<,>,>=,<=,==, ~ ,is$
- $\&,\|,!$
- $.$
- $=,+=,-=,/=,*=,--,:=,++,--$
- $let$
- $if$
- $elif$
- $else$
- $@,@@$
- $,$
- $=>$
- $in$
- $||$
- $;$
- $\$2$
- $\$1,\$3$
