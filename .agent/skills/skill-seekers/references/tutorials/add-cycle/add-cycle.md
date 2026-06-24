# How To: Add Cycle

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add cycle

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
assert sorted(G.edges(nlist)) in oklists
```

### Step 2: Assign nlist = value

```python
nlist = [12, 13, 14, 15]
```

**Verification:**
```python
assert sorted(G.edges(nlist, data=True)) in oklists
```

### Step 3: Assign oklists = value

```python
oklists = [[(12, 13), (12, 15), (13, 14), (14, 15)], [(12, 13), (13, 14), (14, 15), (15, 12)]]
```

**Verification:**
```python
assert nodes_equal(G, list(self.G) + nlist)
```

### Step 4: Call nx.add_cycle()

```python
nx.add_cycle(G, nlist)
```

**Verification:**
```python
assert nodes_equal(G.nodes, self.Gnodes)
```

### Step 5: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

**Verification:**
```python
assert edges_equal(G.edges, self.G.edges)
```

### Step 6: Assign oklists = value

```python
oklists = [[(12, 13, {'weight': 1.0}), (12, 15, {'weight': 1.0}), (13, 14, {'weight': 1.0}), (14, 15, {'weight': 1.0})], [(12, 13, {'weight': 1.0}), (13, 14, {'weight': 1.0}), (14, 15, {'weight': 1.0}), (15, 12, {'weight': 1.0})]]
```

### Step 7: Call nx.add_cycle()

```python
nx.add_cycle(G, nlist, weight=1.0)
```

**Verification:**
```python
assert sorted(G.edges(nlist, data=True)) in oklists
```

### Step 8: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

### Step 9: Assign nlist = value

```python
nlist = [12]
```

### Step 10: Call nx.add_cycle()

```python
nx.add_cycle(G, nlist)
```

**Verification:**
```python
assert nodes_equal(G, list(self.G) + nlist)
```

### Step 11: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

### Step 12: Assign nlist = value

```python
nlist = []
```

### Step 13: Call nx.add_cycle()

```python
nx.add_cycle(G, nlist)
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
oklists = [[(12, 13), (12, 15), (13, 14), (14, 15)], [(12, 13), (13, 14), (14, 15), (15, 12)]]
nx.add_cycle(G, nlist)
assert sorted(G.edges(nlist)) in oklists
G = self.G.copy()
oklists = [[(12, 13, {'weight': 1.0}), (12, 15, {'weight': 1.0}), (13, 14, {'weight': 1.0}), (14, 15, {'weight': 1.0})], [(12, 13, {'weight': 1.0}), (13, 14, {'weight': 1.0}), (14, 15, {'weight': 1.0}), (15, 12, {'weight': 1.0})]]
nx.add_cycle(G, nlist, weight=1.0)
assert sorted(G.edges(nlist, data=True)) in oklists
G = self.G.copy()
nlist = [12]
nx.add_cycle(G, nlist)
assert nodes_equal(G, list(self.G) + nlist)
G = self.G.copy()
nlist = []
nx.add_cycle(G, nlist)
assert nodes_equal(G.nodes, self.Gnodes)
assert edges_equal(G.edges, self.G.edges)
```

## Next Steps


---

*Source: test_function.py:162 | Complexity: Advanced | Last updated: 2026-06-02*