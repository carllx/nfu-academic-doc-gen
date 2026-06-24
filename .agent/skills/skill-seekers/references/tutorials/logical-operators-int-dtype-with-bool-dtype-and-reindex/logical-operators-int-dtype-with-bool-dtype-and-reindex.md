# How To: Logical Operators Int Dtype With Bool Dtype And Reindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with bool dtype and reindex

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

### Step 1: Assign index = list(...)

```python
index = list('bca')
```

### Step 2: Assign s_tft = Series(...)

```python
s_tft = Series([True, False, True], index=index)
```

### Step 3: Assign s_tft = Series(...)

```python
s_tft = Series([True, False, True], index=index)
```

### Step 4: Assign s_tff = Series(...)

```python
s_tff = Series([True, False, False], index=index)
```

### Step 5: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([False] * 7, index=[0, 1, 2, 3, 'a', 'b', 'c'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([False] * 7, index=[0, 1, 2, 3, 'a', 'b', 'c'])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign s_a0b1c0 = Series(...)

```python
s_a0b1c0 = Series([1], list('b'))
```

### Step 11: Assign expected = s_tff.reindex(...)

```python
expected = s_tff.reindex(list('abc'))
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 13: Assign expected = s_tft.reindex(...)

```python
expected = s_tft.reindex(list('abc'))
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 15: Assign result = value

```python
result = s_tft & s_0123
```

### Step 16: Assign result = value

```python
result = s_0123 & s_tft
```

### Step 17: Assign res = value

```python
res = s_tft & s_a0b1c0
```

### Step 18: Assign res = value

```python
res = s_tft | s_a0b1c0
```


## Complete Example

```python
# Workflow
index = list('bca')
s_tft = Series([True, False, True], index=index)
s_tft = Series([True, False, True], index=index)
s_tff = Series([True, False, False], index=index)
s_0123 = Series(range(4), dtype='int64')
expected = Series([False] * 7, index=[0, 1, 2, 3, 'a', 'b', 'c'])
with tm.assert_produces_warning(FutureWarning):
    result = s_tft & s_0123
tm.assert_series_equal(result, expected)
expected = Series([False] * 7, index=[0, 1, 2, 3, 'a', 'b', 'c'])
with tm.assert_produces_warning(FutureWarning):
    result = s_0123 & s_tft
tm.assert_series_equal(result, expected)
s_a0b1c0 = Series([1], list('b'))
with tm.assert_produces_warning(FutureWarning):
    res = s_tft & s_a0b1c0
expected = s_tff.reindex(list('abc'))
tm.assert_series_equal(res, expected)
with tm.assert_produces_warning(FutureWarning):
    res = s_tft | s_a0b1c0
expected = s_tft.reindex(list('abc'))
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:224 | Complexity: Advanced | Last updated: 2026-06-02*