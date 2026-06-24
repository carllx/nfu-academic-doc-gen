# How To: Compare Mean Kappas Different Gammas S1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare mean kappas different gammas S1

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

### Step 1: Assign G1 = nx.geometric_soft_configuration_graph(...)

```python
G1 = nx.geometric_soft_configuration_graph(beta=1.5, n=20, gamma=2.7, mean_degree=5, seed=42)
```

**Verification:**
```python
assert math.fabs(mean_kappas1 - mean_kappas2) < 1
```

### Step 2: Assign G2 = nx.geometric_soft_configuration_graph(...)

```python
G2 = nx.geometric_soft_configuration_graph(beta=1.5, n=20, gamma=3.5, mean_degree=5, seed=42)
```

### Step 3: Assign kappas1 = nx.get_node_attributes(...)

```python
kappas1 = nx.get_node_attributes(G1, 'kappa')
```

### Step 4: Assign mean_kappas1 = value

```python
mean_kappas1 = sum(kappas1.values()) / len(kappas1)
```

### Step 5: Assign kappas2 = nx.get_node_attributes(...)

```python
kappas2 = nx.get_node_attributes(G2, 'kappa')
```

### Step 6: Assign mean_kappas2 = value

```python
mean_kappas2 = sum(kappas2.values()) / len(kappas2)
```

**Verification:**
```python
assert math.fabs(mean_kappas1 - mean_kappas2) < 1
```


## Complete Example

```python
# Workflow
G1 = nx.geometric_soft_configuration_graph(beta=1.5, n=20, gamma=2.7, mean_degree=5, seed=42)
G2 = nx.geometric_soft_configuration_graph(beta=1.5, n=20, gamma=3.5, mean_degree=5, seed=42)
kappas1 = nx.get_node_attributes(G1, 'kappa')
mean_kappas1 = sum(kappas1.values()) / len(kappas1)
kappas2 = nx.get_node_attributes(G2, 'kappa')
mean_kappas2 = sum(kappas2.values()) / len(kappas2)
assert math.fabs(mean_kappas1 - mean_kappas2) < 1
```

## Next Steps


---

*Source: test_geometric.py:477 | Complexity: Intermediate | Last updated: 2026-06-02*