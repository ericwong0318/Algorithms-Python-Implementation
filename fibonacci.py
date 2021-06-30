class Math(object):
    # time: O(2^n)
    # space: O(n)
    def fib_recursive(self, n):
        # base case
        if n == 0 or n == 1:
            return n
        # recursive steps
        else:
            return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)

    # time: O(2^n)
    # space: O(1)
    def fib_iterative(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b  # simultaneously
        return a

    # time: O(n)
    # space: O(n)
    def fib_dynamic_programming(self, n):
        cache = {}
        return self._fib_dynamic_programming(n, cache)

    def _fib_dynamic_programming(self, n, cache):
        # base case
        if n == 0 or n == 1:
            return n
        # memoization
        if n in cache:
            return cache[n]
        # recursive steps
        cache[n] = self._fib_dynamic_programming(n - 1, cache) + self._fib_dynamic_programming(n - 2, cache)
        return cache[n]
