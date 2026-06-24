# How To: Factorize Complex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize complex

## Prerequisites

**Required Modules:**
- `datetime`
- `struct`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign array = value

```python
array = [1, 2, 2 + 1j]
```

### Step 2: Assign msg = 'factorize with argument that is not not a Series'

```python
msg = 'factorize with argument that is not not a Series'
```

### Step 3: Assign expected_labels = np.array(...)

```python
expected_labels = np.array([0, 1, 2], dtype=np.intp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(labels, expected_labels)
```

### Step 5: Assign expected_uniques = np.array(...)

```python
expected_uniques = np.array([1 + 0j, 2 + 0j, 2 + 1j], dtype=object)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(uniques, expected_uniques)
```

### Step 7: Assign unknown = algos.factorize(...)

```python
labels, uniques = algos.factorize(array)
```


## Complete Example

```python
# Workflow
array = [1, 2, 2 + 1j]
msg = 'factorize with argument that is not not a Series'
with tm.assert_produces_warning(FutureWarning, match=msg):
    labels, uniques = algos.factorize(array)
expected_labels = np.array([0, 1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(labels, expected_labels)
expected_uniques = np.array([1 + 0j, 2 + 0j, 2 + 1j], dtype=object)
tm.assert_numpy_array_equal(uniques, expected_uniques)
```

## Next Steps


---

*Source: test_algos.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*