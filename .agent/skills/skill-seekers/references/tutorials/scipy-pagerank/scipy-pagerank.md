# How To: Scipy Pagerank

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scipy pagerank

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
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

### Step 2: Assign p = _pagerank_scipy(...)

```python
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08)
```

**Verification:**
```python
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

### Step 3: Assign personalize = value

```python
personalize = {n: random.random() for n in G}
```

### Step 4: Assign p = _pagerank_scipy(...)

```python
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08, personalization=personalize)
```

### Step 5: Assign nstart = value

```python
nstart = {n: random.random() for n in G}
```

### Step 6: Assign p = _pagerank_scipy(...)

```python
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08, nstart=nstart)
```

**Verification:**
```python
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```


## Complete Example

```python
# Workflow
G = self.G
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08)
for n in G:
    assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
personalize = {n: random.random() for n in G}
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08, personalization=personalize)
nstart = {n: random.random() for n in G}
p = _pagerank_scipy(G, alpha=0.9, tol=1e-08, nstart=nstart)
for n in G:
    assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

## Next Steps


---

*Source: test_pagerank.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*