# How To: Trophic Levels More Complex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trophic levels more complex

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign matrix = np.array(...)

```python
matrix = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
```

**Verification:**
```python
assert d[ind] == pytest.approx(expected_result[ind], abs=1e-07)
```

### Step 2: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
```

**Verification:**
```python
assert d[ind] == pytest.approx(expected_result[ind], abs=1e-07)
```

### Step 3: Assign d = nx.trophic_levels(...)

```python
d = nx.trophic_levels(G)
```

### Step 4: Assign expected_result = value

```python
expected_result = [1, 2, 3, 4]
```

### Step 5: Assign matrix = np.array(...)

```python
matrix = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
```

### Step 6: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
```

### Step 7: Assign d = nx.trophic_levels(...)

```python
d = nx.trophic_levels(G)
```

### Step 8: Assign expected_result = value

```python
expected_result = [1, 2, 2.5, 3.25]
```

**Verification:**
```python
assert d[ind] == pytest.approx(expected_result[ind], abs=1e-07)
```


## Complete Example

```python
# Workflow
matrix = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
d = nx.trophic_levels(G)
expected_result = [1, 2, 3, 4]
for ind in range(4):
    assert d[ind] == pytest.approx(expected_result[ind], abs=1e-07)
matrix = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
d = nx.trophic_levels(G)
expected_result = [1, 2, 2.5, 3.25]
for ind in range(4):
    assert d[ind] == pytest.approx(expected_result[ind], abs=1e-07)
```

## Next Steps


---

*Source: test_trophic.py:87 | Complexity: Advanced | Last updated: 2026-06-02*