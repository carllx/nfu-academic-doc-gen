# How To: Wrong Parameters S1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wrong parameters S1

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

### Step 1: Assign G = nx.geometric_soft_configuration_graph(...)

```python
G = nx.geometric_soft_configuration_graph(beta=1.5, gamma=3.5, mean_degree=10, seed=42)
```

### Step 2: Assign kappas = value

```python
kappas = {i: 10 for i in range(1000)}
```

### Step 3: Assign G = nx.geometric_soft_configuration_graph(...)

```python
G = nx.geometric_soft_configuration_graph(beta=1.5, kappas=kappas, gamma=2.3, seed=42)
```

### Step 4: Assign G = nx.geometric_soft_configuration_graph(...)

```python
G = nx.geometric_soft_configuration_graph(beta=1.5, seed=42)
```


## Complete Example

```python
# Workflow
with pytest.raises(nx.NetworkXError, match='Please provide either kappas, or all 3 of: n, gamma and mean_degree.'):
    G = nx.geometric_soft_configuration_graph(beta=1.5, gamma=3.5, mean_degree=10, seed=42)
with pytest.raises(nx.NetworkXError, match='When kappas is input, n, gamma and mean_degree must not be.'):
    kappas = {i: 10 for i in range(1000)}
    G = nx.geometric_soft_configuration_graph(beta=1.5, kappas=kappas, gamma=2.3, seed=42)
with pytest.raises(nx.NetworkXError, match='Please provide either kappas, or all 3 of: n, gamma and mean_degree.'):
    G = nx.geometric_soft_configuration_graph(beta=1.5, seed=42)
```

## Next Steps


---

*Source: test_geometric.py:422 | Complexity: Intermediate | Last updated: 2026-06-02*