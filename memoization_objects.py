class Fib():
    cache = {}

    def __call__(self, n):
        if n in self.cache:
            ans = self.cache[n]

        if n <= 2:
            ans = 1
            self.cache[n] = ans
        else:
            ans = self(n - 2) + self(n - 1)
            self.cache[n] = ans

            return ans

