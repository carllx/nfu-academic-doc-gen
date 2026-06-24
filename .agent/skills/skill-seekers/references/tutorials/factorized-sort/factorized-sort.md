# How To: Factorized Sort

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorized sort

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = pd.Categorical(...)

```python
cat = pd.Categorical(['b', 'b', None, 'a'])
```

### Step 2: Assign unknown = pd.factorize(...)

```python
codes, uniques = pd.factorize(cat, sort=True)
```

### Step 3: Assign expected_codes = np.array(...)

```python
expected_codes = np.array([1, 1, -1, 0], dtype=np.intp)
```

### Step 4: Assign expected_uniques = pd.Categorical(...)

```python
expected_uniques = pd.Categorical(['a', 'b'])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(codes, expected_codes)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(uniques, expected_uniques)
```


## Complete Example

```python
# Workflow
cat = pd.Categorical(['b', 'b', None, 'a'])
codes, uniques = pd.factorize(cat, sort=True)
expected_codes = np.array([1, 1, -1, 0], dtype=np.intp)
expected_uniques = pd.Categorical(['a', 'b'])
tm.assert_numpy_array_equal(codes, expected_codes)
tm.assert_categorical_equal(uniques, expected_uniques)
```

## Next Steps


---

*Source: test_algos.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*