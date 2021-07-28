#include <iostream>

constexpr int fibonacci(const int n) {
  return n == 1 || n == 2 ? 1 : fibonacci(n - 1) + fibonacci(n - 2);
}

int main(void) {
  std::cout << fibonacci(2) << std::endl;
  return 0;
}