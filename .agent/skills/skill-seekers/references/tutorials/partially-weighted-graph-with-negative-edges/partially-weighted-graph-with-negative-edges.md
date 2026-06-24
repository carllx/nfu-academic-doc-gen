# How To: Partially Weighted Graph With Negative Edges

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partially weighted graph with negative edges

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nx.johnson(G) == nx.johnson(H)
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2), (2, 0), (1, 0)])
```

**Verification:**
```python
assert nx.johnson(G) != nx.johnson(I)
```

### Step 3: Assign unknown = value

```python
G[1][0]['weight'] = -2
```

### Step 4: Assign unknown = 3

```python
G[0][1]['weight'] = 3
```

### Step 5: Assign unknown = value

```python
G[1][2]['weight'] = -4
```

### Step 6: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 7: Assign unknown = 1

```python
H[2][0]['weight'] = 1
```

### Step 8: Assign I = G.copy(...)

```python
I = G.copy()
```

### Step 9: Assign unknown = 8

```python
I[2][0]['weight'] = 8
```

**Verification:**
```python
assert nx.johnson(G) == nx.johnson(H)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (1, 0)])
G[1][0]['weight'] = -2
G[0][1]['weight'] = 3
G[1][2]['weight'] = -4
H = G.copy()
H[2][0]['weight'] = 1
I = G.copy()
I[2][0]['weight'] = 8
assert nx.johnson(G) == nx.johnson(H)
assert nx.johnson(G) != nx.johnson(I)
```

## Next Steps


---

*Source: test_weighted.py:961 | Complexity: Advanced | Last updated: 2026-06-02*