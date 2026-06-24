# How To: Bipartite Degrees

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bipartite degrees

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
assert dict(u) == {1: 2, 3: 2}
```

### Step 2: Assign X = value

```python
X = {1, 3}
```

**Verification:**
```python
assert dict(d) == {0: 1, 2: 2, 4: 1}
```

### Step 3: Assign Y = value

```python
Y = {0, 2, 4}
```

### Step 4: Assign unknown = bipartite.degrees(...)

```python
u, d = bipartite.degrees(G, Y)
```

**Verification:**
```python
assert dict(u) == {1: 2, 3: 2}
```


## Complete Example

```python
# Workflow
G = nx.path_graph(5)
X = {1, 3}
Y = {0, 2, 4}
u, d = bipartite.degrees(G, Y)
assert dict(u) == {1: 2, 3: 2}
assert dict(d) == {0: 1, 2: 2, 4: 1}
```

## Next Steps


---

*Source: test_basic.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*