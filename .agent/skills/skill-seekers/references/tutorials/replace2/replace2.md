# How To: Replace2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace2

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign N = 50

```python
N = 50
```

**Verification:**
```python
assert (rs[:5] == -1).all()
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(np.fabs(np.random.default_rng(2).standard_normal(N)), pd.date_range('2020-01-01', periods=N), dtype=object)
```

**Verification:**
```python
assert (rs[6:10] == -1).all()
```

### Step 3: Assign unknown = value

```python
ser[:5] = np.nan
```

**Verification:**
```python
assert (rs[20:30] == -1).all()
```

### Step 4: Assign unknown = 'foo'

```python
ser[6:10] = 'foo'
```

**Verification:**
```python
assert pd.isna(ser[:5]).all()
```

### Step 5: Assign unknown = 'bar'

```python
ser[20:30] = 'bar'
```

**Verification:**
```python
assert (rs[:5] == -1).all()
```

### Step 6: Assign msg = 'Downcasting behavior in `replace`'

```python
msg = 'Downcasting behavior in `replace`'
```

**Verification:**
```python
assert (rs[6:10] == -2).all()
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, rs2)
```

**Verification:**
```python
assert (rs[20:30] == -3).all()
```

### Step 8: Assign rs = ser.replace(...)

```python
rs = ser.replace([np.nan, 'foo', 'bar'], -1)
```

**Verification:**
```python
assert pd.isna(ser[:5]).all()
```

### Step 9: Assign rs = ser.replace(...)

```python
rs = ser.replace({np.nan: -1, 'foo': -2, 'bar': -3})
```

**Verification:**
```python
assert return_value is None
```

### Step 10: Assign rs2 = ser.replace(...)

```python
rs2 = ser.replace([np.nan, 'foo', 'bar'], [-1, -2, -3])
```

**Verification:**
```python
assert (ser[:5] == -1).all()
```

### Step 11: Assign return_value = ser.replace(...)

```python
return_value = ser.replace([np.nan, 'foo', 'bar'], -1, inplace=True)
```

**Verification:**
```python
assert (ser[6:10] == -1).all()
```


## Complete Example

```python
# Workflow
N = 50
ser = pd.Series(np.fabs(np.random.default_rng(2).standard_normal(N)), pd.date_range('2020-01-01', periods=N), dtype=object)
ser[:5] = np.nan
ser[6:10] = 'foo'
ser[20:30] = 'bar'
msg = 'Downcasting behavior in `replace`'
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs = ser.replace([np.nan, 'foo', 'bar'], -1)
assert (rs[:5] == -1).all()
assert (rs[6:10] == -1).all()
assert (rs[20:30] == -1).all()
assert pd.isna(ser[:5]).all()
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs = ser.replace({np.nan: -1, 'foo': -2, 'bar': -3})
assert (rs[:5] == -1).all()
assert (rs[6:10] == -2).all()
assert (rs[20:30] == -3).all()
assert pd.isna(ser[:5]).all()
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs2 = ser.replace([np.nan, 'foo', 'bar'], [-1, -2, -3])
tm.assert_series_equal(rs, rs2)
with tm.assert_produces_warning(FutureWarning, match=msg):
    return_value = ser.replace([np.nan, 'foo', 'bar'], -1, inplace=True)
assert return_value is None
assert (ser[:5] == -1).all()
assert (ser[6:10] == -1).all()
assert (ser[20:30] == -1).all()
```

## Next Steps


---

*Source: test_replace.py:290 | Complexity: Advanced | Last updated: 2026-06-02*