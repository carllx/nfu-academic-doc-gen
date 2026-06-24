# How To: Bridge Cc

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bridge cc

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_kcomponents`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign cc2 = value

```python
cc2 = [(1, 2, 4, 3, 1, 4), (8, 9, 10, 8), (11, 12, 13, 11)]
```

**Verification:**
```python
assert bridge_ccs == target_ccs
```

### Step 2: Assign bridges = value

```python
bridges = [(4, 8), (3, 5), (20, 21), (22, 23, 24)]
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph(it.chain(*(pairwise(path) for path in cc2 + bridges)))
```

### Step 4: Assign bridge_ccs = fset(...)

```python
bridge_ccs = fset(bridge_components(G))
```

### Step 5: Assign target_ccs = fset(...)

```python
target_ccs = fset([{1, 2, 3, 4}, {5}, {8, 9, 10}, {11, 12, 13}, {20}, {21}, {22}, {23}, {24}])
```

**Verification:**
```python
assert bridge_ccs == target_ccs
```

### Step 6: Call _check_edge_connectivity()

```python
_check_edge_connectivity(G)
```


## Complete Example

```python
# Workflow
cc2 = [(1, 2, 4, 3, 1, 4), (8, 9, 10, 8), (11, 12, 13, 11)]
bridges = [(4, 8), (3, 5), (20, 21), (22, 23, 24)]
G = nx.Graph(it.chain(*(pairwise(path) for path in cc2 + bridges)))
bridge_ccs = fset(bridge_components(G))
target_ccs = fset([{1, 2, 3, 4}, {5}, {8, 9, 10}, {11, 12, 13}, {20}, {21}, {22}, {23}, {24}])
assert bridge_ccs == target_ccs
_check_edge_connectivity(G)
```

## Next Steps


---

*Source: test_edge_kcomponents.py:244 | Complexity: Intermediate | Last updated: 2026-06-02*