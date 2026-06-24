# How To: Add Star

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add star

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

**Verification:**
```python
assert edges_equal(G.edges(nlist), [(12, 13), (12, 14), (12, 15)])
```

### Step 2: Assign nlist = value

```python
nlist = [12, 13, 14, 15]
```

**Verification:**
```python
assert edges_equal(G.edges(nlist, data=True), [(12, 13, {'weight': 2.0}), (12, 14, {'weight': 2.0}), (12, 15, {'weight': 2.0})])
```

### Step 3: Call nx.add_star()

```python
nx.add_star(G, nlist)
```

**Verification:**
```python
assert nodes_equal(G, list(self.G) + nlist)
```

### Step 4: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

**Verification:**
```python
assert nodes_equal(G.nodes, self.Gnodes)
```

### Step 5: Call nx.add_star()

```python
nx.add_star(G, nlist, weight=2.0)
```

**Verification:**
```python
assert edges_equal(G.edges, self.G.edges)
```

### Step 6: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

### Step 7: Assign nlist = value

```python
nlist = [12]
```

### Step 8: Call nx.add_star()

```python
nx.add_star(G, nlist)
```

**Verification:**
```python
assert nodes_equal(G, list(self.G) + nlist)
```

### Step 9: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

### Step 10: Assign nlist = value

```python
nlist = []
```

### Step 11: Call nx.add_star()

```python
nx.add_star(G, nlist)
```

**Verification:**
```python
assert nodes_equal(G.nodes, self.Gnodes)
```


## Complete Example

```python
# Workflow
G = self.G.copy()
nlist = [12, 13, 14, 15]
nx.add_star(G, nlist)
assert edges_equal(G.edges(nlist), [(12, 13), (12, 14), (12, 15)])
G = self.G.copy()
nx.add_star(G, nlist, weight=2.0)
assert edges_equal(G.edges(nlist, data=True), [(12, 13, {'weight': 2.0}), (12, 14, {'weight': 2.0}), (12, 15, {'weight': 2.0})])
G = self.G.copy()
nlist = [12]
nx.add_star(G, nlist)
assert nodes_equal(G, list(self.G) + nlist)
G = self.G.copy()
nlist = []
nx.add_star(G, nlist)
assert nodes_equal(G.nodes, self.Gnodes)
assert edges_equal(G.edges, self.G.edges)
```

## Next Steps


---

*Source: test_function.py:82 | Complexity: Advanced | Last updated: 2026-06-02*