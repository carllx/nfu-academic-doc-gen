# How To: Isna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isna

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0, 5.4, 3, np.nan, -0.001])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False, False, False, True, False])
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.isna(), expected)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.notna(), ~expected)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(['hi', '', np.nan])
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([False, False, True])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.isna(), expected)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.notna(), ~expected)
```


## Complete Example

```python
# Workflow
ser = Series([0, 5.4, 3, np.nan, -0.001])
expected = Series([False, False, False, True, False])
tm.assert_series_equal(ser.isna(), expected)
tm.assert_series_equal(ser.notna(), ~expected)
ser = Series(['hi', '', np.nan])
expected = Series([False, False, True])
tm.assert_series_equal(ser.isna(), expected)
tm.assert_series_equal(ser.notna(), ~expected)
```

## Next Steps


---

*Source: test_isna.py:26 | Complexity: Advanced | Last updated: 2026-06-02*