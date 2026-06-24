# How To: Greedy Plus Plus Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test greedy plus plus complete graph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert d == pytest.approx(6 / 4)
```

### Step 2: Assign unknown = approx.densest_subgraph(...)

```python
d, S = approx.densest_subgraph(G, iterations=1, method=method)
```

**Verification:**
```python
assert S == {0, 1, 2, 3}
```

### Step 3: Call pytest.importorskip()

```python
pytest.importorskip('numpy')
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
if method == 'fista':
    pytest.importorskip('numpy')
G = nx.complete_graph(4)
d, S = approx.densest_subgraph(G, iterations=1, method=method)
assert d == pytest.approx(6 / 4)
assert S == {0, 1, 2, 3}
```

## Next Steps


---

*Source: test_density.py:38 | Complexity: Beginner | Last updated: 2026-06-02*