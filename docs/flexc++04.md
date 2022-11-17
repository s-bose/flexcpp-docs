

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


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++03.html)* [Next Chapter](flexc++05.html)




---



Chapter 4: Generated files
==========================


**Flexc++** generates four files from a well-formed input file:
 * A file containing the implementation of the `lex` member function
and its support functions. By default this file is named `lex.cc`.

* A file containing the scanner's class interface. By default this file
is named `Scanner.h`. The scanner class itself is generated once and is
thereafter `owned' by the programmer, who may change it *ad-lib*. Newly
added members (data members, function members) will survive future **flexc++** runs
as **flexc++** will never rewrite an existing scanner class interface file, unless
explicitly ordered to do so.

* A file containing the interface of the scanner class's *base
class*. The scanner class is publicly derived from this base class. It is used
to minimize the size of the scanner interface itself. The scanner base class
is `owned' by **flexc++** and should never be hand-modified. By
default the scanner's base class is provided in the file
`Scannerbase.h`. At each new **flexc++** run this file is rewritten unless **flexc++**
is explicitly ordered *not* to do so.

* A file containing the *implementation header*. This file should
contain includes and declarations that are only required when compiling the
members of the scanner class. By default this file is named
`Scanner.ih`. This file, like the file containing the scanner class's
interface is never rewritten by **flexc++** unless **flexc++** is explicitly ordered to do
so.



The first file, `lex.cc` contains lookup tables, the code to walk through
the lookup tables and the actions specified in the lexer file. Since the
lookup tables and actions (possibly) change every time **flexc++** is called,
`lex.cc` is rewritten at each new **flexc++** run.

The file `Scannerbase.h` contains the `Scanner`'s base class The
`Scanner` class is derived from `ScannerBase`. The `Scannerbase.h` is
`owned' by **flexc++**, and **flexc++** reqrites `Scannerbase.h` at each new **flexc++** run.

The other two files `Scanner.h` and `Scanner.ih` are created only once,
and can safely be edited by the programmer. The `Scanner.h` header file
contains the final `Scanner` class, to which new members may be added. These
members may be called from the actions defined in **flexc++**'s input file
(`lexer`).

Finally, `Scanner.ih` contains declarations which are used by the
implementations of the `Scanner` members. One can place `using` statements
here as well as includes which are only required by member implementations. In
a well-designed classq, source files defining new members of the class
`Scanner` should only have to include `Scanner.ih`.


4.1: Multiple input streams
---------------------------


 Some scanners (such as those which support `include' files) require reading
from several input streams. Usually, a directive like `#include` is defined
controlling stack-wise stream switching. Alternatively, direct switches to
other streams can be requested. **Flexc++** offers both ways to switch streams.

* For stack-wise stream switching, a directive like `#include` is
usually defined. When encountered, processing of the current stream is
suspended and the scanning process continues at the stream whose name is
specified at the `#include` directive. When reaching a stream's end-of-file
the scanner switches back to the suspended input stream. In this case streams
are pushed on a stack when encountering a stream switching directive and
popped off the stack once the current file has completely been processed.
 * Second, the user may request the scanner to switch to another stream.
Optionally, the user may request to switch back. In this case, the user is
completely responsible for all stream-related bookkeeping. The scanner merely
provides a means to switch from one stream to another.



The members `void pushStream(std::istream &curStream)` and `void
pushStream(std::string const &curName)` are provided for stack-wise stream
switching. By default, at a stream's end-of-file the member `bool
popStream()` is automatically called by **flexc++**, closing the currently processed
input stream and continuing the processing of the most recently stacked input
stream (removing it from the stack of streams). If this switch was
successfully performed `true` is returned. Otherwise (e.g., when the stream
stack is empty) `false` is returned. If the stream to switch to does not
exist a `std::exception` is thrown. An exception is also thrown when files
are recursively pushed. 

Returning to the previously stacked stream is handled automatically and
does not require the use of an `<<EOF>>` rule. If an `<<EOF>>` rule is
defined, however, previously pushed streams are *not* automatically
re-activated. In that case, returning to previously pushed streams is the
responsibility of the programmer. After completely processing the first input
file the member `lex` returns 0.

When switching to another stream the line number counter and file name are
reset to, respectively, 1 and the new file's name. When returning to a
previously suspended (stacked) stream that stream's line number and file name
are restored. 

Direct, non-stack based stream switching is handled by various public
support member functions of the Scanner class (actually, the functions are
implemented as members of the ScannerBase base class):
 * **void switchIstream(std::string const &infilename)**
 The currently processed input stream is closed, and processing
 continues at the stream whose name is specified as the function's
 argument. This is *not* a stack-operation: after processing
 `infilename` processing does not return to the original stream.

**This member is not available with interactive scanners.**

* **void switchOstream(std::ostream &out)**
 The currently processed output stream is closed, and
 new output is written to `out`. 

* **void switchOstream(std::string const &outfilename)**

The current output stream is closed, and output is written to
 `outfilename`. If this file already exists, it is rewritten.

* **void switchStreams(std::istream &in,
 std::ostream &out = std::cout)**
 The currently processed input and output streams are closed, and
 processing continues at `in`, writing output to `out`. This is
 *not* a stack-operation: after processing `in` processing
 does not return to the original stream.

**This member is not available with interactive scanners.**

* **void switchStreams(std::string const &infilename,
 std::string const &outfilename)**
 The currently processed input and output streams are closed, and
 processing continues at the stream whose name is specified as the
 function's first argument, writing output to the file whose name is
 specified as the function's second argument. This latter file is
 rewritten. This is *not* a stack-operation: after processing
 `infilename` processing does not return to the original stream.
 If `outfilename == "-"` then the standard output stream
 is used as the scanner's output medium; if `outfilename == ""` then
 the standard error stream is used as the scanner's output medium.

If `outfilename == "-"` then the standard output stream
 is used as the scanner's output medium; if `outfilename == ""` then
 the standard error stream is used as the scanner's output medium.

**This member is not available with interactive scanners.**


 When switching streams using the above input-stream switching members
processing of the current input file ends, and continues at the file or stream
specified when calling these members.



---


* [Table of Contents](flexc++.html)* [Previous Chapter](flexc++03.html)* [Next Chapter](flexc++05.html)




---


























