// use this link to download catch.hpp
// https://raw.githubusercontent.com/catchorg/Catch2/v2.x/single_include/catch2/catch.hpp

#define CATCH_CONFIG_MAIN // will supply the executable with a proper main()
#include "power.hpp"
#include "catch2.hpp"

TEST_CASE("simple test case", "[simple]")
{
    // The REQUIRE is the main assertion method in Catch2. If the result of the
    // operation in braces is false (or zero), then the test fails and the runner
    // stops.
    REQUIRE(1 == 1);
}

TEST_CASE("squares of", "[power]")
{
    SECTION("zero")
    {
        REQUIRE(square(0) == 0);
    }
    SECTION("negative numbers")
    {
        REQUIRE(square(-1) == 1);
        REQUIRE(square(-2) == 4);
        REQUIRE(square(-3) == 9);
        REQUIRE(square(-11) == 121);
    }
    SECTION("positive numbers")
    {
        REQUIRE(square(1) == 1);
        REQUIRE(square(2) == 4);
        REQUIRE(square(3) == 9);
        REQUIRE(square(4) == 16);
    }
}

TEST_CASE("cubes of", "[power]")
{
    SECTION("zero")
    {
        REQUIRE(cube(0) == 0);
    }
    SECTION("negative numbers")
    {
        REQUIRE(cube(-1) == 1); // errors!
        REQUIRE(cube(-2) == 8);
        REQUIRE(cube(-3) == 27);
        REQUIRE(cube(-11) == 1331);
    }
    SECTION("positive numbers")
    {
        REQUIRE(cube(1) == 1);
        REQUIRE(cube(2) == 8);
        REQUIRE(cube(3) == 27);
        REQUIRE(cube(4) == 64);
    }
}