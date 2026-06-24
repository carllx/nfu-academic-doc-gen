# How To: Cython Group Sum Inf At Begining And End

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython group sum Inf at begining and end

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.groupby`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values, out
```

## Step-by-Step Guide

### Step 1: Assign actual = np.array(...)

```python
actual = np.array([[np.nan], [np.nan]], dtype='float64')
```

### Step 2: Assign counts = np.array(...)

```python
counts = np.array([0, 0], dtype='int64')
```

### Step 3: Assign data = np.array(...)

```python
data = np.array(values, dtype='float64')
```

### Step 4: Assign labels = np.array(...)

```python
labels = np.array([0, 1, 1], dtype=np.intp)
```

### Step 5: Call group_sum()

```python
group_sum(actual, counts, data, labels, None, is_datetimelike=False)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array(out, dtype='float64')
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: values, out

# Workflow
actual = np.array([[np.nan], [np.nan]], dtype='float64')
counts = np.array([0, 0], dtype='int64')
data = np.array(values, dtype='float64')
labels = np.array([0, 1, 1], dtype=np.intp)
group_sum(actual, counts, data, labels, None, is_datetimelike=False)
expected = np.array(out, dtype='float64')
tm.assert_numpy_array_equal(actual, expected)
```

## Next Steps


---

*Source: test_libgroupby.py:317 | Complexity: Intermediate | Last updated: 2026-06-02*