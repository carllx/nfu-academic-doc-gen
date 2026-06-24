# How To: Invert

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invert

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([True, False, None], dtype='boolean')
```

### Step 2: Assign expected = pd.array(...)

```python
expected = pd.array([False, True, None], dtype='boolean')
```

### Step 3: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(~a, expected)
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(expected, index=['a', 'b', 'c'], name='name')
```

### Step 5: Assign result = value

```python
result = ~pd.Series(a, index=['a', 'b', 'c'], name='name')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': a, 'B': [True, False, False]}, index=['a', 'b', 'c'])
```

### Step 8: Assign result = value

```python
result = ~df
```

### Step 9: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': expected, 'B': [False, True, True]}, index=['a', 'b', 'c'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.array([True, False, None], dtype='boolean')
expected = pd.array([False, True, None], dtype='boolean')
tm.assert_extension_array_equal(~a, expected)
expected = pd.Series(expected, index=['a', 'b', 'c'], name='name')
result = ~pd.Series(a, index=['a', 'b', 'c'], name='name')
tm.assert_series_equal(result, expected)
df = pd.DataFrame({'A': a, 'B': [True, False, False]}, index=['a', 'b', 'c'])
result = ~df
expected = pd.DataFrame({'A': expected, 'B': [False, True, True]}, index=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ops.py:6 | Complexity: Advanced | Last updated: 2026-06-02*