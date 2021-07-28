// use this link to download catch.hpp
// https://raw.githubusercontent.com/catchorg/Catch2/v2.x/single_include/catch2/catch.hpp

#define CATCH_CONFIG_MAIN // will supply the executable with a proper main()
#include "fibonacci.hpp"
#include "catch2.hpp"

// fibonacci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
// x(n) = x(n-1) + x(n-2)

TEST_CASE("fibonacci sequence")
{
    // The REQUIRE is the main assertion method in Catch2. If the result of the
    // operation in braces is false (or zero), then the test fails and the runner
    // stops.
    SECTION("zero")
    {
        REQUIRE(fib(0) == 0);
    }

    SECTION("positive numbers")
    {
        REQUIRE(fib(1) == 1);
        REQUIRE(fib(2) == 1);
        REQUIRE(fib(3) == 2);
        REQUIRE(fib(9) == 34);
    }

    SECTION("negetive numbers")
    {
        REQUIRE(fib(-1) == -1);
        REQUIRE(fib(-10) == -1);
    }
}