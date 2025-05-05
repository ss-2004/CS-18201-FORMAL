# Lab 5: Fixed Points and Behavioral Properties
# Use Python to calculate a fixed point for a simple example.

def fixed_point(func, x0, max_iter=10):
    for _ in range(max_iter):
        x1 = func(x0)
        if x1 == x0:
            return x1
        x0 = x1
    return None

# Example: Fixed point of f(x) = x^2 for initial value x0 = 1
f = lambda x: x**2
x0 = 1
print(f"Fixed point: {fixed_point(f, x0)}")