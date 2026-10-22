class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places



        #  MAKE SURE ==> x_new = x_old - ((alpha) f'(x_old))    ---------> return this x_new

        output = init

        for _ in range(iterations):
            der = 2 * output
            output = output - learning_rate * der

        return round(output,5)

