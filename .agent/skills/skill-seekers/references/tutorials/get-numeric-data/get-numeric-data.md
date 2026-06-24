# How To: Get Numeric Data

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get numeric data

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign datetime64name = value

```python
datetime64name = np.dtype('M8[s]').name
```

### Step 2: Assign objectname = value

```python
objectname = np.dtype(np.object_).name
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'f': Timestamp('20010102')}, index=np.arange(10))
```

### Step 4: Assign result = value

```python
result = df.dtypes
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64'), np.dtype('int64'), np.dtype(objectname) if not using_infer_string else pd.StringDtype(na_value=np.nan), np.dtype(datetime64name)], index=['a', 'b', 'c', 'f'])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'd': np.array([1.0] * 10, dtype='float32'), 'e': np.array([1] * 10, dtype='int32'), 'f': np.array([1] * 10, dtype='int16'), 'g': Timestamp('20010102')}, index=np.arange(10))
```

### Step 8: Assign result = df._get_numeric_data(...)

```python
result = df._get_numeric_data()
```

### Step 9: Assign expected = value

```python
expected = df.loc[:, ['a', 'b', 'd', 'e', 'f']]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign only_obj = value

```python
only_obj = df.loc[:, ['c', 'g']]
```

### Step 12: Assign result = only_obj._get_numeric_data(...)

```python
result = only_obj._get_numeric_data()
```

### Step 13: Assign expected = value

```python
expected = df.loc[:, []]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign df = DataFrame.from_dict(...)

```python
df = DataFrame.from_dict({'a': [1, 2], 'b': ['foo', 'bar'], 'c': [np.pi, np.e]})
```

### Step 16: Assign result = df._get_numeric_data(...)

```python
result = df._get_numeric_data()
```

### Step 17: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict({'a': [1, 2], 'c': [np.pi, np.e]})
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 19: Assign df = result.copy(...)

```python
df = result.copy()
```

### Step 20: Assign result = df._get_numeric_data(...)

```python
result = df._get_numeric_data()
```

### Step 21: Assign expected = df

```python
expected = df
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
datetime64name = np.dtype('M8[s]').name
objectname = np.dtype(np.object_).name
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'f': Timestamp('20010102')}, index=np.arange(10))
result = df.dtypes
expected = Series([np.dtype('float64'), np.dtype('int64'), np.dtype(objectname) if not using_infer_string else pd.StringDtype(na_value=np.nan), np.dtype(datetime64name)], index=['a', 'b', 'c', 'f'])
tm.assert_series_equal(result, expected)
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'd': np.array([1.0] * 10, dtype='float32'), 'e': np.array([1] * 10, dtype='int32'), 'f': np.array([1] * 10, dtype='int16'), 'g': Timestamp('20010102')}, index=np.arange(10))
result = df._get_numeric_data()
expected = df.loc[:, ['a', 'b', 'd', 'e', 'f']]
tm.assert_frame_equal(result, expected)
only_obj = df.loc[:, ['c', 'g']]
result = only_obj._get_numeric_data()
expected = df.loc[:, []]
tm.assert_frame_equal(result, expected)
df = DataFrame.from_dict({'a': [1, 2], 'b': ['foo', 'bar'], 'c': [np.pi, np.e]})
result = df._get_numeric_data()
expected = DataFrame.from_dict({'a': [1, 2], 'c': [np.pi, np.e]})
tm.assert_frame_equal(result, expected)
df = result.copy()
result = df._get_numeric_data()
expected = df
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_numeric_data.py:23 | Complexity: Advanced | Last updated: 2026-06-02*