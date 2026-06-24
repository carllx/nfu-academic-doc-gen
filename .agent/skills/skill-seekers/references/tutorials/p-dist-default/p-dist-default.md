# How To: P Dist Default

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests default p_dict = 0.5 returns graph with edge count <= RGG with
same n, radius, dim and positions

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

### Step 1: 'Tests default p_dict = 0.5 returns graph with edge count <= RGG with\n        same n, radius, dim and positions\n        '

```python
'Tests default p_dict = 0.5 returns graph with edge count <= RGG with\n        same n, radius, dim and positions\n        '
```

**Verification:**
```python
assert len(SRGG.edges()) <= len(RGG.edges())
```

### Step 2: Assign nodes = 50

```python
nodes = 50
```

### Step 3: Assign dim = 2

```python
dim = 2
```

### Step 4: Assign pos = value

```python
pos = {v: [random.random() for i in range(dim)] for v in range(nodes)}
```

### Step 5: Assign RGG = nx.random_geometric_graph(...)

```python
RGG = nx.random_geometric_graph(50, 0.25, pos=pos)
```

### Step 6: Assign SRGG = nx.soft_random_geometric_graph(...)

```python
SRGG = nx.soft_random_geometric_graph(50, 0.25, pos=pos)
```

**Verification:**
```python
assert len(SRGG.edges()) <= len(RGG.edges())
```


## Complete Example

```python
# Workflow
'Tests default p_dict = 0.5 returns graph with edge count <= RGG with\n        same n, radius, dim and positions\n        '
nodes = 50
dim = 2
pos = {v: [random.random() for i in range(dim)] for v in range(nodes)}
RGG = nx.random_geometric_graph(50, 0.25, pos=pos)
SRGG = nx.soft_random_geometric_graph(50, 0.25, pos=pos)
assert len(SRGG.edges()) <= len(RGG.edges())
```

## Next Steps


---

*Source: test_geometric.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*