# How To: Weightkey

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weightkey

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `networkx`
- `networkx.algorithms.isomorphism`


## Step-by-Step Guide

### Step 1: Assign g1 = nx.DiGraph(...)

```python
g1 = nx.DiGraph()
```

**Verification:**
```python
assert nx.is_isomorphic(g1, g2)
```

### Step 2: Assign g2 = nx.DiGraph(...)

```python
g2 = nx.DiGraph()
```

**Verification:**
```python
assert nx.is_isomorphic(g1, g2, edge_match=em)
```

### Step 3: Call g1.add_edge()

```python
g1.add_edge('A', 'B', weight=1)
```

**Verification:**
```python
assert not nx.is_isomorphic(g1, g2, edge_match=em)
```

### Step 4: Call g2.add_edge()

```python
g2.add_edge('C', 'D', weight=0)
```

**Verification:**
```python
assert nx.is_isomorphic(g1, g2, edge_match=em)
```

### Step 5: Assign em = iso.numerical_edge_match(...)

```python
em = iso.numerical_edge_match('nonexistent attribute', 1)
```

**Verification:**
```python
assert nx.is_isomorphic(g1, g2, edge_match=em)
```

### Step 6: Assign em = iso.numerical_edge_match(...)

```python
em = iso.numerical_edge_match('weight', 1)
```

**Verification:**
```python
assert not nx.is_isomorphic(g1, g2, edge_match=em)
```

### Step 7: Assign g2 = nx.DiGraph(...)

```python
g2 = nx.DiGraph()
```

### Step 8: Call g2.add_edge()

```python
g2.add_edge('C', 'D')
```

**Verification:**
```python
assert nx.is_isomorphic(g1, g2, edge_match=em)
```


## Complete Example

```python
# Workflow
g1 = nx.DiGraph()
g2 = nx.DiGraph()
g1.add_edge('A', 'B', weight=1)
g2.add_edge('C', 'D', weight=0)
assert nx.is_isomorphic(g1, g2)
em = iso.numerical_edge_match('nonexistent attribute', 1)
assert nx.is_isomorphic(g1, g2, edge_match=em)
em = iso.numerical_edge_match('weight', 1)
assert not nx.is_isomorphic(g1, g2, edge_match=em)
g2 = nx.DiGraph()
g2.add_edge('C', 'D')
assert nx.is_isomorphic(g1, g2, edge_match=em)
```

## Next Steps


---

*Source: test_vf2userfunc.py:57 | Complexity: Advanced | Last updated: 2026-06-02*