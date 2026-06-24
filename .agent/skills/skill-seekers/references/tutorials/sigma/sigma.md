# How To: Sigma

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sigma

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign Gs = nx.connected_watts_strogatz_graph(...)

```python
Gs = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
```

**Verification:**
```python
assert sigmar < sigmas
```

### Step 2: Assign Gr = nx.connected_watts_strogatz_graph(...)

```python
Gr = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
```

### Step 3: Assign sigmas = sigma(...)

```python
sigmas = sigma(Gs, niter=1, nrand=2, seed=rng)
```

### Step 4: Assign sigmar = sigma(...)

```python
sigmar = sigma(Gr, niter=1, nrand=2, seed=rng)
```

**Verification:**
```python
assert sigmar < sigmas
```


## Complete Example

```python
# Workflow
Gs = nx.connected_watts_strogatz_graph(50, 6, 0.1, seed=rng)
Gr = nx.connected_watts_strogatz_graph(50, 6, 1, seed=rng)
sigmas = sigma(Gs, niter=1, nrand=2, seed=rng)
sigmar = sigma(Gr, niter=1, nrand=2, seed=rng)
assert sigmar < sigmas
```

## Next Steps


---

*Source: test_smallworld.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*