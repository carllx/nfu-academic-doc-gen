# How To: Google Matrix

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test google matrix

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.link_analysis.pagerank_alg`
- `networkx.classes.tests`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert a == pytest.approx(b, abs=1e-07)
```

### Step 2: Assign M = nx.google_matrix(...)

```python
M = nx.google_matrix(G, alpha=0.9, nodelist=sorted(G))
```

### Step 3: Assign unknown = np.linalg.eig(...)

```python
_, ev = np.linalg.eig(M.T)
```

### Step 4: Assign p = value

```python
p = ev[:, 0] / ev[:, 0].sum()
```

**Verification:**
```python
assert a == pytest.approx(b, abs=1e-07)
```


## Complete Example

```python
# Workflow
G = self.G
M = nx.google_matrix(G, alpha=0.9, nodelist=sorted(G))
_, ev = np.linalg.eig(M.T)
p = ev[:, 0] / ev[:, 0].sum()
for a, b in zip(p, self.G.pagerank.values()):
    assert a == pytest.approx(b, abs=1e-07)
```

## Next Steps


---

*Source: test_pagerank.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*