.  repeat the last command
:reg  register


# Navigate - normal mode

## go to the first line of the file
:1
ctrl + home
gg

## go to the last line of the file
:%
ctrl + end
G

3G: jump to the third line
:123 - jump to the 123th line

= auto indent the line
gg=G auto indent the entire file

zz center the screen

# jump to the pair parenthese
%

# jump to next symbol
t(: jump before the next (
f(: jump to the next (
* jump to the next same word

# jump to the previous symbol
T(
F(
# jump to the previous symbol

ma: mark the position with the caracter 'a'
'a: jump to the marker 'a'

# search
/pattern find the next pattern
n next item
N previous item

?pattern find the previous pattern (reverse of /pattern)


# jump 

# (w)ord - jump to the next word
!= b

# 

ci( copy until the next character '('

:%s/find_pattern/replace_pattern/g  global find and replace

# Edit mode

every key can be combined with a number

## undo
u

## redo
CTRL + R

## (d)elete
dd: delete the line
5d: delete the 5 next lines
dw: delete word
d0: delete until the begining to the line
d%: delete the inner paranthese
dt(: delete everything until the next (

## (y)ank = copy

## (p)aste
p: after
P: before

## (r)eplace - instead of delete + insert

# (v)isual mode

# CTRL + v - visual block mode - column mode

