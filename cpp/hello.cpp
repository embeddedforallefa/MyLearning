#include <iostream> // for std::cout

int main()
{
    std::cout << "Hello world!"; // print Hello world! to console

    std::cout << "Enter a number: "; // ask user for a number
    int x{};                         // define variable x to hold user input
    std::cin >> x;                   // get number from keyboard and store it in variable x
    std::cout << "You entered " << x << '\n';

    return 0;
}

// summary
// std::cin and std::cout always go on the left-hand side of the statement.
// std::cout is used to output a value (cout = character output)
// std::cin is used to get an input value (cin = character input)
// << is used with std::cout, and shows the direction that data is moving (if std::cout represents the console, the output data is moving from the variable to the console). std::cout << 4 moves the value of 4 to the console
// >> is used with std::cin, and shows the direction that data is moving (if std::cin represents the keyboard, the input data is moving from the keyboard to the variable). std::cin >> x moves the value the user entered from the keyboard into x
