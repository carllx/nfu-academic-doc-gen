# How To: Random Reference

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random reference

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.connected_watts_strogatz_graph(...)

```python
G = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
```

**Verification:**
```python
assert C > Cr
```

### Step 2: Assign Gr = random_reference(...)

```python
Gr = random_reference(G, niter=1, seed=rng)
```

### Step 3: Assign C = nx.average_clustering(...)

```python
C = nx.average_clustering(G)
```

### Step 4: Assign Cr = nx.average_clustering(...)

```python
Cr = nx.average_clustering(Gr)
```

**Verification:**
```python
assert C > Cr
```

### Step 5: Assign H = nx.Graph(...)

```python
H = nx.Graph(((0, 1), (2, 3)))
```

### Step 6: Assign Hl = random_reference(...)

```python
Hl = random_reference(H, niter=1, seed=rng)
```

### Step 7: Call next()

```python
next(random_reference(nx.Graph()))
```

### Step 8: Call next()

```python
next(random_reference(nx.DiGraph()))
```


## Complete Example

```python
# Workflow
G = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
Gr = random_reference(G, niter=1, seed=rng)
C = nx.average_clustering(G)
Cr = nx.average_clustering(Gr)
assert C > Cr
with pytest.raises(nx.NetworkXError):
    next(random_reference(nx.Graph()))
with pytest.raises(nx.NetworkXNotImplemented):
    next(random_reference(nx.DiGraph()))
H = nx.Graph(((0, 1), (2, 3)))
Hl = random_reference(H, niter=1, seed=rng)
```

## Next Steps


---

*Source: test_smallworld.py:11 | Complexity: Advanced | Last updated: 2026-06-02*