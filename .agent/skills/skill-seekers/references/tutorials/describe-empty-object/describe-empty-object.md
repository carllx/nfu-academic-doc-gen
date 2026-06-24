# How To: Describe Empty Object

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe empty object

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([None, None], dtype=object)
```

**Verification:**
```python
assert np.isnan(result.iloc[2])
```

### Step 2: Assign result = s.describe(...)

```python
result = s.describe()
```

**Verification:**
```python
assert np.isnan(result.iloc[3])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([0, 0, np.nan, np.nan], dtype=object, index=['count', 'unique', 'top', 'freq'])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = unknown.describe(...)

```python
result = s[:0].describe()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert np.isnan(result.iloc[2])
```


## Complete Example

```python
# Workflow
s = Series([None, None], dtype=object)
result = s.describe()
expected = Series([0, 0, np.nan, np.nan], dtype=object, index=['count', 'unique', 'top', 'freq'])
tm.assert_series_equal(result, expected)
result = s[:0].describe()
tm.assert_series_equal(result, expected)
assert np.isnan(result.iloc[2])
assert np.isnan(result.iloc[3])
```

## Next Steps


---

*Source: test_describe.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*