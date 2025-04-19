# Q1. Use model checking to verify the correctness of a topological sorting algorithm.

from collections import deque

def topological_sort(graph):
    """
    Performs topological sorting using Kahn's algorithm.
    Raises ValueError if the graph contains a cycle.
    """
    in_degree = {node: 0 for node in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != len(graph):
        raise ValueError("Graph has at least one cycle")

    return result


def verify_topological_sort(graph, order):
    """
    Verifies that the topological order is valid for the given graph.
    Raises AssertionError if the order is incorrect.
    """
    pos = {node: i for i, node in enumerate(order)}
    for u in graph:
        for v in graph[u]:
            assert pos[u] < pos[v], f"Order invalid: {u} appears after {v}"


def run_model_check():
    test_graphs = [
        # Graph 1: Linear DAG
        {"A": ["B"], "B": ["C"], "C": []},

        # Graph 2: A splits to B and C
        {"A": ["B", "C"], "B": [], "C": []},

        # Graph 3: Diamond shape
        {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []},

        # Graph 4: Disconnected nodes
        {"A": ["B"], "B": [], "C": [], "D": []},

        # Graph 5: Cycle (should fail)
        {"A": ["B"], "B": ["C"], "C": ["A"]}
    ]

    for i, graph in enumerate(test_graphs):
        print(f"Checking Graph {i + 1}")
        try:
            order = topological_sort(graph)
            verify_topological_sort(graph, order)
            print(f"✅ Passed. Order: {order}")
        except AssertionError as e:
            print(f"❌ Assertion failed: {e}")
        except Exception as e:
            print(f"⚠️ Exception: {e}")


if __name__ == "__main__":
    run_model_check()
