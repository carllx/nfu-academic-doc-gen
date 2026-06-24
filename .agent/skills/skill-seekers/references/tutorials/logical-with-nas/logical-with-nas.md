# How To: Logical With Nas

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test logical with nas

## Prerequisites

**Required Modules:**
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d = DataFrame(...)

```python
d = DataFrame({'a': [np.nan, False], 'b': [True, True]})
```

### Step 2: Assign result = value

```python
result = d['a'] | d['b']
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([False, True])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = d['a'].fillna(False) | d['b']
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([True, True])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign msg = "The 'downcast' keyword in fillna is deprecated"

```python
msg = "The 'downcast' keyword in fillna is deprecated"
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([True, True])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = d['a'].fillna(False, downcast=False) | d['b']
```


## Complete Example

```python
# Workflow
d = DataFrame({'a': [np.nan, False], 'b': [True, True]})
result = d['a'] | d['b']
expected = Series([False, True])
tm.assert_series_equal(result, expected)
result = d['a'].fillna(False) | d['b']
expected = Series([True, True])
tm.assert_series_equal(result, expected)
msg = "The 'downcast' keyword in fillna is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = d['a'].fillna(False, downcast=False) | d['b']
expected = Series([True, True])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:158 | Complexity: Advanced | Last updated: 2026-06-02*