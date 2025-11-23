# Elixir

https://github.com/livebook-dev/livebook

## Basic operation

```elixir
8 + 1   # 9
2 - 9   # -7
2 * 3   # 6
6 / 3   # 2.0 - division always return a float

1 / 3     # 0.33333
div(1, 3) # 0
div 1, 3  # 0
rem 1, 3  # 1
```

## Atoms

An atom is a literal, a constant with name. Atoms must start with a colon `:`
```elixir
:bonjour123
:"bon#jour"  # if non-alphanumeric characters, double quote only!
```

## Tuples

```elixir
{:abc, 123, :ff}
elem {:abc, 123, :ff}, 0  # get index 0
set_elem {:one, :two, :three}, 0, :four  # {:four, :two, :three}
```

## Lists

```elixir
[ 1, :two, [3, 4] ]
[head | tail] = [1, 2, 3]  # head is 1 and tail is [2, 3]
```

## Strings 

Strings and char lists (Strings are all encoded in UTF-8)  
double-quoted strings != single-quoted strings  
Double-quoted strings are represented as binaries, a sequence of bytes in UTF-8 encodings.  
Single-quoted strings are represented as a list of integers, because of this we refer to them as char lists.

```elixir
"héllò"             # utf-8

is_binary "hello"   # true
is_list 'hello'     # true
"hello" == 'hello'  # false

?a              # 97
[?a, ?b, ?c]    # 'abc' Elixir detects that all characters in the list are printable and returns the quoted representation.
[?a, ?b,  17]   # [97, 98, 17]
```

## Variables

Variables are used to store values. In Elixir variables start with a lower case letter or an underscore.

```elixir
answer = 42   # set variable
answer        # display variable
```

## Pattern Matching

In Elixir the equal sign `=` denotes a pattern matching operation.  
First the right hand side is evaluated and its value is matched against the pattern on the left hand side.  
The pattern match succeeds if the expression is compatible with the pattern, it fails otherwise.

```elixir
pattern = expression
{1, a} = {1, 2}     # bind a to 2
{a, b, c} = {1, 2}  # fail! because tuples have different sizes
```

Elixir lets you rebind variables, so it's actually possibly to do things like n = n + 1, if you want to match against the value of a variable use the `^` operator.

```elixir
x = 1   # 1
^x = 1  # 1
^x = 2  # fail!  WTF ????????????
```

## Functions

An anonymous function is created with the `fn` keyword

```elixir
f = fn(x) -> x * 2 end
f.(33)  # the dot . is required on anonymous functions

Enum.map([1, 2, 3], fn(x) -> x * 2 end) # Enum is the module, map is a function of Enum module
Enum.map [1, 2, 3], fn(x) -> x * 2 end  # parantheses are optional
```

The number of parameters in a function is referred as the arity of the function, and it's usual to refer to functions as `Enum.map/2`, This means that Enum.map has an arity of 2. 

```elixir
g = fn
    x, y when x > 0 -> x + y
    x, y -> x * y
end
g.(1,  5)   # 6
g.(-1, 5)   # -5
```
