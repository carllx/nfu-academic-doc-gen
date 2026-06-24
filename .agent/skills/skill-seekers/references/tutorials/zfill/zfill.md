# How To: Zfill

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zfill

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['1', '22', 'aaa', '333', '45678'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.zfill(...)

```python
result = s.str.zfill(5)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['00001', '00022', '00aaa', '00333', '45678'], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([v.zfill(5) for v in np.array(s)], dtype=np.object_)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```

### Step 7: Assign result = s.str.zfill(...)

```python
result = s.str.zfill(3)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(['001', '022', 'aaa', '333', '45678'], dtype=any_string_dtype)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([v.zfill(3) for v in np.array(s)], dtype=np.object_)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```

### Step 12: Assign s = Series(...)

```python
s = Series(['1', np.nan, 'aaa', np.nan, '45678'], dtype=any_string_dtype)
```

### Step 13: Assign result = s.str.zfill(...)

```python
result = s.str.zfill(5)
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(['00001', np.nan, '00aaa', np.nan, '45678'], dtype=any_string_dtype)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['1', '22', 'aaa', '333', '45678'], dtype=any_string_dtype)
result = s.str.zfill(5)
expected = Series(['00001', '00022', '00aaa', '00333', '45678'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.zfill(5) for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
result = s.str.zfill(3)
expected = Series(['001', '022', 'aaa', '333', '45678'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.zfill(3) for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
s = Series(['1', np.nan, 'aaa', np.nan, '45678'], dtype=any_string_dtype)
result = s.str.zfill(5)
expected = Series(['00001', np.nan, '00aaa', np.nan, '45678'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_justify.py:349 | Complexity: Advanced | Last updated: 2026-06-02*