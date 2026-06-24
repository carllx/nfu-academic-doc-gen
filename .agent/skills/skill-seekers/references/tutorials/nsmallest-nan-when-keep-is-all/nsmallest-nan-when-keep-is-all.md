# How To: Nsmallest Nan When Keep Is All

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nsmallest nan when keep is all

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, 3, 3, 3, None])
```

### Step 2: Assign result = s.nsmallest(...)

```python
result = s.nsmallest(3, keep='all')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1.0, 2.0, 3.0, 3.0, 3.0])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign s = Series(...)

```python
s = Series([1, 2, None, None, None])
```

### Step 6: Assign result = s.nsmallest(...)

```python
result = s.nsmallest(3, keep='all')
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([1, 2, None, None, None])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([1, 2, 3, 3, 3, None])
result = s.nsmallest(3, keep='all')
expected = Series([1.0, 2.0, 3.0, 3.0, 3.0])
tm.assert_series_equal(result, expected)
s = Series([1, 2, None, None, None])
result = s.nsmallest(3, keep='all')
expected = Series([1, 2, None, None, None])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:238 | Complexity: Advanced | Last updated: 2026-06-02*