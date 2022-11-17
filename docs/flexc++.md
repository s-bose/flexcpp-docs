

Flexc++ (Version 2.11.00) User Guide

 #title,#author,#date {text-align: center;}
 figure {text-align: center;}
 img {vertical-align: center;}
 .XXfc {margin-left:auto;margin-right:auto;}
 .XXtc {text-align: center;}
 .XXtl {text-align: left;}
 .XXtr {text-align: right;}
 .XXvt {vertical-align: top;}
 .XXvb {vertical-align: bottom;}






---


Flexc++ (Version 2.11.00) User Guide
====================================



[Frank B. Brokken](mailto:f.b.brokken@rug.nl), 
 [Jean-Paul van Oosten](mailto:j.p.van.oosten@rug.nl),
 and (until 0.5.3) Richard Berendsen
--------------------------------------------------------------------------------------------------------------------------------------------


[University of Groningen](http://www.rug.nl/)
---------------------------------------------

2008-2022
---------


Table of Contents
=================


[Chapter 1: Introduction](flexc++01.html#l1)
--------------------------------------------



### [1.1: Running Flexc++](flexc++01.html#l2)



[1.1.1: Flexc++ options](flexc++01.html#l3)

### [1.2: Some simple examples](flexc++01.html#l4)



[1.2.1: A simple lexer file and main function](flexc++01.html#l5)
[1.2.2: An interactive scanner supporting command-line editing](flexc++01.html#l6)


[Chapter 2: Differences between flex and flexc++](flexc++02.html#l7)
--------------------------------------------------------------------



### [2.1: Format of the input file](flexc++02.html#l8)



[2.1.1: Definition section](flexc++02.html#l9)
[2.1.2: Rules section](flexc++02.html#l10)
[2.1.3: User code section](flexc++02.html#l11)

### [2.2: Patterns](flexc++02.html#l12)


### [2.3: Generated files](flexc++02.html#l13)


### [2.4: Comment](flexc++02.html#l14)


### [2.5: Members and macros](flexc++02.html#l15)


### [2.6: Multiple input streams](flexc++02.html#l16)



[Chapter 3: Format of the input file](flexc++03.html#l17)
---------------------------------------------------------



### [3.1: Definitions section](flexc++03.html#l18)



[3.1.1: Directives](flexc++03.html#l19)

### [3.2: Rules section](flexc++03.html#l20)


### [3.3: Comment](flexc++03.html#l21)


### [3.4: Patterns](flexc++03.html#l22)


### [3.5: Character constants](flexc++03.html#l23)


### [3.6: Actions](flexc++03.html#l24)


### [3.7: Start conditions (Mini scanners)](flexc++03.html#l25)



[3.7.1: Notation details](flexc++03.html#l26)

### [3.8: Members](flexc++03.html#l27)


### [3.9: Handling input your own way](flexc++03.html#l28)



[Chapter 4: Generated files](flexc++04.html#l29)
------------------------------------------------



### [4.1: Multiple input streams](flexc++04.html#l30)



[Chapter 5: Pre-loading input lines](flexc++05.html#l31)
--------------------------------------------------------



### [5.1: Using start conditions to pre-load input lines](flexc++05.html#l32)


### [5.2: Wrapping input streams](flexc++05.html#l33)



[5.2.1: The class ScannerStreambuf](flexc++05.html#l34)
[5.2.2: Illustration](flexc++05.html#l35)


[Chapter 6: Technical documentation](flexc++06.html#l36)
--------------------------------------------------------



### [6.1: Notation, Terminology](flexc++06.html#l37)



[6.1.1: Example of LOP-patterns](flexc++06.html#l38)

### [6.2: The parser](flexc++06.html#l39)


### [6.3: Start Conditions and the class StartConditions](flexc++06.html#l40)


### [6.4: Code (action) blocks](flexc++06.html#l41)


### [6.5: The class State](flexc++06.html#l42)


### [6.6: States](flexc++06.html#l43)


### [6.7: Rules and the class Rule](flexc++06.html#l44)


### [6.8: Converting REs to Patterns](flexc++06.html#l45)



[6.8.1: The class CharClass](flexc++06.html#l46)
[6.8.2: The class Interval](flexc++06.html#l47)

### [6.9: Patterns](flexc++06.html#l48)


### [6.10: Patterns using the lookahead operator (LOP)](flexc++06.html#l49)



[6.10.1: The parser recognizing LOP patterns](flexc++06.html#l50)

[6.10.1.1: Start conditions used by standard LOP patterns](flexc++06.html#l51)

[6.10.2: Pattern constructors used with LOP patterns](flexc++06.html#l52)
[6.10.3: Adding (LOP-)rules](flexc++06.html#l53)
[6.10.4: After parsing: adding LOP start conditions](flexc++06.html#l54)
[6.10.5: After parsing: handling LOP rules](flexc++06.html#l55)

### [6.11: Ranges](flexc++06.html#l56)


### [6.12: The class DFAs](flexc++06.html#l57)


### [6.13: The DFA](flexc++06.html#l58)



[6.13.1: DFA::build: From NFA to DFA](flexc++06.html#l59)
[6.13.2: Removing duplicate rows](flexc++06.html#l60)

### [6.14: The rows of the DFA: DFAROW](flexc++06.html#l61)



[6.14.1: Associating a DFARow with a Rule](flexc++06.html#l62)

### [6.15: Finding non-viable rules](flexc++06.html#l63)


### [6.16: Generating Code](flexc++06.html#l64)



[6.16.1: The range-table](flexc++06.html#l65)
[6.16.2: The DFAs](flexc++06.html#l66)

### [6.17: Run-time operations](flexc++06.html#l67)



[6.17.1: Handling BOL-rules](flexc++06.html#l68)

### [6.18: Run-time handling of LOP-patterns](flexc++06.html#l69)


### [6.19: Reflex: refreshing flexc++](flexc++06.html#l70)





---











