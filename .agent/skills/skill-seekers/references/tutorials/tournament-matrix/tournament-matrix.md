# How To: Tournament Matrix

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tournament matrix

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.tournament`


## Step-by-Step Guide

### Step 1: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

### Step 2: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 3: Assign npt = value

```python
npt = np.testing
```

### Step 4: Assign G = DiGraph(...)

```python
G = DiGraph([(0, 1)])
```

### Step 5: Assign m = tournament_matrix(...)

```python
m = tournament_matrix(G)
```

### Step 6: Call npt.assert_array_equal()

```python
npt.assert_array_equal(m.todense(), np.array([[0, 1], [-1, 0]]))
```


## Complete Example

```python
# Workflow
np = pytest.importorskip('numpy')
pytest.importorskip('scipy')
npt = np.testing
G = DiGraph([(0, 1)])
m = tournament_matrix(G)
npt.assert_array_equal(m.todense(), np.array([[0, 1], [-1, 0]]))
```

## Next Steps


---

*Source: test_tournament.py:124 | Complexity: Intermediate | Last updated: 2026-06-02*