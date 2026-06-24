# How To: Eigenvectors

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eigenvectors

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

### Step 2: Assign eigenval = value

```python
eigenval = np.linalg.eigvals
```

### Step 3: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 4: Assign cs = 'ddiiddid'

```python
cs = 'ddiiddid'
```

### Step 5: Assign G = nxt.threshold_graph(...)

```python
G = nxt.threshold_graph(cs)
```

### Step 6: Assign unknown = nxt.eigenvectors(...)

```python
tgeval, tgevec = nxt.eigenvectors(cs)
```

### Step 7: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose([np.dot(lv, lv) for lv in tgevec], 1.0, rtol=1e-09)
```

### Step 8: Assign lapl = nx.laplacian_matrix(...)

```python
lapl = nx.laplacian_matrix(G)
```


## Complete Example

```python
# Workflow
np = pytest.importorskip('numpy')
eigenval = np.linalg.eigvals
pytest.importorskip('scipy')
cs = 'ddiiddid'
G = nxt.threshold_graph(cs)
tgeval, tgevec = nxt.eigenvectors(cs)
np.testing.assert_allclose([np.dot(lv, lv) for lv in tgevec], 1.0, rtol=1e-09)
lapl = nx.laplacian_matrix(G)
```

## Next Steps


---

*Source: test_threshold.py:249 | Complexity: Advanced | Last updated: 2026-06-02*