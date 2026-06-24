# How To: Trophic Incoherence Parameter Cannibalism

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test trophic incoherence parameter cannibalism

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
assert q == pytest.approx(0, abs=1e-07)
```

### Step 2: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix_a, create_using=nx.DiGraph)
```

**Verification:**
```python
assert q == pytest.approx(2, abs=1e-07)
```

### Step 3: Assign q = nx.trophic_incoherence_parameter(...)

```python
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
```

**Verification:**
```python
assert q == pytest.approx(np.std([1, 1.5, 0.5, 0.75, 1.25]), abs=1e-07)
```

### Step 4: Assign matrix_b = np.array(...)

```python
matrix_b = np.array([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]])
```

### Step 5: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix_b, create_using=nx.DiGraph)
```

### Step 6: Assign q = nx.trophic_incoherence_parameter(...)

```python
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
```

**Verification:**
```python
assert q == pytest.approx(2, abs=1e-07)
```

### Step 7: Assign matrix_c = np.array(...)

```python
matrix_c = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
```

### Step 8: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(matrix_c, create_using=nx.DiGraph)
```

### Step 9: Assign q = nx.trophic_incoherence_parameter(...)

```python
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
```

**Verification:**
```python
assert q == pytest.approx(np.std([1, 1.5, 0.5, 0.75, 1.25]), abs=1e-07)
```


## Complete Example

```python
# Workflow
matrix_a = np.array([[0, 1], [0, 0]])
G = nx.from_numpy_array(matrix_a, create_using=nx.DiGraph)
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
assert q == pytest.approx(0, abs=1e-07)
matrix_b = np.array([[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]])
G = nx.from_numpy_array(matrix_b, create_using=nx.DiGraph)
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
assert q == pytest.approx(2, abs=1e-07)
matrix_c = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]])
G = nx.from_numpy_array(matrix_c, create_using=nx.DiGraph)
q = nx.trophic_incoherence_parameter(G, cannibalism=True)
assert q == pytest.approx(np.std([1, 1.5, 0.5, 0.75, 1.25]), abs=1e-07)
```

## Next Steps


---

*Source: test_trophic.py:263 | Complexity: Advanced | Last updated: 2026-06-02*