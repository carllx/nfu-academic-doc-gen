# How To: Mode Nullable Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mode nullable dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 3, 2, pd.NA, 3, 2, pd.NA], dtype=any_numeric_ea_dtype)
```

### Step 2: Assign result = ser.mode(...)

```python
result = ser.mode(dropna=False)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([2, 3, pd.NA], dtype=any_numeric_ea_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.mode(...)

```python
result = ser.mode(dropna=True)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([2, 3], dtype=any_numeric_ea_dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign unknown = value

```python
ser[-1] = pd.NA
```

### Step 9: Assign result = ser.mode(...)

```python
result = ser.mode(dropna=True)
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([2, 3], dtype=any_numeric_ea_dtype)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = ser.mode(...)

```python
result = ser.mode(dropna=False)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([pd.NA], dtype=any_numeric_ea_dtype)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype

# Workflow
ser = Series([1, 3, 2, pd.NA, 3, 2, pd.NA], dtype=any_numeric_ea_dtype)
result = ser.mode(dropna=False)
expected = Series([2, 3, pd.NA], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(result, expected)
result = ser.mode(dropna=True)
expected = Series([2, 3], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(result, expected)
ser[-1] = pd.NA
result = ser.mode(dropna=True)
expected = Series([2, 3], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(result, expected)
result = ser.mode(dropna=False)
expected = Series([pd.NA], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:32 | Complexity: Advanced | Last updated: 2026-06-02*