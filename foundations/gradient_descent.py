class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        min_num = init
        for _ in range(iterations):
            der = 2* min_num
            min_num = min_num - learning_rate * der

        return round(min_num,5)