# How To: Replace Mixed Types

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace mixed types

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(np.arange(5), dtype='int64')
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign unknown = value

```python
tr, v = ([3], [3.0])
```

### Step 3: Call check_replace()

```python
check_replace(tr, v, ser)
```

### Step 4: Call check_replace()

```python
check_replace(tr[0], v[0], ser)
```

### Step 5: Assign e = pd.Series(...)

```python
e = pd.Series([0, 1, 2, 3.5, 4])
```

### Step 6: Assign unknown = value

```python
tr, v = ([3], [3.5])
```

### Step 7: Call check_replace()

```python
check_replace(tr, v, e)
```

### Step 8: Assign e = pd.Series(...)

```python
e = pd.Series([0, 1, 2, 3.5, 'a'])
```

### Step 9: Assign unknown = value

```python
tr, v = ([3, 4], [3.5, 'a'])
```

### Step 10: Call check_replace()

```python
check_replace(tr, v, e)
```

### Step 11: Assign e = pd.Series(...)

```python
e = pd.Series([0, 1, 2, 3.5, pd.Timestamp('20130101')])
```

### Step 12: Assign unknown = value

```python
tr, v = ([3, 4], [3.5, pd.Timestamp('20130101')])
```

### Step 13: Call check_replace()

```python
check_replace(tr, v, e)
```

### Step 14: Assign e = pd.Series(...)

```python
e = pd.Series([0, 1, 2, 3.5, True], dtype='object')
```

### Step 15: Assign unknown = value

```python
tr, v = ([3, 4], [3.5, True])
```

### Step 16: Call check_replace()

```python
check_replace(tr, v, e)
```

### Step 17: Assign dr = pd.Series(...)

```python
dr = pd.Series(pd.date_range('1/1/2001', '1/10/2001', freq='D'))
```

### Step 18: Assign result = dr.astype.replace(...)

```python
result = dr.astype(object).replace([dr[0], dr[1], dr[2]], [1.0, 2, 'a'])
```

### Step 19: Assign expected = pd.Series(...)

```python
expected = pd.Series([1.0, 2, 'a'] + dr[3:].tolist(), dtype=object)
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 21: Assign sc = ser.copy(...)

```python
sc = ser.copy()
```

### Step 22: Assign result = ser.replace(...)

```python
result = ser.replace(to_rep, val)
```

### Step 23: Assign return_value = sc.replace(...)

```python
return_value = sc.replace(to_rep, val, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 24: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 25: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, sc)
```


## Complete Example

```python
# Workflow
ser = pd.Series(np.arange(5), dtype='int64')

def check_replace(to_rep, val, expected):
    sc = ser.copy()
    result = ser.replace(to_rep, val)
    return_value = sc.replace(to_rep, val, inplace=True)
    assert return_value is None
    tm.assert_series_equal(expected, result)
    tm.assert_series_equal(expected, sc)
tr, v = ([3], [3.0])
check_replace(tr, v, ser)
check_replace(tr[0], v[0], ser)
e = pd.Series([0, 1, 2, 3.5, 4])
tr, v = ([3], [3.5])
check_replace(tr, v, e)
e = pd.Series([0, 1, 2, 3.5, 'a'])
tr, v = ([3, 4], [3.5, 'a'])
check_replace(tr, v, e)
e = pd.Series([0, 1, 2, 3.5, pd.Timestamp('20130101')])
tr, v = ([3, 4], [3.5, pd.Timestamp('20130101')])
check_replace(tr, v, e)
e = pd.Series([0, 1, 2, 3.5, True], dtype='object')
tr, v = ([3, 4], [3.5, True])
check_replace(tr, v, e)
dr = pd.Series(pd.date_range('1/1/2001', '1/10/2001', freq='D'))
result = dr.astype(object).replace([dr[0], dr[1], dr[2]], [1.0, 2, 'a'])
expected = pd.Series([1.0, 2, 'a'] + dr[3:].tolist(), dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:214 | Complexity: Advanced | Last updated: 2026-06-02*