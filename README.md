# The HULK Language

**HULK** (**H**avana **U**niversity **L**anguage for **K**ompilers) is a didactic, type-safe, object-oriented, and incremental programming language designed for the course Introduction to Compilers in the Computer Science major at the University of Havana.

A simple “Hello World” in HULK looks like this:

```hulk
print("Hello World");
```

In a bird’s eye view, HULK is an object-oriented programming language with simple inheritance, polymorphism, and encapsulation at the class level. Also, in HULK, it is possible to define global functions outside the scope of all classes. It is also possible to define a single global expression that constitutes the entry point to the program.
Most of the syntactic constructions in HULK are expressions, including conditional instructions and cycles. HULK is a statically typed language with optional type inference, which means that some (or all) parts of a program can be annotated with types, and the compiler will verify the consistency of all operations.

## A Didactic Language
The HULK language has been designed as a mechanism for learning and evaluating a college course about compilers. For this reason, certain language design decisions respond more to didactic questions than to theoretical or pragmatic questions. An illustrative example is the inclusion of a single basic numerical type. In practice, programming languages have several numeric types (int, float, double, decimal) to cover the wide range of trade-offs between efficiency and expressivity. However, from the didactic point of view, it is enough complexity to have to deal with a numerical type, and the inclusion of others does not bring anything new from our point of view.
Another important decision is the static typing with type inference, which will be explained later in detail. The motivation behind this feature is to allow students to first implement an evaluator for the language and then worry about type verification. Likewise, the decision to have global expressions, global functions, and classes responds to the need to introduce various elements of language little by little. By having global expressions, it is possible to implement an expression interpreter without needing to solve context-sensitive problems. Later, students can implement functions and finally the object-oriented features. In this way, students can learn on the fly as they add characteristics to the language, always having a valid subset of the language implemented.

## An Incremental Language

As its name indicates, HULK is a huge language. Actually, the HULK language really is not a single programming language but a set of programming languages. That is, HULK is designed as a set of layers, each with new language features that add increasingly more complex functionalities on top of the previous layers. It starts with a basic syntax for expressions, then global functions, and then a unified type system with simple inheritance. Afterwards, HULK grows to contain arrays, delegates, type inference, iterators, among other characteristics. All these language features have been designed to be compatible with each other. Furthermore, each language feature clearly describes which other language features it depends on.
This design has been conceived to allow the use of HULK at a wide range of learning levels. As a language of expressions and functions, it is useful for introductory courses on parsing and basic compilation techniques. Object orientation introduces a whole universe of semantic complexities; however, the HULK type system is simple enough to illustrate the most common problems in semantic type verification. Vectors introduce problems related to memory management while anonymous functions and iterators fundamentally present problems of transpilation and code generation. The inference of types and verification of null-safety is an exercise in logical inference that can be used in advanced courses. The idea is that each course defines its objectives of interest and can use an appropriate subset of HULK to illustrate and evaluate them.

## BANNER: Intermediate Representation

Even though HULK can be defined without specific compilation details, we also provide a didactic 3-address code for intermediate representation that is convenient to use with HULK. For obvious reasons, it’s called BANNER – Basic 3-Adress liNear iNtEmediate Representation.


# The Hitchhiker's Guide to Compilers - Expressions

HULK is ultimately an expression-based language. Most of the syntactic constructions in HULK are expressions, including the body of all functions, loops, and any other block of code.
The body of a program in HULK always ends with a single global expression (and, if necessary, a final semicolon) that serves as the entry point of the program. This means that a program in HULK can consist of just one global expression.

### Example Programs
A valid program in HULK could be:
```
42;
```

This program has no side effects. A slightly more complicated program that performs an action is:
```
print(42);

```

## Arithmetic Expressions

HULK defines three types of literal values:
Numbers
Strings
Booleans
Numbers are 32-bit floating-point and support all basic arithmetic operations with the usual semantics:
1. $+$ (addition)
2. $-$ (subtraction)
3. $*$ (multiplication)
4. $\div$ (floating-point division)
5. $^$ (power)

The following is a valid HULK program that computes and prints the result of an arithmetic 
expression:

