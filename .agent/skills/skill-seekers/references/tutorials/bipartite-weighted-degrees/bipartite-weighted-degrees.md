# How To: Bipartite Weighted Degrees

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bipartite weighted degrees

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5)
```

**Verification:**
```python
assert dict(u) == {1: 1.1, 3: 2}
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 1, weight=0.1, other=0.2)
```

**Verification:**
```python
assert dict(d) == {0: 0.1, 2: 2, 4: 1}
```

### Step 3: Assign X = value

```python
X = {1, 3}
```

**Verification:**
```python
assert dict(u) == {1: 1.2, 3: 2}
```

### Step 4: Assign Y = value

```python
Y = {0, 2, 4}
```

**Verification:**
```python
assert dict(d) == {0: 0.2, 2: 2, 4: 1}
```

### Step 5: Assign unknown = bipartite.degrees(...)

```python
u, d = bipartite.degrees(G, Y, weight='weight')
```

**Verification:**
```python
assert dict(u) == {1: 1.1, 3: 2}
```

### Step 6: Assign unknown = bipartite.degrees(...)

```python
u, d = bipartite.degrees(G, Y, weight='other')
```

**Verification:**
```python
assert dict(u) == {1: 1.2, 3: 2}
```


## Complete Example

```python
# Workflow
G = nx.path_graph(5)
G.add_edge(0, 1, weight=0.1, other=0.2)
X = {1, 3}
Y = {0, 2, 4}
u, d = bipartite.degrees(G, Y, weight='weight')
assert dict(u) == {1: 1.1, 3: 2}
assert dict(d) == {0: 0.1, 2: 2, 4: 1}
u, d = bipartite.degrees(G, Y, weight='other')
assert dict(u) == {1: 1.2, 3: 2}
assert dict(d) == {0: 0.2, 2: 2, 4: 1}
```

## Next Steps


---

*Source: test_basic.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*