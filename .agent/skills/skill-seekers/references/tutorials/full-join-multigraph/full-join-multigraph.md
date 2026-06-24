# How To: Full Join Multigraph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full join multigraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert set(U) == set(G) | set(H)
```

### Step 2: Call G.add_node()

```python
G.add_node(0)
```

**Verification:**
```python
assert len(U) == len(G) + len(H)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H)
```

### Step 4: Assign H = nx.MultiGraph(...)

```python
H = nx.MultiGraph()
```

**Verification:**
```python
assert set(U) == {'g0', 'g1', 'g2', 'h3', 'h4'}
```

### Step 5: Call H.add_edge()

```python
H.add_edge(3, 4)
```

**Verification:**
```python
assert len(U) == len(G) + len(H)
```

### Step 6: Assign U = nx.full_join(...)

```python
U = nx.full_join(G, H)
```

**Verification:**
```python
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H)
```

### Step 7: Assign U = nx.full_join(...)

```python
U = nx.full_join(G, H, rename=('g', 'h'))
```

**Verification:**
```python
assert set(U) == set(G) | set(H)
```

### Step 8: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph()
```

**Verification:**
```python
assert len(U) == len(G) + len(H)
```

### Step 9: Call G.add_node()

```python
G.add_node(0)
```

**Verification:**
```python
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H) * 2
```

### Step 10: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert set(U) == {'g0', 'g1', 'g2', 'h3', 'h4'}
```

### Step 11: Assign H = nx.MultiDiGraph(...)

```python
H = nx.MultiDiGraph()
```

**Verification:**
```python
assert len(U) == len(G) + len(H)
```

### Step 12: Call H.add_edge()

```python
H.add_edge(3, 4)
```

**Verification:**
```python
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H) * 2
```

### Step 13: Assign U = nx.full_join(...)

```python
U = nx.full_join(G, H)
```

**Verification:**
```python
assert set(U) == set(G) | set(H)
```

### Step 14: Assign U = nx.full_join(...)

```python
U = nx.full_join(G, H, rename=('g', 'h'))
```

**Verification:**
```python
assert set(U) == {'g0', 'g1', 'g2', 'h3', 'h4'}
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.add_node(0)
G.add_edge(1, 2)
H = nx.MultiGraph()
H.add_edge(3, 4)
U = nx.full_join(G, H)
assert set(U) == set(G) | set(H)
assert len(U) == len(G) + len(H)
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H)
U = nx.full_join(G, H, rename=('g', 'h'))
assert set(U) == {'g0', 'g1', 'g2', 'h3', 'h4'}
assert len(U) == len(G) + len(H)
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H)
G = nx.MultiDiGraph()
G.add_node(0)
G.add_edge(1, 2)
H = nx.MultiDiGraph()
H.add_edge(3, 4)
U = nx.full_join(G, H)
assert set(U) == set(G) | set(H)
assert len(U) == len(G) + len(H)
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H) * 2
U = nx.full_join(G, H, rename=('g', 'h'))
assert set(U) == {'g0', 'g1', 'g2', 'h3', 'h4'}
assert len(U) == len(G) + len(H)
assert len(U.edges()) == len(G.edges()) + len(H.edges()) + len(G) * len(H) * 2
```

## Next Steps


---

*Source: test_binary.py:405 | Complexity: Advanced | Last updated: 2026-06-02*