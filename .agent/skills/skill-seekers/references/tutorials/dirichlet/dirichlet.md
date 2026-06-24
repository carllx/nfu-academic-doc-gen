# How To: Dirichlet

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dirichlet

## Prerequisites

**Required Modules:**
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `hashlib`
- `threading`


## Step-by-Step Guide

### Step 1: Assign rng = random.RandomState(...)

```python
rng = random.RandomState(self.seed)
```

**Verification:**
```python
assert_array_almost_equal(actual, desired, decimal=15)
```

### Step 2: Assign alpha = np.array(...)

```python
alpha = np.array([51.72840233779265, 39.74494232180944])
```

### Step 3: Assign actual = rng.dirichlet(...)

```python
actual = rng.dirichlet(alpha, size=(3, 2))
```

### Step 4: Assign desired = np.array(...)

```python
desired = np.array([[[0.5453944457361156, 0.4546055542638844], [0.6234581682203941, 0.376541831779606]], [[0.5520600008578578, 0.44793999914214233], [0.589640233051543, 0.4103597669484569]], [[0.5926690928064783, 0.4073309071935218], [0.5697443174397521, 0.430255682560248]]])
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(actual, desired, decimal=15)
```


## Complete Example

```python
# Workflow
rng = random.RandomState(self.seed)
alpha = np.array([51.72840233779265, 39.74494232180944])
actual = rng.dirichlet(alpha, size=(3, 2))
desired = np.array([[[0.5453944457361156, 0.4546055542638844], [0.6234581682203941, 0.376541831779606]], [[0.5520600008578578, 0.44793999914214233], [0.589640233051543, 0.4103597669484569]], [[0.5926690928064783, 0.4073309071935218], [0.5697443174397521, 0.430255682560248]]])
assert_array_almost_equal(actual, desired, decimal=15)
```

## Next Steps


---

*Source: test_random.py:611 | Complexity: Intermediate | Last updated: 2026-06-02*