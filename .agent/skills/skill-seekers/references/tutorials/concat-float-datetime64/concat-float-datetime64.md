# How To: Concat Float Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat float datetime64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign df_time = DataFrame(...)

```python
df_time = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')})
```

### Step 2: Assign df_float = DataFrame(...)

```python
df_float = DataFrame({'A': pd.array([1.0], dtype='float64')})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [pd.array(['2000'], dtype='datetime64[ns]')[0], pd.array([1.0], dtype='float64')[0]]}, index=[0, 0])
```

### Step 4: Assign result = concat(...)

```python
result = concat([df_time, df_float])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': pd.array([], dtype='object')})
```

### Step 7: Assign result = concat(...)

```python
result = concat([df_time.iloc[:0], df_float.iloc[:0]])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': pd.array([1.0], dtype='object')})
```

### Step 10: Assign result = concat(...)

```python
result = concat([df_time.iloc[:0], df_float])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')})
```

### Step 13: Assign msg = 'The behavior of DataFrame concatenation with empty or all-NA entries'

```python
msg = 'The behavior of DataFrame concatenation with empty or all-NA entries'
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')}).astype({'A': 'object'})
```

### Step 16: Assign result = concat(...)

```python
result = concat([df_time, df_float.iloc[:0]])
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = concat(...)

```python
result = concat([df_time, df_float.iloc[:0]])
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
df_time = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')})
df_float = DataFrame({'A': pd.array([1.0], dtype='float64')})
expected = DataFrame({'A': [pd.array(['2000'], dtype='datetime64[ns]')[0], pd.array([1.0], dtype='float64')[0]]}, index=[0, 0])
result = concat([df_time, df_float])
tm.assert_frame_equal(result, expected)
expected = DataFrame({'A': pd.array([], dtype='object')})
result = concat([df_time.iloc[:0], df_float.iloc[:0]])
tm.assert_frame_equal(result, expected)
expected = DataFrame({'A': pd.array([1.0], dtype='object')})
result = concat([df_time.iloc[:0], df_float])
tm.assert_frame_equal(result, expected)
if not using_array_manager:
    expected = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')})
    msg = 'The behavior of DataFrame concatenation with empty or all-NA entries'
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = concat([df_time, df_float.iloc[:0]])
    tm.assert_frame_equal(result, expected)
else:
    expected = DataFrame({'A': pd.array(['2000'], dtype='datetime64[ns]')}).astype({'A': 'object'})
    result = concat([df_time, df_float.iloc[:0]])
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:570 | Complexity: Advanced | Last updated: 2026-06-02*