# How To: To Timestamp Non Contiguous

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timestamp non contiguous

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2021-10-18', periods=9, freq='D')
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period()
```

### Step 3: Assign result = unknown.to_timestamp(...)

```python
result = pi[::2].to_timestamp()
```

### Step 4: Assign expected = value

```python
expected = dti[::2]
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = unknown.to_timestamp(...)

```python
result = pi._data[::2].to_timestamp()
```

### Step 7: Assign expected = value

```python
expected = dti._data[::2]
```

### Step 8: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected, check_freq=False)
```

### Step 9: Assign result = unknown.to_timestamp(...)

```python
result = pi[::-1].to_timestamp()
```

### Step 10: Assign expected = value

```python
expected = dti[::-1]
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign result = unknown.to_timestamp(...)

```python
result = pi._data[::-1].to_timestamp()
```

### Step 13: Assign expected = value

```python
expected = dti._data[::-1]
```

### Step 14: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected, check_freq=False)
```

### Step 15: Assign result = unknown.to_timestamp(...)

```python
result = pi[::2][::-1].to_timestamp()
```

### Step 16: Assign expected = value

```python
expected = dti[::2][::-1]
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 18: Assign result = unknown.to_timestamp(...)

```python
result = pi._data[::2][::-1].to_timestamp()
```

### Step 19: Assign expected = value

```python
expected = dti._data[::2][::-1]
```

### Step 20: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected, check_freq=False)
```


## Complete Example

```python
# Workflow
dti = date_range('2021-10-18', periods=9, freq='D')
pi = dti.to_period()
result = pi[::2].to_timestamp()
expected = dti[::2]
tm.assert_index_equal(result, expected)
result = pi._data[::2].to_timestamp()
expected = dti._data[::2]
tm.assert_datetime_array_equal(result, expected, check_freq=False)
result = pi[::-1].to_timestamp()
expected = dti[::-1]
tm.assert_index_equal(result, expected)
result = pi._data[::-1].to_timestamp()
expected = dti._data[::-1]
tm.assert_datetime_array_equal(result, expected, check_freq=False)
result = pi[::2][::-1].to_timestamp()
expected = dti[::2][::-1]
tm.assert_index_equal(result, expected)
result = pi._data[::2][::-1].to_timestamp()
expected = dti._data[::2][::-1]
tm.assert_datetime_array_equal(result, expected, check_freq=False)
```

## Next Steps


---

*Source: test_to_timestamp.py:19 | Complexity: Advanced | Last updated: 2026-06-02*