## Best practice
### Const, constexpr, and symbolic constants
1. Any variable that should not be modifiable after initialization and whose initializer is known at compile-time should be declared as constexpr.
2. Any variable that should not be modifiable after initialization and whose initializer is not known at compile-time should be declared as const.
3. Use constexpr variables to provide a name and context for your magic numbers.

### Operators
1. Use parentheses to make it clear how an expression should evaluate, even if they are technically unnecessary.
2. Strongly favor the prefix version of the increment and decrement operators, as they are generally more performant, and you’re less likely to run into strange issues with them.
3. Don’t use a variable that has a side effect applied to it more than once in a given statement. If you do, the result may be undefined.
4. Avoid using the comma operator, except within for loops.
5. Always parenthesize the conditional part of the conditional operator, and consider parenthesizing the whole thing as well.
6. Only use the conditional operator for simple conditionals where you use the result and where it enhances readability.
7. Don’t add unnecessary == or != to conditions. It makes them harder to read without offering any additional value.
8. Avoid using operator== and operator!= with floating point operands.
9. If logical NOT is intended to operate on the result of other operators, the other operators and their operands need to be enclosed in parentheses.
10. Short circuit evaluation may cause Logical OR and Logical AND to not evaluate one operand. Avoid using expressions with side effects in conjunction with these operators.
11. When mixing logical AND and logical OR in a single expression, explicitly parenthesize each operation to ensure they evaluate how you intend.

### Bit Manipulation (optional chapter)
1. Bit manipulation is one of the few times when you should unambiguously use unsigned integers (or std::bitset).

### Object Scope and Conversions
1. Keep the nesting level of your functions to 3 or less. If your function has a need for more, consider refactoring.
2. Do not add custom functionality to the std namespace.
3. Define variables in the most limited existing scope. Avoid creating new blocks whose only purpose is to limit the scope of variables.
4. If you want to define an uninitialized non-const global variable, do not use the extern keyword, otherwise C++ will think you’re trying to make a forward declaration for the variable.
5. Although constexpr variables can be given external linkage via the extern keyword, they can not be forward declared, so there is no value in giving them external linkage.
6. Dynamic initialization of global variables causes a lot of problems in C++. Avoid it whenever possible.
7. If you need global constants and your compiler is C++17 capable, prefer defining inline constexpr global variables in a header file.
8. Use local variables instead of global variables whenever possible.