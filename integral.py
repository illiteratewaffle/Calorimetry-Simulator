class Integral:

    @staticmethod
    def integrate(func, lower, upper, n=1024):
        """
        Riemann sum integral
        :param func: function to integrate
        :param lower: integral lower bound
        :param upper: integral upper bound
        :param n: number of trapezoids
        :return: definite integral
        """

        if n <= 0:
            print("n must be a positive integer")
        # force a > b by swapping
        if upper < lower:
            lower, upper = upper, lower

        dx = (upper - lower) / float(n)

        area = 0.5 * (func(lower) + func(upper))
        for i in range(1, n):
            x = lower + i * dx
            area += func(x)

        return area * dx