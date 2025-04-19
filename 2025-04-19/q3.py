# Q3. Implement formal verification of loop invariants for fixed point iterative algorithms.

import math

def g(x):
    return math.cos(x)

def is_invariant_preserved(x):
    return 0.0 <= x <= 1.0

def fixed_point_iteration(initial_guess, tolerance=1e-7, max_iterations=100):

    x = initial_guess
    assert is_invariant_preserved(x), f"Initial guess {x} violates loop invariant."

    for i in range(max_iterations):
        x_new = g(x)

        assert is_invariant_preserved(x_new), f"Loop invariant violated at iteration {i+1}, x = {x_new}"

        if abs(x_new - x) < tolerance:
            print(f"Converged to {x_new} after {i+1} iterations.")
            return x_new

        x = x_new

    raise Exception(f"Did not converge after {max_iterations} iterations.")

def main():
    try:
        result = fixed_point_iteration(initial_guess=0.5)
        print(f"Fixed-point result: {result}")
    except AssertionError as ae:
        print(f"Verification failed: {ae}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()