# How To: Logical Operators Int Dtype With Bool

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with bool

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False] * 4)
```

### Step 3: Assign result = value

```python
result = s_0123 & False
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'

```python
warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = s_0123 ^ False
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([False, True, True, True])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = s_0123 & [False]
```

### Step 12: Assign result = value

```python
result = s_0123 & (False,)
```


## Complete Example

```python
# Workflow
s_0123 = Series(range(4), dtype='int64')
expected = Series([False] * 4)
result = s_0123 & False
tm.assert_series_equal(result, expected)
warn_msg = 'Logical ops \\(and, or, xor\\) between Pandas objects and dtype-less sequences'
with tm.assert_produces_warning(FutureWarning, match=warn_msg):
    result = s_0123 & [False]
tm.assert_series_equal(result, expected)
with tm.assert_produces_warning(FutureWarning, match=warn_msg):
    result = s_0123 & (False,)
tm.assert_series_equal(result, expected)
result = s_0123 ^ False
expected = Series([False, True, True, True])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:128 | Complexity: Advanced | Last updated: 2026-06-02*