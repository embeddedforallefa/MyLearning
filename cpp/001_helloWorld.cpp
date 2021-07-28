// Problem: Let your computer Say "Hello World"

#include <iostream> // for std::cout

int main() {
  std::cout << "Hello world!"; // print Hello world! to console

  std::cout << std::endl; // adds a new line

  return 0;
}

// ***** summary *****
// #include is a prepreocessor directive to include header files that your file
// needs

// std::cout always go on the left-hand side of the statement.

// std::cout is used to output a value (cout = character output)

// << is used with std::cout, and shows the direction that data is moving (if
// std::cout represents the console, the output data is moving from the variable
// to the console). std::cout << 4 moves the value of 4 to the console