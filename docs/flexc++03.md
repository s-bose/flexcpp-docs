

---


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++02.html)* [Next Chapter](flexc++04.html)




---



Chapter 3: Format of the input file
===================================


The **flexc++** input file consists of two sections, separated by a line containing
``%%`'. The section above `%%` contains option specifications and
definitions; the section below `%%` contains the regular expressions (and
their (optional) actions). The general layout of **flexc++**'s input file,
therefore, looks like this:


```


definitions
%%
rules
    

```


Optionally, a final line containing ``%%`' may follow the rules. The
following sections cover the `definitions' and `rules' sections.


3.1: Definitions section
------------------------


**Flexc++** supports command-line *options* and input-file *directives*
controlling **flexc++**'s behavior. Directives are covered in the next section
([3.1.1](flexc++03.html#DIRECTIVES)), options are covered in the section [1.1.1](flexc++01.html#OPTIONS).

The definitions section may also contain declarations of named regular
expressions. A named regular expression looks like
this:


```

name   pattern

```


Here, `name` is an identfier, which may also contain hyphens (`-`);
``pattern`' is a regular expression, see section [3.4](flexc++03.html#patterns). Patterns
start at the first non-blank character following the name, and end at the
line's last non-blank character. A named regular expression cannot contain
comment.

Finally, the definitions section may be used to declare *mini-scanners*
(a.k.a. *start conditions*), cf. section [3.7](flexc++03.html#STARTCONDITIONS). Start
conditions are very useful for defining small `sub-languages' inside the
language whose tokens must be recognized by the scanner. A commonly
encountered example is the start condition recognizing **C** style multi-line
comment.


### 3.1.1: Directives


 Some directives require arguments, which are usually provided following
separating (but optional) `=` characters. Arguments of directives are text,
surrounded by double quotes (strings), or embedded in raw string literals
(rawstrings). Double quotes or backslashes inside strings must themselves be
preceded by backslashes; these backslashes are not required when rawstrings
are used. 

The `%s` and `%x` directives are immediately followed by name lists,
consisting of identifiers separated by blanks. Here is an example of the
definition of a directive:
 
```


    %class-name = "MyScanner"
        

```


Directives accepting a `filename' do not accept path names, i.e., they
cannot contain directory separators (`/`); options accepting a 'pathname'
may contain directory separators. A 'pathname' using blank characters should
be surrounded by double quotes.

Some directives may generate errors. This happens when a directive conflicts
with the contents of an existing file which **flexc++** cannot modify (e.g., a
scanner class header file exists, but doesn't define a name space, but a
`%namespace` directive was provided). To solve the error the offending
directive could be omitted, the existing file could be removed, or the
existing file could be hand-edited according to the directive's specification.
Note that **flexc++** currently does not handle the opposite error condition: if a
previously used directive is omitted, then **flexc++** does not detect the
inconsistency. In those cases you may encounter compilation errors.

* **%baseclass-header** `= "filename"`   

 Defines the name of the file to contain the scanner class's base
 class interface. Corresponding command-line option:
 `--baseclass-header`.

It is an error if this directive is used and an already
 existing scanner-class header file does not include
 ``filename'`. 

* **%case-insensitive**  

 Generates a scanner which *case insensitively* matches regular
 expressions. All regular expressions specified in **flexc++**'s input
 file are interpreted case insensitively and the resulting scanner
 object will case insensitively interpret its input.

Corresponding command-line option: `--cases-insensitive`.

When this directive is specified the resulting scanner does not
 distinguish between the following rules:
 
```


        First       // initial F is transformed to f
        first
        FIRST       // all capitals are transformed to lower case chars
                

```


 With a case-insensitive scanner only the first rule can be matched,
 and **flexc++** will issue warnings for the second and third rule about
 rules that cannot be matched.

Input processed by a case-insensitive scanner is also handled case
 insensitively. The above mentioned `First` rule is matched for
 all of the following input words: `first First FIRST firST`. 

Although the matching process proceeds case insensitively, the
 matched text (as returned by the scanner's `matched()` member)
 always contains the original, unmodified text. So, with the above
 input `matched()` returns, respectively `first, First, FIRST`
 and `firST`, while matching the rule `First`.

* **%class-header** `= "filename"`   

 Defines the name of the file to contain the scanner class's
 interface. Corresponding command-line option: `--class-header`.

* **%class-name**  `= "className"`   

 Declares the name of the scanner class generated by **flexc++**. This
 directive corresponds to the `%name` directive used by
 **flex++**(1). Contrary to **flex++**'s `%name` declaration,
 `class-name` may appear anywhere in the first section of the
 grammar specification file. It may be defined only once. If no
 `class-name` is specified the default class name (`Scanner`)
 is used. Corresponding command-line option:
 `--class-name`.

It is an error if this directive is used and an already
 existing scanner-class header file does not define `class
 `className'`.

* **%debug**   
 
 Provide `lex` and its support functions with debugging code,
 showing the actual parsing process on the standard output
 stream. When included, the debugging output is active by default,
 but its activity may be controlled using the `setDebug(bool
 on-off)` member. Note that no `#ifdef DEBUG` macros are used in
 the generated code. 

* **%filenames** `= "basename"`   

 Defines the basename of the `Scanner.h, Scanner.ih,` and
 `Scannerbase.h` files. E.g., when using the directive
 
```


    %filenames = "scanner"
                

```


 the names of the generated files are, respectively, `scanner.h,
 scanner.ih,` and `scannerbase.h`. Corresponding command-line
 option: `--filenames`. The name of the source file (by default
 `lex.cc`) is controlled by the `%lex-source` directive.

* **%implementation-header** `= "filename"`   

 Defines the name of the file to contain the implementation header.
 Corresponding command-line option: `--implementation-header`.

It is an error if this directive is used and an already
 `'filename'` file does not include the scanner class header
 file.

* **%input-implementation** `= "sourcefile"`   

 Defines the pathname of the file containing the implementation of a
 user-defined `Input` class. 

* **%input-interface** `= "interface"`   

 Defines the pathname of the file containing the interface of a
 user-defined `Input` class. See section **17. THE CLASS INPUT**
 in the **flexc++api**(3) manual page for additional information
 about user-defined `Input` classes.

* **%interactive**  

 Generate an interactive scanner. An interactive scanner reads lines
 from the input stream, and then returns the tokens encountered on
 that line. The interactive scanner implemented by **flexc++** only
 predefines the `Scanner(std::istream &in, std::ostream &out)`
 constructor, by default assuming that input is read from
 `std::cin`. See also section `1. INTERACTIVE SCANNER` section
 in the **flexc++api**(3) manual page.

* **%lex-function-name** `= "funname"`   

 Defines the name of the scanner class's member to perform the
 lexical scanning. If this directive is omitted the default name
 (`lex`) is used. Corresponding command-line option:
 `--lex-function-name`.

* **%lex-source** `= "filename"`   

 Defines the name of the file to contain the scanner member
 `lex`. Corresponding command-line option: `--lex-source`.

* **%no-lines**   
 
 Do not put `#line` preprocessor directives in the file containing
 the scanner's `lex` function. If omitted `#line` directives
 are added to this file, unless overridden by the command line
 options `--lines` and `--no-lines`.

* **%namespace** `= "identifer"`   

 Define the scanner class in the namespace `identifier`. By
 default no namespace is used. If this directives is used the
 implementation header is provided with a commented out `using
 namespace` declaration for the requested namespace. In addition,
 the scanner and scanner base class header files also use the
 specified namespace to define their include guard directives.

It is an error if this directive is used and an already
 scanner-class header file does not define `namespace
 identifier`.

* **%print-tokens**   
 
 this directive results in the tokens as well as the matched text to
 be displayed on the standard output stream, just before returning
 the token to `lex`'s caller. Displaying is suppressed again when
 the `lex.cc` file is generated without using this directive. The
 function showing the tokens (`ScannerBase::print_`) is called
 from `Scanner::print()`, which is defined in-line in
 `Scanner.h`. Calling `ScannerBase::print_`, therefore, can
 also easily be controlled by an option controlled by the program
 using the scanner object.
 this directive does *not* show the tokens returned and text
 matched by **flexc++** itself when reading its input **s**. If that is
 what you want, use the `--own-tokens` option.

* **%s** `namelist`   

 The `%s` directive is followed by a list of one or more
 identifiers, separated by blanks. Each identifier is the name of
 an *inclusive start condition*.

* **%skeleton-directory** `= "pathname"`   

 Use `pathname` rather than the default (e.g.,
 `/usr/share/flexc++`) path when looking for **flexc++**'s skeleton
 files. Corresponding command-line option:
 `--skeleton-directory`.

* **startcondition-name**  `= "startconditionName"`   

 By default, **flexc++** defines the enum `StartCondition_` defining
 the names of start-conditions. The `%startcondition-name`
 directive can be used to configure another name for the enum
 containing the names of the start-conditions. It may be defined
 only once. 

The name of the startcondition-enum may be modified, and the
 directive can also be omitted again after it has been specified
 before. When changing the name of the startcondition-enum or when
 reverting to the default name newly generated `lex.cc` and
 `ScannerBase.h` files will use the currently defined
 startcondition-enum name. Be advised, though, that the
 startcondition-enum name may also be used in user-defined members
 of the scanner-class, or in the scanner's header and internal
 header files. If so, the user is responsible for updating those
 files to the currently defined name of the startcondition-enum.

* **%target-directory** `= "pathname"`   

`Pathname` defines the directory where generated files should be
 written. By default this is the directory where **flexc++** is
 called. This directive is overruled by the `--target-directory`
 command-line option.

* **%x** `namelist`   

 The `%x` directive is followed by a list of one or more
 identifiers, separated by blanks. Each identifier is the name of
 an *exclusive start condition*.




3.2: Rules section
------------------


 The rules section of the **flexc++** input file contains rules of the
form:


```

pattern    action

```


*Action* is optional, and is separated from *pattern* by spaces and/or
tabs. It consists of a single-line **C++**-statement, or it consists of a
compound statement that may span several lines.

Alternatively, an action may consist of a vertical bar (`|'). A vertical bar
indicates that *pattern* uses the same action as the next rule.


3.3: Comment
------------


 Comment may be used almost everywhere in **flexc++**'s input file. 
Both traditional **C**-style multi-line comment (i.e., `/* ... */`) and 
**C++** style end-of-line comment (i.e., `// ...`) can be used. Indentation
is optional.

When comment is encountered outside of an action, **flexc++** discards the comment,
while all comment provided in the contect of actions are copied verbatim to
the generated source file. 

Comment cannot be used when defining named regular expressions in the
definitions section.


3.4: Patterns
-------------


 The patterns in the input (see [Rules Section 3.2](flexc++03.html#rulessection)) are
written using an extended set of regular expressions. These are:

* `x`  

 match the character `x'

* **.**  

 any character except newline;

* `[xyz]`  

 a character class; in this case, the pattern matches either an `x', a `y',
 or a `z'. See also the paragraph about character classes below;

* `[abj-oZ]`  

 a ``character class'' with a range in it; matches an `a', a `b', any
 letter from `j' through `o', or a `Z'. See also the paragraph about
 character classes below; 

* `[^A-Z]`  

 a ``negated character class'', i.e., any character but those in the class.
 In this case, any character EXCEPT an uppercase letter. See also the
 paragraph about character classes below; 

* `[^A-Z\n]`  

 any character EXCEPT an uppercase letter or a newline. See also the
 paragraph about character classes below; 

* `[:predef:]`  

 a *predefined* set of characters. See below for an overview. When used,
 it is interpreted as an element in a character class. Consequently, it is
 always embedded in a set of square brackets defining the character class
 (e.g., `[[:alnum:]]`);

* `s1{+}s2`  

 If `s1` and `s2` are character classes: the union of the characters in
 `s1` and `s2`;

* `s1{-}s2`  

 If `s1` and `s2` are character classes: the set-difference of the
 characters in `s1` minus the characters in `s2`;

* `"[xyz]\"foo"`  

 the literal string ``[xyz]"foo`';

* `R"([xyz]\"foo)"`  
 the literal string ``[xyz]\"foo`' (using a raw string
 literal). Raw string literals using labels (which must be identifiers,
 e.g., `R"label( labelled raw string )label"` are also supported;

* `R"label("(xyz"))label"`  

 the literal string ``"(xyz")`' (using a labeled rawstring);

* `\X`  

 if X is `a', `b', `f', `n', `r', `t', or `v', then the ANSI-C
 interpretation of `\x'. Otherwise, a literal `X' (used to escape operators
 such as `\*');

* `\0`  

 a NUL character (ASCII code 0);

* `\123`  

 the character with octal value 123 (i.e., decimal 83);

* `\x2a`  

 the character with hexadecimal value 2a (i.e, decimal 42);

* `(r)`  

 a regular expression `r` by itself. It is used to override precedence
 (see below);

* `{name}`  

 the expansion of the `name' definition (see also section [3](flexc++03.html#FILEFORMAT));

* `r*`  

 zero or more `r`s, where r is any regular expression;

* `r+`  

 one or more `r`s;

* `r?`  

 zero or one `r`s (that is, an optional r);

* `rs`  

 the regular expression `r' followed by the regular expression `s'. This is
 called concatenation;

* `r{m, n}`  

 where `0 <= m <= n`: match `r' at least m, but at most n times; called
 interval expression; A regular expression to which `{0, 0}` is appended
 is ignored, and a warning message is shown;

* `r{m,}`  

 where `0 <= m`: match `r' m or more times;

* `r{m}`  

 where `0 <= m`: match `r' exactly m times; A regular expression to which
 `{0}` is appended is ignored, and a warning message is shown;

* `r|s`  

 either an `r' or an `s';

* `r/s`  

 an `r' but only if it is followed by an `s'. The text matched by `s' is
 included when determining whether this rule is the longest match, but is
 then returned to the input before the action is executed. So the action
 only sees the text matched by `r'. This type of pattern is called trailing
 context. The `/`-character is commonly referred to as the *lookahead
 operator*.

A warning is generated when the `r`-pattern may match no text. This is a
 potentially dangerous situation. Consider this pattern
 
```


    a*/b
        

```


 with input `b`. This input matches `a*/b`, but `b` is pushed back on
 to the input stream. Then the process is repeated, resulting in a
 continuous loop. 

If **flexc++** detects patterns potentially not matching any text it generates 
 warnings like this:
 
```


    [Warning] input, line 7: null-matching regular expression
        

```


 By placing the comment
 
```


    //%nowarn
        

```


 on the line just before a regular expression that potentially does not
 match any text, the warning for that regular expression is suppressed;

* `^r`  
 
 `r', if appearing at the beginning of a line (i.e., when just starting
 to scan, or right after a newline has been read). When `r` appears
 elsewhere on a line it isn't matched by this rule; if the `^`-character
 is not the first character of a regular expression it is interpreted as a
 plain `^`-character;

* `r$`  

 an `r', if it appears at the end of a line (i.e., the next character on the
 input stream is a newline character). The expression `r$` is equivalent
 to the expression ``r/\n`'. When `r` appears
 elsewhere on a line it isn't matched by this rule; if the `$`-character
 is not the last character of a regular expression it is interpreted as a
 plain `$`-character. A dollar-terminated regular expression, however,
 may be followed by an action or vertical bar indicating that the regular
 expression uses the same action as the next rule;

* `<s>r`  

 an `r', but only in start condition s (cf. section [3.7](flexc++03.html#STARTCONDITIONS));

* `<s1,s2,s3>r`  

 same, but in any of start conditions s1, s2, or s3;

* `<*>r`  

 same, but `r` is used in any start condition;

* `<sc-list>{compound rules}`  

 all rules defined in *compound rules* are active in the set of start
 conditions specified at *sc-list*. Rules defined in *compound rules*
 cannot themselves specify start conditions. *Compound rules* may contain
 empty lines;

* `<<EOF>>`  

 matches `end-of-file';

* `<sc-list><<EOF>>`  

 an end-of-file when in the start conditions specified at *sc-list*.
)

**Character classes**

Inside a character class all regular expression operators lose their special
meanings, except for the escape character (`\`), the character range
operator `-`, the end of character class operator `]`, and, at the
beginning of the class, `^`. All ordinary escape sequences are supported,
all other escaped characters are interpreted as literal characters (e.g.,
`\c` is a literal `c`).

To add a closing bracket to a character class use `[]` or `\]`. To add a
closing bracket to a negated character class use `[^]` (or use `[^`
followed by `\]` somewhere within the character class). Minus characters are
used to define character ranges (e.g., `[a-d]`, defining `[abcd]`) except
in the following cases, where **flexc++** recognizes a literal minus character:
 `[-`, or `[^-` (a minus at the very beginning of a character class); 
 `-]` (a minus at the very end of a character class); 
 or `\-` (an escaped minus character)


 Once a character class has started, all
subsequent character (ranges) are added to the set, until the final closing
bracket (`]`) has been reached.

**Operator precedence**

The operators used in specifying regular expressions have the following
priorities (listed from lowest to highest):

* `|`  
 
 when used to separate patterns sharing the second pattern's actions;

* `^r` and `r$`:  

`^`: at the beginning of a regular expression `r`: `r` only matches
 when encountered at the beginning of a line;  

`$`: at the end of a regular expression `r`: `r` only matches when
 encountered at the end of a line;

* `/`  

 the look ahead operator;

* `|`  

 the alternatives (`or') operator;

* `rs`  

 concatenation of regular expressions `r` and `s`;

* `multipliers`  

`*, +, ?` and the interval specification (i.e., `{...}`);

* `{+}, {-}`  
 
 (In the context of character classes). The set union and set difference
 operators;

* `(r)`  
 
 (Parentheses). Here, r may be any regular expression (not containing the
 look-ahead operator).



Different from the lex-standard, but in line with most other regular
expression engines the interval operator is given higher precedence than
concatenation. To require two repetitions of the word `hello` use
`(hello){2}` rather than `hello{2}`, which to **flexc++** is identical to the
regular expression `helloo`.

Named regular expressions have the same precedence as parenthesized regular
expressions. So after
 
```


    WORD  xyz[a-zA-Z]
    %%
    {WORD}{2}
        

```


 the input `xyzaxyzb` is matched, whereas `xyzab` isn't.

In addition to characters and ranges of characters, character classes can also
contain predefined character sets. These consist of certain names between
`[:` and `:]` delimiters. The predefined character sets are:

```

     
         [:alnum:] [:alpha:] [:blank:]
         [:cntrl:] [:digit:] [:graph:]
         [:lower:] [:print:] [:punct:]
         [:space:] [:upper:] [:xdigit:]


```


 These predefined sets designate sets of characters equivalent to the
corresponding standard **C** `isXXX` function. For example, `[:alnum:]`
defines all characters for which `isalnum` returns true.

As an illustration, the following character classes are equivalent:
 
```

 
         [[:alnum:]]
         [[:alpha:][:digit:]]
         [[:alpha:][0-9]]
         [a-zA-Z0-9]
    

```


Note that a negated character class like `[^A-Z]` matches a newline unless
`\n` (or an equivalent escape sequence) is one of the characters explicitly
present in the negated character class (e.g., `[^A-Z\n]`). This differs from
the way many other regular expression engines treat negated character classes.
Matching newlines means that a pattern like `[^"]*` can match the entire
input unless there's another quote in the input.

**Flexc++** allows negation of character class expressions by prepending `^` to
the name of a predefined character set. Here are the negated predefined
character sets:
 
```

                
         [:^alnum:] [:^alpha:] [:^blank:]
         [:^cntrl:] [:^digit:] [:^graph:]
         [:^lower:] [:^print:] [:^punct:]
         [:^space:] [:^upper:] [:^xdigit:]
    

```


The ``{+}`' operator computes the union of two character classes. For
example, `[a-z]{+}[0-9]` is the same as `[a-z0-9]`.

The ``{-}`' operator computes the difference of two character classes. For
example, `[a-c]{-}[b-z]` represents all the characters in the class
`[a-c]` that are not in the class `[b-z]` (which in this case, is just the
single character ``a`'). 

A rule can have at most one instance of trailing context (the `/` operator
or the `$` operator). The start condition, `^`, and `<<EOF>>`
patterns can only occur at the beginning of a pattern, and, as well as with
`/` and `$`, cannot be grouped inside parentheses. A `^` which does not
occur at the beginning of a rule or a `$` which does not occur at the end of
a rule loses its special properties and is treated as a normal character.

The following are invalid:
 
```

                
         foo/bar$
         <sc1>foo<sc2>bar
    

```

 
Note that the first of these can be rewritten `foo/bar\n'.

If the desired meaning is a `foo' or a `bar'-followed-by-a-newline, the
following could be used (the special | action is explained below, see section
[3.6](flexc++03.html#actions)):


```

                
         foo      |
         bar$     /* action goes here */
    

```

 
 A comparable definition can be used to match a `foo' or a
`bar'-at-the-beginning-of-a-line.


3.5: Character constants
------------------------


 
Character constants are surrounded by single quote characters. They match
single characters which, however, can be specified in various ways.
 * The simplest form consists of just a single character: the pattern
 `'a'` matches the character `a`, the pattern `'.'` matches the
 dot-character (`.` thus loses its meaning of `any character but
 the newline character');
 * Standard escape characters (like `'\n', '\f', '\b'`) are converted
 to their (single character) ascii-values, matching those characters
 when they are encountered in the input. Therefore, of the following
 two rules the second is never matched (with **flexc++** generating a
 corresponding warning, since both match the newline character):
 
```


    '\n'    return 1;
    \n      return 2;
       

```
* Octal numbers, starting with a backslash and consisting of three
 octal digits are converted to a number matching input characters of
 those numbers. E.g., `'\101'` is converted to 65, matching ascii
 character `A`;
 * Likewise, hexadecimal numbers, starting with `x` and followed by
 two hexadecimal digits are converted to a number matching input
 characters whose values equal those numbers. E.g., `'\x41'` is also
 matching ascii character `A`;
 * Other escaped single characters match those characters. E.g.,
 `'\\'` matches the single backslash, `'\''` matches the single
 quote character. But also: `'\F'` matches the single `F`
 character, since no special escaped meaning is associated with `F`.



Considering the above, to match character (in this example: except for the
newline character) including its surrounding quotes a regular expression
consisting of an escaped quote character, followed by any character, followed
by a quote character can be used:
 
```


    \'.'        // matches characters surrounded by quotes
        

```



3.6: Actions
------------


 As described in Section [3.2](flexc++03.html#rulessection), the second section of the **flexc++**
input file contains rules: pairs of patterns and (optional) actions.

Specifications of patterns end at the first unescaped white space character;
the action then starts at the first non-white space character. It usually
contains **C++** code, with two exceptions: the empty and the bar (`|`)
action (see below). If the **C++** code starts with a brace (`{`), the action
can span multiple lines until the matching closing brace (`}`) is
encountered. **Flexc++** correctly handles braces in strings and comments.

Actions can be empty (omitted). Empty actions discard the matched pattern. To
avoid confusion it is advised to provide at least a simple comment stating
that the matched input is ignored.

The *bar action* is an action containing only a single vertical bar (`|`).
This tells **flexc++** to use the action of the next rule. This can be repeated so
the following rules all use the same action:
 
```


    a   |
    b   |
    c   std::cout << "Matched " << match() << "\n";
        

```


 Actions can return an `int` value, which is usually interpreted as a
*token* by the program calling the scanner's `lex` member. When `lex` is
called after it has returned it continues its pattern-matching process just
beyond the last-matched point in the input stream.


3.7: Start conditions (Mini scanners)
-------------------------------------


**Flexc++** uses regular expressions to generically descibe textual patterns. Often
a **flexc++** specification file uses multiple `sub-languages' having specialized
tasks. A sub-language to describe the normal structure of the input, a
sub-language to describe comment, a sub-language to describe strings, etc.,
etc.

For flexible handling of these sub-languages **flexc++**, like flex, offers *start
conditions*, a.k.a. *mini scanners*. A start condition can be declared in
the definition section of the lexer file:
 
```


%x  string
%%
...
    

```

 
 A `%x` is used to declare *exclusive start conditions*. Following
`%x` a list (no commas) of start condition names is expected. Rules
specified for exclusive start conditions only apply to that particular mini
scanner. It is also possible to define *inclusive start condition* using
`%s`. Rules not explicitly associated with a start condition (or with the
(default) start condition `StartCondition_::INITIAL` also apply to
inclusive start conditions.

A start condition is used in the rules section of the lexical scanner
specification file as indicated in section [3.4](flexc++03.html#patterns). Here is a concrete
example:
 
```


%x string
%%

\"              {
                    more();
                    begin(StartCondition_::string);
                }

<string>{
    \"          {
                    begin(StartCondition_::INITIAL);
                    return Token::STRING;
                }
    \\.|.       more();
}
    

```


 This tells **flexc++** that the double quote starts (begins) the
`StartCondition_::string` start condition. The `string` start condition's
rules then define what happens to double quoted strings. All its characters
are collected, and eventually the string's content is returned by
`matched()`.

By default, scanners generated by **flexc++** start in the
`StartCondition_::INITIAL` start condition. When encountering a double
quote, the scanner switches to the `StartCondition_::string` mini
scanner. Now, only the rules that are defined for the `string` start
condition are active. Once **flexc++** encounters an unescaped double quote, it
switches back to the `StartCondition_::INITIAL` start condition and returns
`Token::STRING` to its called, indicating that it has seen a **C** string.

There is nothing special to either the function `begin(StartCondition_)` or
to the `StartCondition_` enum itself. They can be used anywhere within the
Scanner class. E.g., after providing the Scanner class with a
`std::stack<StartCondition_> d_scStack` start conditions can be
stacked. Calling member `begin` could be embedded in a member
`Scanner::push(StartCondition_)` like this:
 
```


    void Scanner::push(StartCondition_ next)
    {
        d_scStack.push(startCondition()); // push the current SC.
        begin(next);                      // switch to the next
    }
        

```


 In addition, for returning to the start condition currently on top of the
stack simply call a member `Scanner::popStartCondition()`, implemented like
this: 
 
```


    void Scanner::popStartCondition()
    {
        begin(d_scStack.top());
        d_scStack.pop();
    }
        

```

`push` and `popStartCondition` should be given the same access rights
as `begin`: they should be defined in the private section of the Scanner
class.


### 3.7.1: Notation details


 Instead of using a mini scanner compound statement, it is also 
possible to define rules using explicit start condition specifications
(cf. section [3.4](flexc++03.html#patterns). Here is the `string` start condition once again,
now using explicit start condition specifications:
 
```


%x string
    
%%

\"              {
                    more();
                    begin(StartCondition_::string);
                }
<string>\"      {
                    begin(StartCondition_::INITIAL);
                    return Token::STRING;
                }
<string>\\.|.   more();
    

```



3.8: Members
------------



The `Scanner` class offers the following members, which can be called from 
within actions (or by members called from
those actions):

* **void accept(size\_t nChars = 0)**  

`accept(n)` returns all but the first `nChars' characters of the
 current token back to the input stream, where they will be rescanned
 when the scanner looks for the next match. So, it matches `nChars' of
 the characters in the input buffer, rescanning the rest. This function
 effectively sets `length`'s return value to `nChars` (note: with
 **flex++** this function was called `less`);

* **void begin(StartCondition\_ startCondition)**  

 activates the regular expression rules associated with
 `StartCondition_ startCondition`. As this enumeration is a strongly
 typed enum the `StartCondition_` scope must be specified as
 well. E.g., 
 
```


    begin(StartCondition_::INITIAL);
        

```


* **std::string const &cwd() const**  

 returns the working directory that was active when the `Scanner's`
 constructor is called. It is also the program's current working
 directory after constructing a `Scanner` object and when its
 `lex` member returns.

* **bool debug() const**  

 returns `true` if `--debug` or `%debug` was specified, otherwise
 `false`.

* **void echo() const**  
 
 The currently matched text (i.e., the text returned by the member
 `matched`) is inserted into the scanner object's output stream;

* **std::string const &filename() const**  

 returns the name of the file currently processed by the scanner object.

* **size\_t length() const**  

 returns the length of the text that was matched by `lex`. With
 **flex++** this function was called `leng`.

* **size\_t lineNr() const**  

 returns the line number of the currently scanned line. This function is
 always available (note: **flex++** only offered a similar function
 (called `lineno`) after using the `%lineno` option).

* **std::string const &matched() const**  

 returns the text matched by `lex` (note: **flex++** offers a similar
 member called `YYText`).

* **void more()**  

 the matched text is kept and will be prefixed to the text that is
 matched at the next lexical scan;

* **std::ostream &out()**  

 returns a reference to the scanner's output stream;

* **bool popStream()**  

 closes the currently processed input stream and continues to process
 the most recently stacked input stream (removing it from the stack of
 streams). If this switch was successfully performed `true` is
 returned, otherwise (e.g., when the stream stack is empty) `false`
 is returned;

* **void preCode()**  

 By default this function has an empty, inline implementation in
 `Scanner.h`. It can safely be replaced by a user-defined
 implementation. This function is called by `lex_`, just before it
 starts to match input characters against its rules: `preCode` is called
 by `lex_` when `lex_` is called and also after having executed the
 actions of a rule which did not execute a `return` statement. The
 outline of `lex_`'s implementation looks like this: 
 
```


int Scanner::lex_()
{
    ...
    preCode();

    while (true)
    {
        size_t ch = get_();            // fetch next char
        ...
        switch (actionType_(range))    // determine the action
        {
            ... maybe return
        }
        ... no return, continue scanning
        preCode();
    } // while
}
        

```


* **void postCode(PostEnum\_ type)**  

 By default this function has an empty, inline implementation in
 `Scanner.h`. It can safely be replaced by a user-defined
 implementation. This function is called by `lex_`, just after a rule
 has been matched, where `PostEnum_`'s value indicates the
 characteristic of the matched rule. `PostEnum_` has four values:
	+ **PostEnum\_::END**: the function `lex_` immediately returns 0
	 once `postCode` returns, indicating the end of the input was
	 reached;
	 + **PostEnum\_::POP**: the end of an input stream was reached, and
	 processing continues with the previously pushed input stream. In
	 this case the function `lex_` doesn't return, it simply
	 coontinues processing the previously pushed stream;
	 + **PostEnum\_::RETURN**: the function `lex_` immediately returns 
	 once `postCode` returns, returning the next token;
	 + **PostEnum\_::WIP**: the function `lex_` has matched a
	 non-returning rule, and continues its rule-matching process.
* **void push(size\_t ch)**  

 character `ch` is pushed back onto the input stream. I.e., it will be
 the character that is retrieved at the next attempt to obtain a
 character from the input stream;

* **void push(std::string const &txt)**  

 the characters in the string `txt` are pushed back onto the input
 stream. I.e., they will be the characters that are retrieved at the
 next attempt to obtain characters from the input stream. The
 characters in `txt` are retrieved from the first character to the
 last. So if `txt == "hello"` then the `'h'` will be the character
 that's retrieved next, followed by `'e'`, etc, until `'o'`;

* **void pushStream(std::istream &curStream)**  

 this function pushes `curStream` on the stream stack;
 **This member is not available with interactive scanners.**

* **void pushStream(std::string const &curName)**  

 same, but the stream `curName` is opened first, and the resulting
 `istream` is pushed on the stream stack;
 **This member is not available with interactive scanners.**

* **void redo(size\_t nChars = 0)**  

 this member acts like `accept` but its argument counts backward from
 the end of the matched text. All but these `nChars` characters are
 kept and the last `nChar` characters are rescanned. This function
 effectively reduces `length`'s return value by `nChars`;

* **void setDebug(bool onOff)**  

 Switches on/off debugging output by providing the argument `true` or
 `false`. Switching on debugging output only has visible effects if the
 `debug` option has been specified when generating `lex.cc`;

* **void setFilename(std::string const &name)**  

 this function sets the name of the stream returned by `filename` to
 `name`;

* **void setMatched(std::string const &text)**  

 this function stores `text` in the matched text buffer. Following a
 call to this function `matched` returns `text`;

* **void switchStreams(std::istream &in,
 std::ostream &out = std::cout)**  

 The currently processed input and output streams are closed, and
 processing continues at `in`, writing output to `out`. This is
 *not* a stack-operation: after processing `in` processing
 does not return to the original stream.

When **flexc++** generates an interactive scanner, this member is 
 available (as a protected member). However, it should be considered an
 internal use only member;

* **void switchStreams(std::string const &infilename)**  

 The currently processed input stream is closed, and processing
 continues at the stream whose name is specified as the function's
 argument. This is *not* a stack-operation: after processing
 `infilename` processing does not return to the original stream.  

**This member is not available with interactive scanners.**

* **void switchStreams(std::string const &infilename,
 std::string const &outfilename)**  

 The currently processed input and output streams are closed, and
 processing continues at the stream whose name is specified as the
 function's first argument, writing output to the file whose name is
 specified as the function's second argument. This latter file is
 rewritten. This is *not* a stack-operation: after processing
 `infilename` processing does not return to the original stream.  

**This member is not available with interactive scanners.**

* **StartCondition\_ startCondition() const**  

 returns the currently active start condition (mini scanner).




3.9: Handling input your own way
--------------------------------


 Assuming that the scanner class is called `Scanner' the class Input is nested
within the class `ScannerBase'. The stream from which **flexc++** retrieves
characters is completely decoupled from the pattern-matching algorithm
implemented in the `ScannerBase` class. the pattern-matching algorithm
retrieves the next character from a class `Input`, nested under
`ScannerBase`. This class will usually provide all the required
functionality, but users of **flexc++** may optionally provide their own `Input`
class. 

In situations where the default `Input` implementation doesn't suffice
simply `roll your own', implementing the following interface and use the
`%option input-interface` and `%option input-implementation` options in
the `lexer` file to include, respectively, your own class `Input`
interface in the generated `Scannerbase.h` file and `Input` member
function implementations in the generated `lex.cc` file.

When implementing your own class `Input`, the following public interface
must at least be provided:
 
```


    class Input
    {
        public:
            Input();
                                            // dynamically allocated iStream
            Input(std::istream *iStream, size_t lineNr = 1);   
            size_t get();                   // the next character
            size_t lineNr() const;          
            size_t nPending() const;          
            void setPending(size_t nPending);          
            void reRead(size_t ch);         // push back 'ch' (if <= 0x100)
                                            // push back str from idx 'fmIdx'
            void reRead(std::string const &str, size_t fmIdx);

            void close();                 // delete dynamically allocated
    };
        

```


 This interface may be augmented with additional members, but the
shown interface is used by `ScannerBase`. **Flexc++** places `Input` in
`ScannerBase`'s private interface and all communication with `Input` is
handled by `ScannerBase`. `Input`'s members must perform the following
tasks:
 * `Input()`: the default constructor performs no special tasks, it
ensures that an `Input` object is in a valid state, in particular allowing
`close` to do its job.

* The copy constructor must be available. When necessary it can be
added to `Input`'s interface. The default implementation uses `Input`'s
default copy constructor so there was no need to add it explicitly to the
interface.

* `Input(std::istream *iStream, size_t lineNr)`: information is read from
the `istream` that is passed to `Input`. The `std::istream *iStream`
already points at an open, dynamically allocated `istream`, and is ready for
reading. Stream switching is not performed by `Input`, but by
`ScannerBase`. Also the names of streams currently being read (e.g., when
using `//include` directives in specification files) are administered and
maintained by `ScannerBase`. `Input` should treat the pointer as plain old
data (POD). The default implementation therefore can use the default copy
constructor, overloaded assignment operator and destructor: `iStream` is
simply assigned to one of `Input`'s data members, and is simply copied when
`Input`'s copy constructor or assignment operator is called. Likewise,
`lineNr` is assigned to `Input's` data member keeping track of the line
number count. 

* `size_t get()`: this member must return the next character as an
`unsigned char`. At end-of-file is must return the value (predefined by
`ScannerBase`) `AT_EOF`. The default implementation is found in 
`lex.cc`, generated by **flexc++**.

* `size_t lineNr() const`: the line number of the currently processed
line should be returned. By convention these are numbers, so while processing
the first line `lineNr` should return 1.

* `size_t nPending() const`: should return the number of pending
characters (i.e., the number of characters which were passed back to the
`Input` object using its `reRead` members which were not yet retrieved
again by its `get` member).

* `void setPending(size_t nPending)`: should keep `nPending` characters
in the `Input` object's pending characters queue. The lexical scanner always
passes the value received from `nPending` to `setPending`, without calling
`get` in between. The default implementation uses an `std::deque` for
storing pending characters, and is found in `lex.cc`, generated by **flexc++**.

* `void reRead(size_t ch)`: the character stored in `ch` is pushed back
into the `Input` object. The call should be ignored if `ch` exceeds the
value `0xff`. The default implementation is found in `lex.cc`, generated
by **flexc++**.

* `void reRead(std::string const &str, size_t fmIdx)`: the characters in
`str` are pushed back into the `Input` object in reverse order from
`str`'s final character down to (and including) the character at offset
`fmIdx`. The default implementation is found in `lex.cc`, generated
by **flexc++**.

* `void close()`: this member must delete the memory to which `iStream`
points, *en passant* closing the stream. It is called by
`ScannerBase::popStream` at end-of-file. The default implementation is
found in `Scannerbase.h`, generated by **flexc++**. Note: `Input's` destructor
should *not* delete the memory to which `iStream` points.





---


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++02.html)* [Next Chapter](flexc++04.html)




---


















































































































