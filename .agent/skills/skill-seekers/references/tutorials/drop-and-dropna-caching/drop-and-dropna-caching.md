# How To: Drop And Dropna Caching

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop and dropna caching

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign original = Series(...)

```python
original = Series([1, 2, np.nan], name='A')
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([1, 2], dtype=original.dtype, name='A')
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': original.values.copy()})
```

### Step 4: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 5: Call unknown.dropna()

```python
df['A'].dropna()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['A'], original)
```

### Step 7: Assign ser = value

```python
ser = df['A']
```

### Step 8: Assign return_value = ser.dropna(...)

```python
return_value = ser.dropna(inplace=True)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['A'], original)
```

**Verification:**
```python
assert return_value is None
```

### Step 11: Call unknown.drop()

```python
df2['A'].drop([1])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df2['A'], original)
```

### Step 13: Assign ser = value

```python
ser = df2['A']
```

### Step 14: Assign return_value = ser.drop(...)

```python
return_value = ser.drop([1], inplace=True)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, original.drop([1]))
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df2['A'], original)
```

**Verification:**
```python
assert return_value is None
```


## Complete Example

```python
# Workflow
original = Series([1, 2, np.nan], name='A')
expected = Series([1, 2], dtype=original.dtype, name='A')
df = DataFrame({'A': original.values.copy()})
df2 = df.copy()
df['A'].dropna()
tm.assert_series_equal(df['A'], original)
ser = df['A']
return_value = ser.dropna(inplace=True)
tm.assert_series_equal(ser, expected)
tm.assert_series_equal(df['A'], original)
assert return_value is None
df2['A'].drop([1])
tm.assert_series_equal(df2['A'], original)
ser = df2['A']
return_value = ser.drop([1], inplace=True)
tm.assert_series_equal(ser, original.drop([1]))
tm.assert_series_equal(df2['A'], original)
assert return_value is None
```

## Next Steps


---

*Source: test_dropna.py:132 | Complexity: Advanced | Last updated: 2026-06-02*