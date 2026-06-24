# How To: Map Series Stringdtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map series stringdtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_string_dtype, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign ser1 = Series(...)

```python
ser1 = Series(data=['cat', 'dog', 'rabbit'], index=['id1', 'id2', 'id3'], dtype=any_string_dtype)
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series(['id3', 'id2', 'id1', 'id7000'], dtype=any_string_dtype)
```

### Step 3: Assign result = ser2.map(...)

```python
result = ser2.map(ser1)
```

### Step 4: Assign item = value

```python
item = pd.NA
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(data=['rabbit', 'dog', 'cat', item], dtype=any_string_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign item = value

```python
item = np.nan
```

### Step 8: Assign expected = expected.astype(...)

```python
expected = expected.astype('str')
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype, using_infer_string

# Workflow
ser1 = Series(data=['cat', 'dog', 'rabbit'], index=['id1', 'id2', 'id3'], dtype=any_string_dtype)
ser2 = Series(['id3', 'id2', 'id1', 'id7000'], dtype=any_string_dtype)
result = ser2.map(ser1)
item = pd.NA
if ser2.dtype == object:
    item = np.nan
expected = Series(data=['rabbit', 'dog', 'cat', item], dtype=any_string_dtype)
if using_infer_string and any_string_dtype == 'object':
    expected = expected.astype('str')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_map.py:88 | Complexity: Advanced | Last updated: 2026-06-02*