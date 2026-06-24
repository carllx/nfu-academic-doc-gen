# How To: Set Attributes S1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set attributes S1

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
G = nx.geometric_soft_configuration_graph(beta=1.5, n=100, gamma=2.7, mean_degree=10, seed=42)
```

**Verification:**
```python
assert len(kappas) == 100
```

### Step 2: Assign kappas = nx.get_node_attributes(...)

```python
kappas = nx.get_node_attributes(G, 'kappa')
```

**Verification:**
```python
assert len(thetas) == 100
```

### Step 3: Assign thetas = nx.get_node_attributes(...)

```python
thetas = nx.get_node_attributes(G, 'theta')
```

**Verification:**
```python
assert len(radii) == 100
```

### Step 4: Assign radii = nx.get_node_attributes(...)

```python
radii = nx.get_node_attributes(G, 'radius')
```

**Verification:**
```python
assert len(radii) == 100
```


## Complete Example

```python
# Workflow
G = nx.geometric_soft_configuration_graph(beta=1.5, n=100, gamma=2.7, mean_degree=10, seed=42)
kappas = nx.get_node_attributes(G, 'kappa')
assert len(kappas) == 100
thetas = nx.get_node_attributes(G, 'theta')
assert len(thetas) == 100
radii = nx.get_node_attributes(G, 'radius')
assert len(radii) == 100
```

## Next Steps


---

*Source: test_geometric.py:378 | Complexity: Intermediate | Last updated: 2026-06-02*