# How To: Margulis Gabber Galil Graph Eigvals

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test margulis gabber galil graph eigvals

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: n
```

## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert w[-2] < 5 * np.sqrt(2)
```

### Step 2: Assign sp = pytest.importorskip(...)

```python
sp = pytest.importorskip('scipy')
```

### Step 3: Assign g = nx.margulis_gabber_galil_graph(...)

```python
g = nx.margulis_gabber_galil_graph(n)
```

### Step 4: Assign w = sorted(...)

```python
w = sorted(sp.linalg.eigvalsh(nx.adjacency_matrix(g).toarray()))
```

**Verification:**
```python
assert w[-2] < 5 * np.sqrt(2)
```


## Complete Example

```python
# Setup
# Fixtures: n

# Workflow
np = pytest.importorskip('numpy')
sp = pytest.importorskip('scipy')
g = nx.margulis_gabber_galil_graph(n)
w = sorted(sp.linalg.eigvalsh(nx.adjacency_matrix(g).toarray()))
assert w[-2] < 5 * np.sqrt(2)
```

## Next Steps


---

*Source: test_expanders.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*