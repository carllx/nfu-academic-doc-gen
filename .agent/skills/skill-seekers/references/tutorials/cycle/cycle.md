# How To: Cycle

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cycle

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: normalized, expected_order, method
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert order in expected_order
```

### Step 2: Assign path = list(...)

```python
path = list(range(10))
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 4: Call nx.add_path()

```python
nx.add_path(G, path, weight=5)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(path[-1], path[0], weight=1)
```

### Step 6: Assign A = nx.laplacian_matrix.todense(...)

```python
A = nx.laplacian_matrix(G).todense()
```

### Step 7: Assign order = nx.spectral_ordering(...)

```python
order = nx.spectral_ordering(G, normalized=normalized, method=method)
```

**Verification:**
```python
assert order in expected_order
```


## Complete Example

```python
# Setup
# Fixtures: normalized, expected_order, method

# Workflow
pytest.importorskip('scipy')
path = list(range(10))
G = nx.Graph()
nx.add_path(G, path, weight=5)
G.add_edge(path[-1], path[0], weight=1)
A = nx.laplacian_matrix(G).todense()
order = nx.spectral_ordering(G, normalized=normalized, method=method)
assert order in expected_order
```

## Next Steps


---

*Source: test_algebraic_connectivity.py:392 | Complexity: Intermediate | Last updated: 2026-06-02*