# How To: Is Equitable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is equitable

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert is_equitable(G, coloring)
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2)])
```

**Verification:**
```python
assert is_coloring(G, coloring)
```

### Step 3: Assign coloring = value

```python
coloring = {0: 0, 1: 1, 2: 0}
```

**Verification:**
```python
assert not is_equitable(G, coloring)
```

### Step 4: Call G.add_edges_from()

```python
G.add_edges_from([(2, 3), (2, 4), (2, 5)])
```

### Step 5: Assign unknown = 1

```python
coloring[3] = 1
```

### Step 6: Assign unknown = 1

```python
coloring[4] = 1
```

### Step 7: Assign unknown = 1

```python
coloring[5] = 1
```

**Verification:**
```python
assert is_coloring(G, coloring)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2)])
coloring = {0: 0, 1: 1, 2: 0}
assert is_equitable(G, coloring)
G.add_edges_from([(2, 3), (2, 4), (2, 5)])
coloring[3] = 1
coloring[4] = 1
coloring[5] = 1
assert is_coloring(G, coloring)
assert not is_equitable(G, coloring)
```

## Next Steps


---

*Source: test_coloring.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*