# <a name="main"></a>C++ Core Guidelines

April 16, 2018


Editors:

* [Bjarne Stroustrup](http://www.stroustrup.com)
* [Herb Sutter](http://herbsutter.com/)

This is a living document under continuous improvement.
Had it been an open-source (code) project, this would have been release 0.8.
Copying, use, modification, and creation of derivative works from this project is licensed under an MIT-style license.
Contributing to this project requires agreeing to a Contributor License. See the accompanying [LICENSE](LICENSE) file for details.
We make this project available to "friendly users" to use, copy, modify, and derive from, hoping for constructive input.

Comments and suggestions for improvements are most welcome.
We plan to modify and extend this document as our understanding improves and the language and the set of available libraries improve.
When commenting, please note [the introduction](#S-introduction) that outlines our aims and general approach.

Problems:

* The sets of rules have not been completely checked for completeness, consistency, or enforceability.
* Triple question marks (???) mark known missing information
* Update reference sections; many pre-C++11 sources are too old.


* [In: Introduction](#S-introduction)
* [SS: SS-Readers](#SS-readers)

* error: ???
* exception: exception guarantee (???)
* failure: ???
* invariant: ???
* leak: ???
* library: ???
* precondition: ???
* postcondition: ???
* resource: ???

* <a name="Cplusplus03"></a>
  \[C++03]:           ISO/IEC 14882:2003(E), Programming Languages — C++
  (updated ISO and ANSI C++ Standard including the contents of (C++98) plus
  errata corrections).

### <a name="SS-readers"></a>In.target: Target readership


## <a name="SS-aims"></a>In.aims: Aims

The purpose of this document is to help developers to adopt modern C++ (C++17, C++14, and C++11) and to achieve a more uniform style across code bases.

We do not suffer the delusion that every one of these rules can be effectively applied to every code base. Upgrading old systems is hard. However, we do believe that a program that uses a rule is less error-prone and more maintainable than one that does not. Often, rules also lead to faster/easier initial development.
As far as we can tell, these rules lead to code that performs as well or better than older, more conventional techniques; they are meant to follow the zero-overhead principle ("what you don't use, you don't pay for" or "when you use an abstraction mechanism appropriately, you get at least as good performance as if you had handcoded using lower-level language constructs").
Consider these rules ideals for new code, opportunities to exploit when working on older code, and try to approximate these ideals as closely as feasible.
Remember:

### <a name="R0"></a>In.0: Don't panic!

Take the time to understand the implications of a guideline rule on your program.

They do not simply define a subset of C++ to be used (for reliability, safety, performance, or whatever).
that make the use of the most error-prone features of C++ redundant, so that they can be banned (in our set of rules).

The rules emphasize static type safety and resource safety.
For that reason, they emphasize possibilities for range checking, for avoiding dereferencing `nullptr`, for avoiding dangling pointers, and the systematic use of exceptions (via RAII).
Partly to achieve that and partly to minimize obscure code as a source of errors, the rules also emphasize simplicity and the hiding of necessary complexity behind well-specified interfaces.

Many of the rules are prescriptive.
We are uncomfortable with rules that simply state "don't do that!" without offering an alternative.
One consequence of that is that some rules can be supported only by heuristics, rather than precise and mechanically verifiable checks.
Other rules articulate general principles. For these more general rules, more detailed and specific rules provide partial checking.

These guidelines address the core of C++ and its use.
We expect that most large organizations, specific application areas, and even large projects will need further rules, possibly further restrictions, and further library support.
For example, hard-real-time programmers typically can't use free store (dynamic memory) freely and will be restricted in their choice of libraries.
We encourage the development of such more specific rules as addenda to these core guidelines.
Build your ideal small foundation library and use that, rather than lowering your level of programming to glorified assembly code.


Some rules aim to increase various forms of safety while others aim to reduce the likelihood of accidents, many do both.
The guidelines aimed at preventing accidents often ban perfectly legal C++.
However, when there are two ways of expressing an idea and one has shown itself a common source of errors and the other has not, we try to guide programmers towards the latter.

## <a name="SS-struct"></a>In.struct: The structure of this document

Each rule (guideline, suggestion) can have several parts:

* The rule itself -- e.g., **no naked `new`**
* A rule reference number -- e.g., **C.7** (the 7th rule related to classes).
  Since the major sections are not inherently ordered, we use letters as the first part of a rule reference "number".
  We leave gaps in the numbering to minimize "disruption" when we add or remove rules.
* **Reason**s (rationales) -- because programmers find it hard to follow rules they don't understand
* **Example**s -- because rules are hard to understand in the abstract; can be positive or negative
* **Alternative**s -- for "don't do this" rules
* **Exception**s -- we prefer simple general rules. However, many rules apply widely, but not universally, so exceptions must be listed
* **Enforcement** -- ideas about how the rule might be checked "mechanically"
* **See also**s -- references to related rules and/or further discussion (in this document or elsewhere)
* **Note**s (comments) -- something that needs saying that doesn't fit the other classifications
* **Discussion** -- references to more extensive rationale and/or examples placed outside the main lists of rules

Some rules are hard to check mechanically, but they all meet the minimal criteria that an expert programmer can spot many violations without too much trouble.
We hope that "mechanical" tools will improve with time to approximate what such an expert programmer notices.
Also, we assume that the rules will be refined over time to make them more precise and checkable.

A rule is aimed at being simple, rather than carefully phrased to mention every alternative and special case.
If you don't understand a rule or disagree with it, please visit its **Discussion**.
If you feel that a discussion is missing or incomplete, enter an [Issue](https://github.com/isocpp/CppCoreGuidelines/issues)
explaining your concerns and possibly a corresponding PR.

This is not a language manual.
It is meant to be helpful, rather than complete, fully accurate on technical details, or a guide to existing code.

# <a name="S-introduction"></a>In: Introduction

This is a set of core guidelines for modern C++, C++17, C++14, and C++11, taking likely future enhancements and ISO Technical Specifications (TSs) into account.
The aim is to help C++ programmers to write simpler, more efficient, more maintainable code.

Introduction summary:

* <a name="Henricson97"></a>
  \[Henricson97]:     M. Henricson and E. Nyquist. Industrial Strength C++
  (Prentice Hall, 1997).
