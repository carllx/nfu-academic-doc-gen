# How To: Laplacian Centrality Dg

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laplacian centrality DG

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign DG = nx.DiGraph(...)

```python
DG = nx.DiGraph([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (5, 8)])
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```

### Step 2: Assign d = nx.laplacian_centrality(...)

```python
d = nx.laplacian_centrality(DG)
```

**Verification:**
```python
assert exact[n] * full_energy == pytest.approx(dc, abs=0.0001)
```

### Step 3: Assign exact = value

```python
exact = {0: 0.2123352, 5: 0.515391, 1: 0.2123352, 2: 0.2123352, 3: 0.2123352, 4: 0.2123352, 6: 0.2952031, 7: 0.2952031, 8: 0.2952031}
```

### Step 4: Assign full_energy = 9.50704

```python
full_energy = 9.50704
```

### Step 5: Assign dnn = nx.laplacian_centrality(...)

```python
dnn = nx.laplacian_centrality(DG, normalized=False)
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```


## Complete Example

```python
# Workflow
DG = nx.DiGraph([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (5, 8)])
d = nx.laplacian_centrality(DG)
exact = {0: 0.2123352, 5: 0.515391, 1: 0.2123352, 2: 0.2123352, 3: 0.2123352, 4: 0.2123352, 6: 0.2952031, 7: 0.2952031, 8: 0.2952031}
for n, dc in d.items():
    assert exact[n] == pytest.approx(dc, abs=1e-07)
full_energy = 9.50704
dnn = nx.laplacian_centrality(DG, normalized=False)
for n, dc in dnn.items():
    assert exact[n] * full_energy == pytest.approx(dc, abs=0.0001)
```

## Next Steps


---

*Source: test_laplacian_centrality.py:199 | Complexity: Intermediate | Last updated: 2026-06-02*