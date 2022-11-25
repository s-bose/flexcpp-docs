
---


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++01.html)* [Next Chapter](flexc++03.html)




---



Chapter 2: Differences between flex and flexc++
===============================================



Although **flexc++** tries to be as compatible as possible with **flex**(1), there
are some noteworthy differences. This chapter provides a quick overview for
the users already familiar with flex.


2.1: Format of the input file
-----------------------------


 In **flex**(1) initializating code can be provided in the definition section
(see section [3.1](flexc++03.html#definitionsection)), and pre-match code can be provided as
the first lines in the rules section.

**Flexc++** does not support code blocks. Since **flexc++** generates a class with
appropriate header files, initialization code can be activated bij **flexc++**'s
constructor, code to be executed when `lex` is called can be placed in the
member `lex`'s body, just before calling `lex_`, and `Scanner::preCode`
can be provided with any required pre-match code. See also [generated
files 2.3](flexc++02.html#files) below.

**Flexc++** also does not support a trailing `user code' section, where additional
code can be placed to be copied verbatim to the source file. Again, the
`Scanner` class approach offers preferable means for adding user code to the
scanner. 

Sections [2.1.1](flexc++02.html#diffdef), [2.1.2](flexc++02.html#diffrules) and [2.1.3](flexc++02.html#diffusercode) cover 
items which are no longer supported in **flexc++**, offering alternatives.


### 2.1.1: Definition section


* Supported by **flex**(1), not supported by **flexc++**: `%top` block, copies code to top of yylex.cc.
 
> 
> 
> 	+ Purpose: Define macros or include files.
> 	 + **Flexc++**'s alternative: Include header files in Scanner.ih.
> 



* Supported by **flex**(1), not supported by **flexc++**: Indented text or ``%{ ... %}'` blocks copied verbatim to
 yylex.cc
 
> 
> 
> 	+ Purpose: Can be used for helper code
> 	 + **Flexc++**'s alternative: Use member functions and/or data members of the `Scanner` class.
> 



* Supported by **flex**(1), not supported by **flexc++**: An unindented c-comment (``/* ... */'`) is copied to yylex.cc
 
> 
> 
> 	+ Purpose: Commenting helper code.
> 	 + **Flexc++**'s alternative: Comment outside of actions is ignored, and is considered part of
> 	 **flexc++**'s input file.
>




### 2.1.2: Rules section


* Supported by **flex**(1), not supported by **flexc++**: Indented text or ``%{ ... %}'` blocks before first rule copied
 to the top of the function body of yylex.cc
 
> 
> 
> 	+ Purpose: Declare local variables for yylex().
> 	 + **Flexc++**'s alternative: Use data members to keep track of state, or if you want to execute
> 	 some code everytime lex() is called, redefine
> 	 lex() to do more than just call the generated function
> 	 lex\_().
> 

* Supported by **flex**(1), not supported by **flexc++**: Other indented text or ``%{ ... %}'` blocks are copied
 to the output, but meaning is ill-defined and compiler errors may
 result.
 
> 
> 
> 	+ Purpose: POSIX compliance
> 	 + **Flexc++**'s alternative: A user code section is superfluous. User code should be provided as
> 	 member functions.
>




### 2.1.3: User code section


* Supported by **flex**(1), not supported by **flexc++**: The entire last section is copied to yylex.cc verbatim
 
> 
> 
> 	+ Purpose: defining companion routines
> 	 + **Flexc++**'s alternative: define member functions in scanner class
>




2.2: Patterns
-------------


 Not all patterns supported by **flex**(1) are supported by **flexc++**. Notably,
**flexc++** does not yet support certain flags in regular expressions, like the flag
to define case-insensitive regular expressions, or the flag allowing white
space in regular expressions.

Another minor difference is that named patterns, defined in the definion
section, cannot be used if they contain the lookahead operator (`/'). This is
the result of the way name expansions are handled by **flexc++**. **Flexc++** handles name
expansions as a parenthesized regular expression (a group). Since groups may
occur any number of times in a regular expression but a lookahead operator
only once, the look-ahead operator is not accepted in a named pattern.


2.3: Generated files
--------------------


 While **flex**(1) only generates a file `lex.yy.cc`, **flexc++** generates several
files: several header files and a source file. By default **flexc++** generates a
class header file (`Scanner.h`), and internal header file (`Scanner.ih`),
a base class header file (`Scannerbase.h`), and the file `lex.cc`
containing the implementation of the required members of the `class
Scanner`. `Scannerbase.h` and `lex.cc` should not be edited: they are
overwritten whenever **flexc++** is invoked. The other files (`Scanner.h` and
`Scanner.ih`) are generated only once, and can thereafter be modified by the
user (e.g., to add members to the `Scanner` class).


2.4: Comment
------------


**Flexc++** supports traditional **C** and **C++** style end-of-line comment. **Flexc++**
handles comment more flexible than `flex`. Cf. section [3.3](flexc++03.html#comments) for
details.


2.5: Members and macros
-----------------------


 As **C++** supports namespaces, the `yy`-prefix is no longer needed. In
addition, as **flexc++** generates a scanner class, member functions rather than
macros can (should) be used. See the conversion table below.



|  |  |  |
| --- | --- | --- |
| **flex** | ****flexc++**** | ****flexc++**** alternative |
| `yylex()` | `lex()` |
| `YYText()` | `matched()` |
| `YYLeng()` | `length()` |
| `ECHO` | `echo()` |
| `yymore()` | `more()` |
| `yyless()` | `redo()` | `accept()` |
| `BEGIN startcondition` | `begin(StartCondition_::startcondition)` |
| `YY_AT_BOL` |  n.a. |
| `yy_set_bol(at_bol)` |  n.a. |



The member functions in the **flexc++** column above are either members of
`Scanner` or of its base class. **Flexc++** does not use macros. All member
functions can be used from within actions or by other member functions.


2.6: Multiple input streams
---------------------------


 Multiple input files can easily be handled by **flexc++**. See section
[4.1](flexc++04.html#multiplestreams) for details.



---


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++01.html)* [Next Chapter](flexc++03.html)




---






































