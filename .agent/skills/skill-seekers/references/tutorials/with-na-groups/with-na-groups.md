# How To: With Na Groups

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test with na groups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(np.arange(10))
```

### Step 2: Assign values = Series(...)

```python
values = Series(np.ones(10), index, dtype=dtype)
```

### Step 3: Assign labels = Series(...)

```python
labels = Series([np.nan, 'foo', 'bar', 'bar', np.nan, np.nan, 'bar', 'bar', np.nan, 'foo'], index=index)
```

### Step 4: Assign grouped = values.groupby(...)

```python
grouped = values.groupby(labels)
```

### Step 5: Assign agged = grouped.agg(...)

```python
agged = grouped.agg(len)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([4, 2], index=['bar', 'foo'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(agged, expected, check_dtype=False)
```

### Step 8: Assign agged = grouped.agg(...)

```python
agged = grouped.agg(f)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([4.0, 2.0], index=['bar', 'foo'])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(agged, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
index = Index(np.arange(10))
values = Series(np.ones(10), index, dtype=dtype)
labels = Series([np.nan, 'foo', 'bar', 'bar', np.nan, np.nan, 'bar', 'bar', np.nan, 'foo'], index=index)
grouped = values.groupby(labels)
agged = grouped.agg(len)
expected = Series([4, 2], index=['bar', 'foo'])
tm.assert_series_equal(agged, expected, check_dtype=False)

def f(x):
    return float(len(x))
agged = grouped.agg(f)
expected = Series([4.0, 2.0], index=['bar', 'foo'])
tm.assert_series_equal(agged, expected)
```

## Next Steps


---

*Source: test_groupby.py:355 | Complexity: Advanced | Last updated: 2026-06-02*