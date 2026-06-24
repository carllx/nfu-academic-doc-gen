# How To: Minmax Extensionarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test minmax extensionarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: method, numeric_only
```

## Step-by-Step Guide

### Step 1: Assign int64_info = np.iinfo(...)

```python
int64_info = np.iinfo('int64')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([int64_info.max, None, int64_info.min], dtype=pd.Int64Dtype())
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'Int64': ser})
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(df, method)(numeric_only=numeric_only)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([getattr(int64_info, method)], dtype='Int64', index=Index(['Int64']))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, numeric_only

# Workflow
int64_info = np.iinfo('int64')
ser = Series([int64_info.max, None, int64_info.min], dtype=pd.Int64Dtype())
df = DataFrame({'Int64': ser})
result = getattr(df, method)(numeric_only=numeric_only)
expected = Series([getattr(int64_info, method)], dtype='Int64', index=Index(['Int64']))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:1951 | Complexity: Intermediate | Last updated: 2026-06-02*