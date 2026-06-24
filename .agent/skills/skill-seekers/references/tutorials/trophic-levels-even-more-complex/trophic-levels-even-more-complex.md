# How To: Trophic Levels Even More Complex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trophic levels even more complex

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign matrix = np.array(...)

```python
matrix = np.array([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]])
```

**Verification:**
```python
assert result_1[ind] == pytest.approx(result_2[ind], abs=1e-07)
```

### Step 2: Assign K = np.array(...)

```python
K = np.array([[1, 0, -1, 0, 0], [0, 0.5, 0, -0.5, 0], [0, 0, 1, 0, 0], [0, -0.5, 0, 1, -0.5], [0, 0, 0, 0, 1]])
```

### Step 3: Assign result_1 = np.ravel(...)

```python
result_1 = np.ravel(np.linalg.inv(K) @ np.ones(5))
```

### Step 4: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
```

### Step 5: Assign result_2 = nx.trophic_levels(...)

```python
result_2 = nx.trophic_levels(G)
```

**Verification:**
```python
assert result_1[ind] == pytest.approx(result_2[ind], abs=1e-07)
```


## Complete Example

```python
# Workflow
matrix = np.array([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]])
K = np.array([[1, 0, -1, 0, 0], [0, 0.5, 0, -0.5, 0], [0, 0, 1, 0, 0], [0, -0.5, 0, 1, -0.5], [0, 0, 0, 0, 1]])
result_1 = np.ravel(np.linalg.inv(K) @ np.ones(5))
G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
result_2 = nx.trophic_levels(G)
for ind in range(5):
    assert result_1[ind] == pytest.approx(result_2[ind], abs=1e-07)
```

## Next Steps


---

*Source: test_trophic.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*