# How To: Lattice Reference

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lattice reference

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.connected_watts_strogatz_graph(...)

```python
G = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
```

**Verification:**
```python
assert Ll > L
```

### Step 2: Assign Gl = lattice_reference(...)

```python
Gl = lattice_reference(G, niter=1, seed=rng)
```

### Step 3: Assign L = nx.average_shortest_path_length(...)

```python
L = nx.average_shortest_path_length(G)
```

### Step 4: Assign Ll = nx.average_shortest_path_length(...)

```python
Ll = nx.average_shortest_path_length(Gl)
```

**Verification:**
```python
assert Ll > L
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, lattice_reference, nx.Graph())
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, lattice_reference, nx.DiGraph())
```

### Step 7: Assign H = nx.Graph(...)

```python
H = nx.Graph(((0, 1), (2, 3)))
```

### Step 8: Assign Hl = lattice_reference(...)

```python
Hl = lattice_reference(H, niter=1)
```


## Complete Example

```python
# Workflow
G = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
Gl = lattice_reference(G, niter=1, seed=rng)
L = nx.average_shortest_path_length(G)
Ll = nx.average_shortest_path_length(Gl)
assert Ll > L
pytest.raises(nx.NetworkXError, lattice_reference, nx.Graph())
pytest.raises(nx.NetworkXNotImplemented, lattice_reference, nx.DiGraph())
H = nx.Graph(((0, 1), (2, 3)))
Hl = lattice_reference(H, niter=1)
```

## Next Steps


---

*Source: test_smallworld.py:27 | Complexity: Advanced | Last updated: 2026-06-02*