# How To: Where String Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where string dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(['a', 'b', 'c', 'd'], index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
```

### Step 2: Assign filtered_obj = frame_or_series(...)

```python
filtered_obj = frame_or_series(['b', 'c'], index=['id2', 'id3'], dtype=StringDtype())
```

### Step 3: Assign filter_ser = Series(...)

```python
filter_ser = Series([False, True, True, False])
```

### Step 4: Assign result = obj.where(...)

```python
result = obj.where(filter_ser, filtered_obj)
```

### Step 5: Assign expected = frame_or_series(...)

```python
expected = frame_or_series([pd.NA, 'b', 'c', pd.NA], index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 7: Assign result = obj.mask(...)

```python
result = obj.mask(~filter_ser, filtered_obj)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Call obj.mask()

```python
obj.mask(~filter_ser, filtered_obj, inplace=True)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = frame_or_series(['a', 'b', 'c', 'd'], index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
filtered_obj = frame_or_series(['b', 'c'], index=['id2', 'id3'], dtype=StringDtype())
filter_ser = Series([False, True, True, False])
result = obj.where(filter_ser, filtered_obj)
expected = frame_or_series([pd.NA, 'b', 'c', pd.NA], index=['id1', 'id2', 'id3', 'id4'], dtype=StringDtype())
tm.assert_equal(result, expected)
result = obj.mask(~filter_ser, filtered_obj)
tm.assert_equal(result, expected)
obj.mask(~filter_ser, filtered_obj, inplace=True)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_where.py:845 | Complexity: Advanced | Last updated: 2026-06-02*