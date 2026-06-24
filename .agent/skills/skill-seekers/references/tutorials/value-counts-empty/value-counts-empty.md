# How To: Value Counts Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts empty

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([], dtype='Float64')
```

**Verification:**
```python
assert idx.dtype == 'Float64'
```

### Step 2: Assign result = ser.value_counts(...)

```python
result = ser.value_counts()
```

### Step 3: Assign idx = pd.Index(...)

```python
idx = pd.Index([], dtype='Float64')
```

**Verification:**
```python
assert idx.dtype == 'Float64'
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([], index=idx, dtype='Int64', name='count')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = pd.Series([], dtype='Float64')
result = ser.value_counts()
idx = pd.Index([], dtype='Float64')
assert idx.dtype == 'Float64'
expected = pd.Series([], index=idx, dtype='Int64', name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*