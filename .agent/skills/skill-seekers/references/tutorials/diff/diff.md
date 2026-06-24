# How To: Diff

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([True, True, False, False, True, None, True, None, False], dtype='boolean')
```

### Step 2: Assign result = pd.core.algorithms.diff(...)

```python
result = pd.core.algorithms.diff(a, 1)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array([None, False, True, False, True, None, None, None, None], dtype='boolean')
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign ser = pd.Series(...)

```python
ser = pd.Series(a)
```

### Step 6: Assign result = ser.diff(...)

```python
result = ser.diff()
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series(expected)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.array([True, True, False, False, True, None, True, None, False], dtype='boolean')
result = pd.core.algorithms.diff(a, 1)
expected = pd.array([None, False, True, False, True, None, None, None, None], dtype='boolean')
tm.assert_extension_array_equal(result, expected)
ser = pd.Series(a)
result = ser.diff()
expected = pd.Series(expected)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:113 | Complexity: Advanced | Last updated: 2026-06-02*