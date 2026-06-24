# How To: Factorize Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize nan

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

### Step 1: Assign key = np.array(...)

```python
key = np.array([1, 2, 1, np.nan], dtype='O')
```

**Verification:**
```python
assert len(set(key)) == len(set(expected))
```

### Step 2: Assign rizer = ht.ObjectFactorizer(...)

```python
rizer = ht.ObjectFactorizer(len(key))
```

### Step 3: Assign ids = rizer.factorize(...)

```python
ids = rizer.factorize(key, na_sentinel=na_sentinel)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0, 1, 0, na_sentinel], dtype=np.intp)
```

**Verification:**
```python
assert len(set(key)) == len(set(expected))
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(pd.isna(key), expected == na_sentinel)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ids, expected)
```


## Complete Example

```python
# Workflow
key = np.array([1, 2, 1, np.nan], dtype='O')
rizer = ht.ObjectFactorizer(len(key))
for na_sentinel in (-1, 20):
    ids = rizer.factorize(key, na_sentinel=na_sentinel)
    expected = np.array([0, 1, 0, na_sentinel], dtype=np.intp)
    assert len(set(key)) == len(set(expected))
    tm.assert_numpy_array_equal(pd.isna(key), expected == na_sentinel)
    tm.assert_numpy_array_equal(ids, expected)
```

## Next Steps


---

*Source: test_algos.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*