```
print((((1 + 2) ^ 3) * 4) / 5);
```

All usual syntactic and precedence rules apply.

## Strings

String literals in HULK are defined within enclosed double-quotes ("), such as:
```
print("Hello World");
```

A double-quote can be included literally by escaping it:
```
print("The message is \"Hello World\"");
```

Other escaped characters include:

1. `\n` for line endings
2. `\t` for tabs

Strings can be concatenated with other strings (or the string representation of numbers) using 

the $@$ operator:
```
print("The meaning of life is " @ 42);
```

## Built-in Math Functions and Constants

HULK includes several built-in math functions:

```
sqrt(<value>): Computes the square root of a value.
sin(<angle>): Computes the sine of an angle in radians.
cos(<angle>): Computes the cosine of an angle in radians.
exp(<value>): Computes 
log(<base>, <value>): Computes the logarithm of a value in a given base.
rand(): Returns a random uniform number between 0 and 1 (both inclusive).

```

HULK also includes two global constants:
```
PI
E
```

These represent the floating-point values of these mathematical constants. Functions can be nested, allowing for expressions like:

```
print(sin(2 * PI) ^ 2 + cos(3 * PI / log(4, 64)));
```

Function invocation is also an expression in HULK, enabling you to mix arithmetic expressions and mathematical functions freely.

## Expression Blocks

Anywhere an expression is allowed (or almost), you can also use an expression block, which is a series of expressions enclosed in curly braces ({ and }), separated by semicolons (;).
A trivial usage of expression blocks could look like this:
```
{
    print(42);
    print(sin(PI/2));
    print("Hello World");
}
```

When using an expression block instead of a single expression, it is often not necessary to end with a semicolon (;), but it is not erroneous to do so either.

##  Functions

###  Inline Functions

###  Full-form Functions

**Functions**

HULK also lets you define your own functions (of course!). A program in HULK can have an arbitrary number of functions defined before the final global expression (or expression block).

A function’s body is always an expression (or expression block), hence all functions have a return value (and type), that is, the return value (and type) of its body.

### Inline Functions

The easiest way to define a function is the inline form. Here’s an example:

```hulk
function tan(x) => sin(x) / cos(x);
```

An inline function is defined by an identifier followed by arguments between parentheses, then the => symbol, and then a simple expression (not an expression block) as body, ending in ;.
In HULK, all functions must be defined before the final global expression. All these functions live in a single global namespace, hence it is not allowed to repeat function names. Similarly, there are no overloads in HULK (at least in “basic” HULK).
Finally, the body of any function can use other functions, regardless of whether they are defined before or after the corresponding function. Thus, the following is a valid HULK program:

```
function cot(x) => 1 / tan(x);
function tan(x) => sin(x) / cos(x);

print(tan(PI) ** 2 + cot(PI) ** 2);

```

And of course, inline functions (and any other type of function) can call themselves recursively.

## Full-form Functions

Since inline functions only allow for a single expression as body (as complex as that may be), HULK also allows full-form functions, in which the body is an expression block.
Here’s an example of a rather useless function that prints four times:

```
function operate(x, y) {
    print(x + y);
    print(x - y);
    print(x * y);
    print(x / y);
}

```

Note that the following form is discouraged for stylistic reasons:

```
function id(<args>) => {
    <...>
}

```

That is, you should either use the inline form with => and a simple expression, or the full form with {} and an expression block.


## Variables

Variables in HULK are lexically-scoped, which means that their scope is explicitly defined by the syntax. You use the `let` expression to introduce one or more variables and evaluate an expression in a new scope where those variables are defined.

The simplest form is introducing a single variable and using a single expression as body:

```hulk
let msg = "Hello World" in print(msg);
```

Here, msg is a new symbol that is defined only within the expression that goes after in.

## Multiple Variables
The let expression admits defining multiple variables at once like this:

```
let number = 42, text = "The meaning of life is" in
    print(text @ number);

```

This is semantically equivalent to the following long form:

```
let number = 42 in
    let text = "The meaning of life is" in
        print(text @ number);

```

As you can notice, let associates to the right, so the previous is also equivalent to:

```

let number = 42 in (
    let text = "The meaning of life is" in (
            print(text @ number)
        )
    );

```

## Scoping Rules

Since the binding is performed left-to-right (or equivalently starting from the outer let), and every variable is effectively bound in a new scope, you can safely use one variable when defining another:

```
let a = 6, b = a * 7 in print(b);

```

Which is equivalent to (and thus valid):

```
let a = 6 in
    let b = a * 7 in
        print(b);

```

## Expression Block Body

You can also use an expression block as the body of a let expression:

```
let a = 5, b = 10, c = 20 in {
    print(a + b);
    print(b * c);
    print(c / a);
}
```

As we said before, semicolons (;) are seldom necessary after an expression block, but they are never wrong.

## The Let Return Value
As with almost everything in HULK, let is an expression, so it has a return value, which is obviously the return value of its body. This means the following is a valid HULK program:

```
let a = (let b = 6 in b * 7) in print(a);
```

Or more directly:

```
print(let b = 6 in b * 7);
```

This can be of course nested ad infinitum.

## Redefining Symbols
In HULK, every new scope hides the symbols from the parent scope, which means you can redefine a variable name in an inner let expression:

```
let a = 20 in {
    let a = 42 in print(a);
    print(a);
}
```

The previous code prints 42 then 20, since the inner let redefines the value of a inside its scope, but the value outside is still the one defined by the outer let.
And because of the scoping rules, the following is also valid:

```
let a = 7, a = 7 * 6 in print(a);
```

Which is equivalent to:

```
let a = 7 in
    let a = 7 * 6 in
        print(a);
```

## Destructive Assignment
Most of the time in HULK you won’t need to overwrite a variable, but there are cases where you do. In those cases, you can use the destructive assignment operator :=, like this:

```
let a = 0 in {
    print(a);
    a := 1;
    print(a);
}
```

The previous program prints 0 and then 1, since the value of a is overwritten before the second print. This is the only way in which a variable can be written to outside of a let.
As you would expect, the := operator defines an expression too, which returns the value just assigned, so you can do the following:

```
let a = 0 in
    let b = a := 1 in {
        print(a);
        print(b);
    };
```

This is useful if you want to evaluate a complex expression to both test it (e.g., to see if it's greater than zero) and store it for later use.

## Rules for Naming Identifiers
Variables (and identifiers in general) in HULK can be named with any sequence of alphanumeric characters, plus underscore _, but must always begin with a letter (not a digit or _). Hence, the following are all valid identifiers:
- x
- x0
- x_0
- lowercase
- TitleCase
- snake_case
- camelCase

The following are invalid HULK identifiers:
- _x
- x+y
- some method
- 8ball
And many others, of course!
Since starting with an underscore _ is invalid in HULK, you will notice that when we talk about transpilation in HULK, variables and identifiers in transpiled code always start with _.

## Conditionals

The `if` expression allows evaluating different expressions based on a condition:

```hulk
let a = 42 in if (a % 2 == 0) print("Even") else print("Odd");
```

Since if is itself an expression, returning the value of the branch that evaluated true, the previous program can be rewritten as follows:

```
let a = 42 in print(if (a % 2 == 0) "Even" else "Odd");
```

Conditions are just expressions of boolean type. The following are the valid boolean expressions:
Boolean literals: true and false.
Arithmetic comparison operators: <, >, <=, >=, ==, !=, with their usual semantics.
Boolean operators: & (and), | (or), and ! (not) with their usual semantics.

## Expression Blocks in Conditionals

The body of the if or the else part of a conditional (or both) can be an expression block as well:

```
let a = 42 in
    if (a % 2 == 0) {
        print(a);
        print("Even");
    }
    else print("Odd");
```

## Multiple Branches

The if expression supports multiple branches with the elif construction, which introduces another conditioned branch:

```
let a = 42, mod = a % 3 in
    print(
        if (mod == 0) "Magic"
        elif (mod % 3 == 1) "Woke"
        else "Dumb"
    );
```

## Loops

HULK defines two kinds of loops: the `while` expression and the `for` expression. Both loop constructions are expressions, returning the value of the body.

### The While Loop

A `while` loop evaluates a condition and its body while the condition is true. The body can be a simple expression or an expression block:

```hulk
let a = 10 in while (a >= 0) {
    print(a);
    a := a - 1;
}
```

Since the return value of the while loop is the return value of its expression body, it can often be used directly as the body of a function:

```
function gcd(a, b) => while (a > 0)
    let m = a % b in {
        b := a;
        a := m;
    };
```

### The For Loop
A for loop iterates over an iterable of elements of a certain type. We will talk about iterables later on, but for now, it suffices to say that if some expression evaluates to a collection, then the for loop can be used to iterate it.
For example, the built-in range(< start >, < end >) function evaluates to an iterable of numbers between < start > (inclusive) and < end > (non-inclusive):

```
for (x in range(0, 10)) print(x);
```

The for loop is semantically and operationally equivalent to the following:

```
let iterable = range(0, 10) in
    while (iterable.next())
        let x = iterable.current() in
            print(x);
```

In fact, what the reference implementation of the HULK compiler does in for loops is to transpile them into their while equivalent. This also effectively means that, just like the while loop, the for loop returns the last value of its body expression.

Types
HULK is ultimately an object-oriented language with simple inheritance and nominal typing. It also has features of structural typing via protocols, which support language features such as iterables, which we will explain later.

This section explains the basics of HULK’s nominal typing system.

A type in HULK is basically a collection of attributes and methods, encapsulated under a type name. Attributes are always private, which means they can’t be read or writen to from any code outside the type in which they are defined (not even inheritors), while methods are always public and virtual.

# Declaring types
A new type is declared using the type keyword followed by a name, and a body composed of attribute definitions and method definitions. All attributes must be given an initialization expression. Methods, like functions, can have a single expression or an expression block as body;

```
type Point {
    x = 0;
    y = 0;

    getX() => self.x;
    getY() => self.y;

    setX(x) => self.x := x;
    setY(y) => self.y := y;
}
```

The body of every method is evaluated in a namespace that contains global symbols plus an especial symbol named self that references the current instance. The self symbol is not a keyword, which means it can be hidden by a let expression, or by a method argument.

However, when referring to the current instance, self is not a valid assignment target, so the following code should fail with a semantic error:

```
type A {
    // ...
    f() {
        self := new A(); // <-- Semantic error, `self` is not a valid assignment target
    }
}
```

## Instantiating types
To instantiate a type you use the keyword new followed by the type name:

```
let pt = new Point() in
    print("x: " @ pt.getX() @ "; y: " @ pt.getY());
```

As you can see, type members are accessed by dot notation (instance.member).

You can pass arguments to a type, that you can use in the initialization expressions. This achieves an effect similar to having a single constructor.

```
type Point(x, y) {
    x = x;
    y = y;

    // ...
}
```

Then, at instantiation time, you can pass specific values:

```
let pt = new Point(3,4) in
    print("x: " @ pt.getX() @ "; y: " @ pt.getY());
```

Each attribute initialization expression is evaluated in a namespace that contains the global symbols and the type arguments, but no the self symbol. This means you cannot use other attributes of the same instance in an attribute initialization expression. This also means that you cannot assume any specifc order of initialization of attributes.

## Inheritance

Types in HULK can inherit from other types. The base of the type hierarchy is a type named Object which has no public members, which is the type you implicitely inherit from by default. To inherit from a specific type, you use the inherits keyword followed by the type name:

```
type PolarPoint inherits Point {
    rho() => sqrt(self.getX() ^ 2 + self.getY() ^ 2);
    // ...
}
```

By default, a type inherits its parent type arguments, which means that to construct a PolarPoint you have to pass the x and y that Point is expecting:

```
let pt = new PolarPoint(3,4) in
    print("rho: " @ pt.rho());
```

If you want to define a different set of type arguments, then you have to provide initialization expressions for the parent type at the declaration:

```
type PolarPoint(phi, rho) inherits Point(rho * sin(phi), rho * cos(phi)) {
    // ...
}
```

During construction, the expressions for type arguments of the parent are evaluated in a namespace that contains global symbols plus the type arguments of the inheritor. Like before, you cannot assume a specific order of evaluation.

In HULK, the three builtin types (Number, String, and Boolean) implicitely inherit from Object, but it is a semantic error to inherit from these types.

## Polymorphism

All type methods in HULK are virtual by definition, and can be redefined by an inheritor provided the exact same signature is used:

```
type Person(firstname, lastname) {
    firstname = firstname;
    lastname = lastname;

    name() => self.firstname @@ self.lastname;
}
```

NOTE: @@ is equivalent to @ "  " @. It is a shorthand to insert a whitespace between two concatenated strings. There is no @@@ or beyond, we’re not savages.

```
type Knight inherits Person {
    name() => "Sir" @@ base();
}

let p = new Knight("Phil", "Collins") in
    print(p.name()); // prints 'Sir Phil Collins'
```

The base symbol in every method refers to the implementation of the parent (or the closest ancestor that has an implementation).

# Type Checking

HULK is a statically-typed language with optional type annotations. So far, you haven’t seen any because HULK has a powerful type inference system, which we will talk about later on. However, all symbols in HULK have a static type, and all programs in HULK are statically checked during compilation.

Type annotations can be added anywhere a symbol is defined, that is:

- In variable declarations with `let` expressions;
- In function or method arguments and return type;
- In type attributes; and,
- In type arguments.

Let’s see an example of each case.

### Typing Variables

Variables can be explicitly type-annotated in `let` expressions with the following syntax:

```hulk
let x: Number = 42 in print(x);
```
The type checker will verify that the type inferred for the initialization expression is compatible with (formally, conforms to) the annotated type.

## Typing Functions and Methods
All or a subset of a function’s or method’s arguments, and its return value, can be type-annotated with a similar syntax:

```
function tan(x: Number): Number => sin(x) / cos(x);
```

On the declaration side, the type checker will verify that the body of the method uses the types in a way that is consistent with their declaration. The exact meaning of this consistency is defined in the section about type semantics. The type checker will also verify that the return type of the body conforms to the annotated return type.
On the invocation side, the type checker will verify that the values passed as parameters conform to the annotated types.
Inside methods of a type T, the implicitly defined self symbol is always assumed as if annotated with type T.

## Typing Attributes and Type Arguments

In type definitions, attributes and type arguments can be type-annotated as follows:

```
type Point(x: Number, y: Number) {
    x: Number = x;
    y: Number = y;

    // ...
}
```

The type checker will verify that type arguments are used consistently inside attribute initialization expressions and that the inferred type for each attribute initialization expression conforms to the attribute annotation.

## Type Conforming

The basic type relation in HULK is called conforming (<=). A type T1 is said to conform to another type T2 (written as T1 <= T2) if a variable of type T2 can hold a value of type T1 such that every possible operation that is semantically valid with T2 is guaranteed to be semantically valid with T1.

In general, this means that the type checker will verify that the inferred type for any expression conforms to the corresponding type declared for that expression (e.g., the type of a variable or the return type of a function).

The following rules provide an initial definition for the conforming relationship. The formal definition is given in the section about type semantics:

Every type conforms to Object.
Every type conforms to itself.

If T1 inherits T2, then T1 conforms to T2.
If T1 conforms to T2 and T2 conforms to T3, then T1 conforms to T3.

The only types that conform to Number, String, and Boolean, are respectively those same types.
Types in HULK form a single hierarchy rooted at Object. In this hierarchy, the conforming relationship is equivalent to the descendant relationship. Thus, if T1 conforms to T2, that means that T1 is a descendant of T2 (or trivially the same type). Thus, we can talk about the lowest common ancestor of a set of types ( T_1, T_2, \ldots, T_n ), which is the most specific type ( T ) such that all ( T_i ) conform to ( T ). When two types are in different branches of the type hierarchy, they are effectively incomparable.
NOTE: This conforming relationship is extended when we add protocols.

## Testing for Dynamic Types

The is operator allows testing an object to check whether its dynamic type conforms to a specific static type.

```
type Bird {
    // ...
}

type Plane {
    // ...
}

type Superman {
    // ...
}

let x = new Superman() in
    print(
        if (x is Bird) "It's a bird!"
        elif (x is Plane) "It's a plane!"
        else "No, it's Superman!"
    );
```

In general, before the is operator, you can put any expression, not just a variable.

## Downcasting
You can use the as operator to downcast an expression to a given static type. The result is a runtime error if the expression is not a suitable dynamic type, which means you should always test if you’re unsure:

```
type A {
    // ...
}

type B inherits A {
    // ...
}

type C inherits A {
    // ...
}

let x: A = if (rand() < 0.5) new B() else new C() in
    if (x is B)
        let y: B = x as B in {
            // you can use y with static type B
        }
    else {
        // x cannot be downcasted to B
    }
```

# Type Inference

Since every program in HULK is statically type-checked, and type annotations are optional in most cases, this means that HULK infers types for most of the symbols in a program.

Because the problem of type inference is computationally complex, and ultimately unsolvable in the general case, the HULK reference definition doesn’t give precise semantics about how the type inferer must work. Rather, we will give only a set of minimal constraints that the type inferer must assert if a type is inferred at all for a given symbol, or otherwise it must fail to infer types.

## Type Inference vs Type Checking

The type inferer works before the type checker and assigns type annotations to all symbols that are not explicitly annotated, and to all the expressions. Afterwards, the type checker verifies that all semantic rules are valid.

Thus, even if a program is fully annotated, the type inferer still needs to work since it needs to infer the type of all expressions. When some symbols are not explicitly annotated, the type inferer must also assign types for them.

Hence, there are two different moments when a semantic error can be reported. First, if the type inferer cannot infer the type of some symbol, a semantic error will be thrown to indicate to the programmer that some symbol must be explicitly typed. Second, if the type inferer finishes without errors, the type checker will verify that all types are consistent and will report a semantic error if there is some incompatibility.

## Type Inference of Expressions

The first task of the type inferer is to infer the runtime type of any expression that appears in a HULK program. This process is performed bottom-up, starting from atomic sub-expressions (e.g., literals) and working up the AST. The exact rules for type inference of expressions are given in the section about type semantics, but an intuitive introduction can be provided at this point.

Literals are the easiest to type-infer because their type comes directly from the parser. Arithmetic expressions are also easy because their type is always `Number`. Likewise, string and boolean operators are straightforward.

The type of complex expressions that have an expression body is determined by the type of the body. This is the case for `let`, `while`, and `for`. The type of an expression block is the type of the last expression of the block. The type of a function or method invocation is the type of its body. The type of expressions that have more than one branch (like `if`) is the lowest common ancestor of the types of each branch or ultimately `Object`.

## Type Inference of Symbols

Once all expressions have been type-inferred, the type inferer will attempt to assign a type to each symbol declaration that is not explicitly annotated. Instead of providing an exact algorithm, we will define a set of constraints that the type inferer must satisfy whenever it succeeds in assigning a type.

Specific implementations of HULK can choose different methods to attempt the type inference of symbols. According to the order in which symbols are processed and the sophistication of each method, some implementations may succeed where others fail. However, if two type inference algorithms are correct, they must agree on all types for which both succeed in inference.

These are the constraints a type inference algorithm must satisfy to be correct; otherwise, it must report a failed inference:

- In a `let` expression, whenever a variable is not type-annotated, the type inferer must assign a type for the variable that is equivalent to the type inferred for its initialization expression.
- Similarly, in an attribute declaration that is not type-annotated, the type inferer must assign a type that is equivalent to the type inferred for its initialization expression.
- In a function or method, whenever an argument is not type-annotated, the type inferer must assign the lowest (most specific) type that would be consistent with the use of that argument in the method or function body. If more than one type in different branches of the type hierarchy would be consistent, the type inferer must fail.
- Similarly, in a type argument, the type inferer must assign the lowest type that is consistent with the use of that argument in all attribute initialization expressions where it is referenced.

If a type inferer satisfies those constraints, we will say it is sound. This means that, for example, the simplest sound strategy for type inference is to infer types for all expressions and fail for all symbols. We will call this the basic inference strategy.

### Examples of Type Inference

These are some programs where a sufficiently sophisticated type inference strategy should work.

In the following program, the type of variable `x` should be inferred as `Number` because the type of `42` is trivially `Number`:

```hulk
let x = 42 in print(x);
```

In this following function, the type of argument n should be inferred as Number because it is the only possible type where arithmetic operators (i.e., +) are defined since there is no operator overloading in HULK:

```
function fib(n) => if (n == 0 | n == 1) 1 else fib(n - 1) + fib(n - 2);
```

For similar reasons, in this following function, the argument x should be inferred as Number. Likewise, variable f should be inferred as Number because its initialization expression is a literal Number.

```
function fact(x) => let f = 1 in for (i in range(1, x + 1)) f := f * i;
```

# Protocols

Protocols are special types that support a limited form of structural typing in HULK. The difference between structural and nominal typing in HULK is that the latter is explicit while the former is implicitly defined. That is, a type doesn’t need to explicitly declare that it conforms to a protocol.

Protocols have a syntax similar to that of types, except that they only have method declarations and no body, only signatures. Hence, protocols define the methods that a type must have in order to support some operation.

Protocols don’t exist at runtime; they are a compile-time-only concept that helps in writing more flexible programs. After type checking, all information about protocols can be safely removed.

## Defining Protocols

A protocol is defined with the keyword `protocol` followed by a collection of method declarations:

```hulk
protocol Hashable {
    hash(): Number;
}
```

A protocol can have any number of method declarations. For obvious reasons, all method declarations in protocol definitions must be fully typed, as it is impossible to infer any types since they have no body.

A protocol can extend another protocol by adding new methods but never overriding (since there is no actual body) or removing any method (although you can override the types of some method arguments or return types provided with some restrictions explained below).

```
protocol Equatable extends Hashable {
    equals(other: Object): Boolean;
}
```

# Implementing Protocols

A type implements a protocol implicitly, simply by having methods with the right signature. There is no need to explicitly declare which types implement which protocols.
Thus, you can annotate a variable or argument with a protocol type, and the type checker will correctly verify the consistency of both the method body and the invocation.

```
type Person {
    // ...

    hash(): Number {
        // ...
    }
}

let x: Hashable = new Person() in print(x.hash());
```

Anywhere you can annotate a symbol with a type (variables, attributes, function, method and type arguments, and return values), you can also use a protocol. For the purpose of type inference, protocols are treated as types.

## Variance in Protocol Implementation

In order to implement a protocol, a type doesn’t necessarily have to match the exact signature of the protocol. Instead, method and type arguments are considered contravariant, and return values covariant. This means that arguments can be of the same type or higher, and the return values of the same type or lower than as defined in the protocol.
Similarly, when you extend a protocol, you can override some of the methods as long as you respect the variance constraints.

## Conforming with Protocols

More formally, protocols extend the notion of type conforming by adding the following rules:

- A type T conforms to a protocol P if T has all the methods defined in P with the appropriate types (respecting the variance constraints explained before).

- If a protocol P1 extends a protocol P2, then trivially ( P1 \leq P2 ).
- A protocol ( P1 ) also conforms to another protocol ( P2 ) if any type that conforms to ( P1 ) would also conform to ( P2 ), even if there is no explicit extension declared.

# Iterables

An iterable in HULK is any object that follows the iterable protocol, which is defined as follows:

```hulk
protocol Iterable {
    next(): Boolean;
    current(): Object;
}
```

An example of an iterable is the built-in range function, which returns an instance of the built-in Range type, defined as follows:

```
type Range(min: Number, max: Number) {
    min = min;
    max = max;
    current = min - 1;

    next(): Boolean => (self.current := self.current + 1) < max;
    current(): Number => self.current;
}
```

Notice that since protocols are covariant in the return types of the methods, the Range type correctly implements the Iterable protocol.

## Using Iterables with the For Loop

As explained in the loops section, the for loop works with the Iterable protocol, which means you can apply for on any instance of a type that implements the protocol.
At compile-time, for is transpiled to code that is equivalent but explicitly uses the Iterable protocol members.

For example, the code:

```
for (x in range(0, 10)) {
    // code that uses `x`
}
```

is transpiled to:

```
let iterable = range(0, 10) in
    while (iterable.next())
        let x = iterable.current() in {
            // code that uses `x`
        }
```

This transpilation guarantees that even though the Iterable protocol defines the current method with a return type of Object, when you use a for loop, you will get the exact covariant type inferred in x.

As a matter of fact, due to the transpilation process, the Iterable protocol itself is not even necessary since nowhere is a symbol annotated as Iterable. However, the protocol is explicitly defined as a built-in type so that you can use it if you need to annotate a method to receive a black-box iterable.

Keep in mind, though, that when you annotate something explicitly as Iterable, you are effectively forcing the type inferrer to assign Object as the type of the iteration variable (x in this example). This is one of the reasons it is often better to let HULK infer types than annotating them yourself.

## Typing Iterables

Since in the Iterable protocol we can only define (at this point) the return value of current() as Object, it is cumbersome to type arguments of a function or method as Iterable, because doing so will force you to downcast the elements to a desired type.

For this reason, HULK allows a special syntax for typing iterables of a specific type ( T ) using the format ( T* ):

```
function sum(numbers: Number*): Number =>
    let total = 0 in
        for (x in numbers)
            total := total + x;
```

What happens under the hood is that when you use ( T* ) anywhere in a HULK program, the compiler will insert an implicit protocol definition that looks like this:

```
protocol Iterable_T extends Iterable {
    current(): T;
}
```

Since protocols can be extended by overriding some methods with the correct variance constraints, the previous code will compile correctly.

## Implementing Collections

The iterable protocols defined so far encapsulate the concept of making a single iteration over a sequence of elements. In contrast, most collection types you will define allow for multiple iterations, even simultaneously, over the same sequence of elements.
To accommodate this kind of behavior, we can define an enumerable protocol that simply provides one method to create an iterable for one specific iteration every time that is needed:

```
protocol Enumerable {
    iter(): Iterable;
}
```


With this protocol defined, the for loop is extended such that when used with an enumerable instead of directly an iterable, it will transpile to slightly different code:

```
let iterable = enumerable.iter() in
    while (iterable.next())
        let x = iterable.current() in {
            // ..
        }
```

# Vectors

The built-in vector type provides a simple but powerful abstraction for creating collections of objects of the same type. In terms of functionality, a vector is close to plain arrays as defined in most programming languages. Vectors implement the iterable protocol so they can be iterated with a `for` syntax.

Vectors in HULK can be defined with two different syntactic forms: explicit and implicit.

## Explicit Syntax

An explicit vector of `Number`, for example, can be defined as follows:

```hulk
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] in
    for (x in numbers)
        print(x);
```

Because vectors implement the iterable protocol, you can explicitly find next and current methods in case you ever need them. Besides that, vectors also have a size(): Number method that returns the number of items in the vector.

Vectors also support an indexing syntax using square brackets [], as in the following example:

```
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] in print(numbers);
```

## Implicit Syntax

An implicit vector can be created using what we call a generator pattern, which is always an expression.

Here’s one example:

```
let squares = [x^2 | x in range(1, 10)] in print(x);
// prints 1, 4, 9, 16, ...
```

In general, the syntax has the form [<expr> | <symbol> in <iterable>], where <expr> is run in a new scope where <symbol> is iteratively bound to each element in the vector.

## Typing Vectors

Since vectors are iterables, you can safely pass a vector as an argument to a method that expects an iterable:

```
function sum(numbers: Number*): Number =>
    let total = 0 in
        for (x in numbers)
            total := total + x;

let numbers = [1, 2, 3, 4, 5] in
    print(sum(numbers));
```

However, inside sum, you cannot use the indexing operator [] or the size method because the argument is typed as an iterable and not explicitly as a vector. To fix this, HULK provides another special syntax for vectors using the T[] notation:

```
function mean(numbers: Number[]): Number =>
    let total = 0 in {
        for (x in numbers)
            total := total + x;

        // here `numbers` is known to be a vector
        total / numbers.size();
    };

let numbers = [1, 2, 3, 4, 5] in
    print(mean(numbers));
```

Like with iterables, what happens under the hood is that the compiler implicitly defines a type with the following structure:

```
type Vector_T {
    size() {
        // implementation of size ...
    }

    iter(): Iterable_T {
        // implementation of iter
    }
}
```

# END