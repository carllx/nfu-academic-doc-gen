# How To: Logical Operators Bool Dtype With Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators bool dtype with int

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

### Step 4: Assign res = value

```python
res = s_tft & 0
```

### Step 5: Assign expected = s_fff

```python
expected = s_fff
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Assign res = value

```python
res = s_tft & 1
```

### Step 8: Assign expected = s_tft

```python
expected = s_tft
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
index = list('bca')
s_tft = Series([True, False, True], index=index)
s_fff = Series([False, False, False], index=index)
res = s_tft & 0
expected = s_fff
tm.assert_series_equal(res, expected)
res = s_tft & 1
expected = s_tft
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:167 | Complexity: Advanced | Last updated: 2026-06-02*