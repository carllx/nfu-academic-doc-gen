# How To: Domrel Png

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test domrel png

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(1, 2), (2, 3), (2, 4), (2, 6), (3, 5), (4, 5), (5, 2)]
```

**Verification:**
```python
assert result == {2: 1, 3: 2, 4: 2, 5: 2, 6: 2}
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert result == {1: 2, 2: 6, 3: 5, 4: 5, 5: 2}
```

### Step 3: Assign result = nx.immediate_dominators(...)

```python
result = nx.immediate_dominators(G, 1)
```

**Verification:**
```python
assert result == {2: 1, 3: 2, 4: 2, 5: 2, 6: 2}
```

### Step 4: Assign result = nx.immediate_dominators(...)

```python
result = nx.immediate_dominators(G.reverse(copy=False), 6)
```

**Verification:**
```python
assert result == {1: 2, 2: 6, 3: 5, 4: 5, 5: 2}
```


## Complete Example

```python
# Workflow
edges = [(1, 2), (2, 3), (2, 4), (2, 6), (3, 5), (4, 5), (5, 2)]
G = nx.DiGraph(edges)
result = nx.immediate_dominators(G, 1)
assert result == {2: 1, 3: 2, 4: 2, 5: 2, 6: 2}
result = nx.immediate_dominators(G.reverse(copy=False), 6)
assert result == {1: 2, 2: 6, 3: 5, 4: 5, 5: 2}
```

## Next Steps


---

*Source: test_dominance.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*