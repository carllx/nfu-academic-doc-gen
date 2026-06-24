# How To: Pagerank

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pagerank

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.link_analysis.pagerank_alg`
- `networkx.classes.tests`

**Setup Required:**
```python
# Fixtures: alg
```

## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

### Step 2: Assign p = alg(...)

```python
p = alg(G, alpha=0.9, tol=1e-08)
```

**Verification:**
```python
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

### Step 3: Assign nstart = value

```python
nstart = {n: random.random() for n in G}
```

### Step 4: Assign p = alg(...)

```python
p = alg(G, alpha=0.9, tol=1e-08, nstart=nstart)
```

**Verification:**
```python
assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```


## Complete Example

```python
# Setup
# Fixtures: alg

# Workflow
G = self.G
p = alg(G, alpha=0.9, tol=1e-08)
for n in G:
    assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
nstart = {n: random.random() for n in G}
p = alg(G, alpha=0.9, tol=1e-08, nstart=nstart)
for n in G:
    assert p[n] == pytest.approx(G.pagerank[n], abs=0.0001)
```

## Next Steps


---

*Source: test_pagerank.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*