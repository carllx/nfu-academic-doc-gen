# How To: Nlargest And Smallest Noop

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nlargest and smallest noop

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data, groups, dtype, method
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(data, name='a')
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(ser.groupby(groups), method)(n=2)
```

### Step 3: Assign expidx = value

```python
expidx = np.array(groups, dtype=int) if isinstance(groups, list) else groups
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(data, index=MultiIndex.from_arrays([expidx, ser.index]), name='a')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign data = np.array(...)

```python
data = np.array(data, dtype=dtype)
```

### Step 7: Assign data = list(...)

```python
data = list(reversed(data))
```


## Complete Example

```python
# Setup
# Fixtures: data, groups, dtype, method

# Workflow
if dtype is not None:
    data = np.array(data, dtype=dtype)
if method == 'nlargest':
    data = list(reversed(data))
ser = Series(data, name='a')
result = getattr(ser.groupby(groups), method)(n=2)
expidx = np.array(groups, dtype=int) if isinstance(groups, list) else groups
expected = Series(data, index=MultiIndex.from_arrays([expidx, ser.index]), name='a')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest_nsmallest.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*