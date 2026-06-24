# How To: From Records Iterator

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records iterator

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([(1.0, 1.0, 2, 2), (3.0, 3.0, 4, 4), (5.0, 5.0, 6, 6), (7.0, 7.0, 8, 8)], dtype=[('x', np.float64), ('u', np.float32), ('y', np.int64), ('z', np.int32)])
```

### Step 2: Assign df = DataFrame.from_records(...)

```python
df = DataFrame.from_records(iter(arr), nrows=2)
```

### Step 3: Assign xp = DataFrame(...)

```python
xp = DataFrame({'x': np.array([1.0, 3.0], dtype=np.float64), 'u': np.array([1.0, 3.0], dtype=np.float32), 'y': np.array([2, 4], dtype=np.int64), 'z': np.array([2, 4], dtype=np.int32)})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.reindex_like(xp), xp)
```

### Step 5: Assign arr = value

```python
arr = [(1.0, 2), (3.0, 4), (5.0, 6), (7.0, 8)]
```

### Step 6: Assign df = DataFrame.from_records(...)

```python
df = DataFrame.from_records(iter(arr), columns=['x', 'y'], nrows=2)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, xp.reindex(columns=['x', 'y']), check_dtype=False)
```


## Complete Example

```python
# Workflow
arr = np.array([(1.0, 1.0, 2, 2), (3.0, 3.0, 4, 4), (5.0, 5.0, 6, 6), (7.0, 7.0, 8, 8)], dtype=[('x', np.float64), ('u', np.float32), ('y', np.int64), ('z', np.int32)])
df = DataFrame.from_records(iter(arr), nrows=2)
xp = DataFrame({'x': np.array([1.0, 3.0], dtype=np.float64), 'u': np.array([1.0, 3.0], dtype=np.float32), 'y': np.array([2, 4], dtype=np.int64), 'z': np.array([2, 4], dtype=np.int32)})
tm.assert_frame_equal(df.reindex_like(xp), xp)
arr = [(1.0, 2), (3.0, 4), (5.0, 6), (7.0, 8)]
df = DataFrame.from_records(iter(arr), columns=['x', 'y'], nrows=2)
tm.assert_frame_equal(df, xp.reindex(columns=['x', 'y']), check_dtype=False)
```

## Next Steps


---

*Source: test_from_records.py:325 | Complexity: Intermediate | Last updated: 2026-06-02*