import math
from itertools import product
from statistics import mean, pstdev


def compute_values(expr: str, variables: list, domains: dict):
    """Evaluate expression over the cartesian product of domains."""
    domain_values = [domains[v].values() for v in variables]
    combos = list(product(*domain_values))
    env = {name: None for name in variables}
    env.update(math.__dict__)
    results = []
    for combo in combos:
        for v, val in zip(variables, combo):
            env[v] = val
        results.append(eval(expr, {"__builtins__": {}}, env))
    return combos, results


def compute_stats(values):
    """Compute min, max, mean, and population standard deviation."""
    if not values:
        raise ValueError("No values to compute stats")
    return {
        "min": min(values),
        "max": max(values),
        "mean": mean(values),
        "std": pstdev(values),
    }
