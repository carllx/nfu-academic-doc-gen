# How To: Mean Degree Influence On Connectivity S1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mean degree influence on connectivity S1

## Prerequisites

**Required Modules:**
- `math`
- `random`
- `itertools`
- `pytest`
- `networkx`
- `string`
- `string`
- `string`


## Step-by-Step Guide

### Step 1: Assign low_mean_degree = 2

```python
low_mean_degree = 2
```

**Verification:**
```python
assert nx.number_connected_components(G_low) > nx.number_connected_components(G_high)
```

### Step 2: Assign high_mean_degree = 20

```python
high_mean_degree = 20
```

### Step 3: Assign G_low = nx.geometric_soft_configuration_graph(...)

```python
G_low = nx.geometric_soft_configuration_graph(beta=1.2, n=100, gamma=2.7, mean_degree=low_mean_degree, seed=42)
```

### Step 4: Assign G_high = nx.geometric_soft_configuration_graph(...)

```python
G_high = nx.geometric_soft_configuration_graph(beta=1.2, n=100, gamma=2.7, mean_degree=high_mean_degree, seed=42)
```

**Verification:**
```python
assert nx.number_connected_components(G_low) > nx.number_connected_components(G_high)
```


## Complete Example

```python
# Workflow
low_mean_degree = 2
high_mean_degree = 20
G_low = nx.geometric_soft_configuration_graph(beta=1.2, n=100, gamma=2.7, mean_degree=low_mean_degree, seed=42)
G_high = nx.geometric_soft_configuration_graph(beta=1.2, n=100, gamma=2.7, mean_degree=high_mean_degree, seed=42)
assert nx.number_connected_components(G_low) > nx.number_connected_components(G_high)
```

## Next Steps


---

*Source: test_geometric.py:463 | Complexity: Intermediate | Last updated: 2026-06-02*