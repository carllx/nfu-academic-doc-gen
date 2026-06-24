# How To: Laplacian Centrality E

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laplacian centrality E

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign E = nx.Graph(...)

```python
E = nx.Graph()
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```

### Step 2: Call E.add_weighted_edges_from()

```python
E.add_weighted_edges_from([(0, 1, 4), (4, 5, 1), (0, 2, 2), (2, 1, 1), (1, 3, 2), (1, 4, 2)])
```

**Verification:**
```python
assert exact[n] * full_energy == pytest.approx(dc, abs=1e-07)
```

### Step 3: Assign d = nx.laplacian_centrality(...)

```python
d = nx.laplacian_centrality(E)
```

**Verification:**
```python
assert exact_uw_nn[n] == pytest.approx(dc, abs=1e-07)
```

### Step 4: Assign exact = value

```python
exact = {0: 0.7, 1: 0.9, 2: 0.28, 3: 0.22, 4: 0.26, 5: 0.04}
```

**Verification:**
```python
assert exact_uw_nn[n] / full_energy == pytest.approx(dc, abs=1e-07)
```

### Step 5: Assign full_energy = 200

```python
full_energy = 200
```

### Step 6: Assign dnn = nx.laplacian_centrality(...)

```python
dnn = nx.laplacian_centrality(E, normalized=False)
```

### Step 7: Assign duw_nn = nx.laplacian_centrality(...)

```python
duw_nn = nx.laplacian_centrality(E, normalized=False, weight=None)
```

### Step 8: Assign exact_uw_nn = value

```python
exact_uw_nn = {0: 18, 1: 34, 2: 18, 3: 10, 4: 16, 5: 6}
```

### Step 9: Assign duw = nx.laplacian_centrality(...)

```python
duw = nx.laplacian_centrality(E, weight=None)
```

### Step 10: Assign full_energy = 42

```python
full_energy = 42
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```


## Complete Example

```python
# Workflow
E = nx.Graph()
E.add_weighted_edges_from([(0, 1, 4), (4, 5, 1), (0, 2, 2), (2, 1, 1), (1, 3, 2), (1, 4, 2)])
d = nx.laplacian_centrality(E)
exact = {0: 0.7, 1: 0.9, 2: 0.28, 3: 0.22, 4: 0.26, 5: 0.04}
for n, dc in d.items():
    assert exact[n] == pytest.approx(dc, abs=1e-07)
full_energy = 200
dnn = nx.laplacian_centrality(E, normalized=False)
for n, dc in dnn.items():
    assert exact[n] * full_energy == pytest.approx(dc, abs=1e-07)
duw_nn = nx.laplacian_centrality(E, normalized=False, weight=None)
exact_uw_nn = {0: 18, 1: 34, 2: 18, 3: 10, 4: 16, 5: 6}
for n, dc in duw_nn.items():
    assert exact_uw_nn[n] == pytest.approx(dc, abs=1e-07)
duw = nx.laplacian_centrality(E, weight=None)
full_energy = 42
for n, dc in duw.items():
    assert exact_uw_nn[n] / full_energy == pytest.approx(dc, abs=1e-07)
```

## Next Steps


---

*Source: test_laplacian_centrality.py:41 | Complexity: Advanced | Last updated: 2026-06-02*