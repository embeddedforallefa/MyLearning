The smallest unit of memory is a binary digit, also called a bit. The smallest unit amount of memory that can be addressed directly is a byte. The modern standard is that a byte equals 8 bits.

A data type tells the compiler how to interpret the contents of memory in some meaningful way.

C++ comes with support for many fundamental data types, including floating point numbers, integers, boolean, chars, null pointers, and void.

Void is used to indicate no type. It is primarily used to indicate that a function does not return a value.

Different types take different amounts of memory, and the amount of memory used may vary by machine. See 4.3 -- Object sizes and the sizeof operator for a table indicating the minimum size for each fundamental type.

The sizeof operator can be used to return the size of a type in bytes.

Signed integers are used for holding positive and negative whole numbers, including 0. The set of values that a specific data type can hold is called its range. When using integers, keep an eye out for overflow and integer division problems.

Unsigned integers only hold positive numbers, and should generally be avoided unless you’re doing bit-level manipulation.

Fixed-width integers exist to define integer types with guaranteed sizes. Favor the std::int_fast#_t and std::int_least#_t integers when you need a fixed size guaranteed to be at least a certain size. std::int8_t and std::uint8_t should generally be avoided, as they tend to behave like chars instead of integers.

size_t is an unsigned integral type that is used to represent the size or length of objects.

Scientific notation is a shorthand way of writing lengthy numbers. C++ supports scientific notation in conjunction with floating point numbers. The digits in the significand (the part before the e) are called the significant digits.

Floating point is a set of types designed to hold real numbers (including those with a fractional component). The precision of a number defines how many significant digits it can represent without information loss. A rounding error can occur when too many significant digits are stored in a floating point number that can’t hold that much precision. Rounding errors happen all the time, even with simple numbers such as 0.1. Because of this, you shouldn’t compare floating point numbers directly.

The boolean type is used to store a true or false value.

If statements allow us to execute one or more lines of code if some condition is true. Multiple statements can be executed if they are put inside a block (inside curly braces). The conditional expression of an if statement is interpreted as a boolean value.

Char is used to store values that are interpreted as an ASCII character. When using chars, be careful not to mix up ASCII code values and numbers. Printing a char as an integer value requires use of static_cast.

Angled brackets are typically used in C++ to represent something that needs a parameterizable type. This is used with static_cast to determine what data type the argument should be converted to (e.g. static_cast<int>(x) will convert x to an int).

A constant is a fixed value that may not be changed. C++ supports two types of constants: literal constants, and symbolic constants.

Literals are values inserted directly into the code. Literals have types, and literal suffixes can be used to change the type of a literal from default.

Const variables are variables that can’t be changed after being initialized. Const variables can be either runtime or compile-time constants. constexpr variables must be compile-time constants.

Don’t use magic numbers in your code. Instead, use symbolic constants.