#include "fibonacci.hpp"

int fib(int number)
{
    if (number < 0)
    {
        // return -1 to indicate number is invalid
        return -1;
    }
    else if (0 == number)
        return 0;
    else if (1 == number || 2 == number)
        return 1;
    else
    {
        return fib(number - 1) + fib(number - 2);
    }
}