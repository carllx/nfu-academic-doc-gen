# How To: Trophic Differences

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trophic differences

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign matrix_a = np.array(...)

```python
matrix_a = np.array([[0, 1], [0, 0]])
```

**Verification:**
```python
assert diffs[0, 1] == pytest.approx(1, abs=1e-07)
```

### Step 2: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix_a, create_using=nx.DiGraph)
```

**Verification:**
```python
assert diffs[0, 1] == pytest.approx(1, abs=1e-07)
```

### Step 3: Assign diffs = nx.trophic_differences(...)

```python
diffs = nx.trophic_differences(G)
```

**Verification:**
```python
assert diffs[0, 2] == pytest.approx(1.5, abs=1e-07)
```

### Step 4: Assign matrix_b = np.array(...)

```python
matrix_b = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
```

**Verification:**
```python
assert diffs[1, 2] == pytest.approx(0.5, abs=1e-07)
```

### Step 5: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix_b, create_using=nx.DiGraph)
```

**Verification:**
```python
assert diffs[1, 3] == pytest.approx(1.25, abs=1e-07)
```

### Step 6: Assign diffs = nx.trophic_differences(...)

```python
diffs = nx.trophic_differences(G)
```

**Verification:**
```python
assert diffs[2, 3] == pytest.approx(0.75, abs=1e-07)
```


## Complete Example

```python
# Workflow
matrix_a = np.array([[0, 1], [0, 0]])
G = nx.from_numpy_array(matrix_a, create_using=nx.DiGraph)
diffs = nx.trophic_differences(G)
assert diffs[0, 1] == pytest.approx(1, abs=1e-07)
matrix_b = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
G = nx.from_numpy_array(matrix_b, create_using=nx.DiGraph)
diffs = nx.trophic_differences(G)
assert diffs[0, 1] == pytest.approx(1, abs=1e-07)
assert diffs[0, 2] == pytest.approx(1.5, abs=1e-07)
assert diffs[1, 2] == pytest.approx(0.5, abs=1e-07)
assert diffs[1, 3] == pytest.approx(1.25, abs=1e-07)
assert diffs[2, 3] == pytest.approx(0.75, abs=1e-07)
```

## Next Steps


---

*Source: test_trophic.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*