# How To: More Na Comparisons

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test more na comparisons

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign left = Series(...)

```python
left = Series(['a', np.nan, 'c'], dtype=dtype)
```

### Step 2: Assign right = Series(...)

```python
right = Series(['a', np.nan, 'd'], dtype=dtype)
```

### Step 3: Assign result = value

```python
result = left == right
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([True, False, False])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = left != right
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([False, True, True])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = left == np.nan
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([False, False, False])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = left != np.nan
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([True, True, True])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
left = Series(['a', np.nan, 'c'], dtype=dtype)
right = Series(['a', np.nan, 'd'], dtype=dtype)
result = left == right
expected = Series([True, False, False])
tm.assert_series_equal(result, expected)
result = left != right
expected = Series([False, True, True])
tm.assert_series_equal(result, expected)
result = left == np.nan
expected = Series([False, False, False])
tm.assert_series_equal(result, expected)
result = left != np.nan
expected = Series([True, True, True])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_object.py:57 | Complexity: Advanced | Last updated: 2026-06-02*