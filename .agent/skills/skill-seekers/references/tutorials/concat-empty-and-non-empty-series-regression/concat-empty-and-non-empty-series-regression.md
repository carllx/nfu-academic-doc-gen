# How To: Concat Empty And Non Empty Series Regression

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty and non empty series regression

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([], dtype=object)
```

### Step 3: Assign expected = s1

```python
expected = s1
```

### Step 4: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat([s1, s2])
```


## Complete Example

```python
# Workflow
s1 = Series([1])
s2 = Series([], dtype=object)
expected = s1
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = concat([s1, s2])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*