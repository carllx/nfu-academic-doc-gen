# How To: Di Cache Reset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test di cache reset

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `test_graph`
- `test_graph`
- `test_graph`


## Step-by-Step Guide

### Step 1: Assign G = self.K3.copy(...)

```python
G = self.K3.copy()
```

**Verification:**
```python
assert id(G.succ) == id(old_succ)
```

### Step 2: Assign old_succ = value

```python
old_succ = G.succ
```

**Verification:**
```python
assert id(G.adj) == id(old_adj)
```

### Step 3: Assign old_adj = value

```python
old_adj = G.adj
```

**Verification:**
```python
assert id(G.succ) != id(old_succ)
```

### Step 4: Assign G._succ = value

```python
G._succ = {}
```

**Verification:**
```python
assert id(G.adj) != id(old_adj)
```

### Step 5: Assign old_pred = value

```python
old_pred = G.pred
```

**Verification:**
```python
assert id(G.pred) == id(old_pred)
```

### Step 6: Assign G._pred = value

```python
G._pred = {}
```

**Verification:**
```python
assert id(G.pred) != id(old_pred)
```


## Complete Example

```python
# Workflow
G = self.K3.copy()
old_succ = G.succ
assert id(G.succ) == id(old_succ)
old_adj = G.adj
assert id(G.adj) == id(old_adj)
G._succ = {}
assert id(G.succ) != id(old_succ)
assert id(G.adj) != id(old_adj)
old_pred = G.pred
assert id(G.pred) == id(old_pred)
G._pred = {}
assert id(G.pred) != id(old_pred)
```

## Next Steps


---

*Source: test_digraph.py:135 | Complexity: Intermediate | Last updated: 2026-06-02*