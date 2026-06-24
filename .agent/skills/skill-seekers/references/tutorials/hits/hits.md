# How To: Hits

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test hits

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.link_analysis.hits_alg`

**Setup Required:**
```python
# Fixtures: hits_alg
```

## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert h[n] == pytest.approx(G.h[n], abs=0.0001)
```

### Step 2: Assign unknown = hits_alg(...)

```python
h, a = hits_alg(G, tol=1e-08)
```

**Verification:**
```python
assert a[n] == pytest.approx(G.a[n], abs=0.0001)
```

### Step 3: Assign nstart = value

```python
nstart = {i: 1.0 / 2 for i in G}
```

**Verification:**
```python
assert h[n] == pytest.approx(G.h[n], abs=0.0001)
```

### Step 4: Assign unknown = hits_alg(...)

```python
h, a = hits_alg(G, nstart=nstart)
```

**Verification:**
```python
assert a[n] == pytest.approx(G.a[n], abs=0.0001)
```


## Complete Example

```python
# Setup
# Fixtures: hits_alg

# Workflow
G = self.G
h, a = hits_alg(G, tol=1e-08)
for n in G:
    assert h[n] == pytest.approx(G.h[n], abs=0.0001)
for n in G:
    assert a[n] == pytest.approx(G.a[n], abs=0.0001)
nstart = {i: 1.0 / 2 for i in G}
h, a = hits_alg(G, nstart=nstart)
for n in G:
    assert h[n] == pytest.approx(G.h[n], abs=0.0001)
for n in G:
    assert a[n] == pytest.approx(G.a[n], abs=0.0001)
```

## Next Steps


---

*Source: test_hits.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*