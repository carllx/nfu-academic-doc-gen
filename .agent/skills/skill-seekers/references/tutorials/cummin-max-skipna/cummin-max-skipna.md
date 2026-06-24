# How To: Cummin Max Skipna

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cummin max skipna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, dtype, groups, expected_data
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([1, None, 2], dtype=dtype)})
```

### Step 2: Assign orig = df.copy(...)

```python
orig = df.copy()
```

### Step 3: Assign gb = value

```python
gb = df.groupby(groups)['a']
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(gb, method)(skipna=False)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(expected_data, dtype=dtype, name='a')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, orig)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, dtype, groups, expected_data

# Workflow
df = DataFrame({'a': Series([1, None, 2], dtype=dtype)})
orig = df.copy()
gb = df.groupby(groups)['a']
result = getattr(gb, method)(skipna=False)
expected = Series(expected_data, dtype=dtype, name='a')
tm.assert_frame_equal(df, orig)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*