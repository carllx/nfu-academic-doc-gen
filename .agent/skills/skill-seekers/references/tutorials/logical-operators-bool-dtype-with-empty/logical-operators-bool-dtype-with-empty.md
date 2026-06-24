# How To: Logical Operators Bool Dtype With Empty

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators bool dtype with empty

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

### Step 3: Assign s_fff = Series(...)

```python
s_fff = Series([False, False, False], index=index)
```

### Step 4: Assign s_empty = Series(...)

```python
s_empty = Series([], dtype=object)
```

### Step 5: Assign res = value

```python
res = s_tft & s_empty
```

### Step 6: Assign expected = s_fff.sort_index(...)

```python
expected = s_fff.sort_index()
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 8: Assign res = value

```python
res = s_tft | s_empty
```

### Step 9: Assign expected = s_tft.sort_index(...)

```python
expected = s_tft.sort_index()
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
index = list('bca')
s_tft = Series([True, False, True], index=index)
s_fff = Series([False, False, False], index=index)
s_empty = Series([], dtype=object)
res = s_tft & s_empty
expected = s_fff.sort_index()
tm.assert_series_equal(res, expected)
res = s_tft | s_empty
expected = s_tft.sort_index()
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:38 | Complexity: Advanced | Last updated: 2026-06-02*