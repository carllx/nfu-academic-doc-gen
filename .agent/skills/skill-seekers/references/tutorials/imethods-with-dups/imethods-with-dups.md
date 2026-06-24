# How To: Imethods With Dups

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test imethods with dups

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(5), index=[1, 1, 2, 2, 3], dtype='int64')
```

**Verification:**
```python
assert result == 2
```

### Step 2: Assign result = value

```python
result = s.iloc[2]
```

**Verification:**
```python
assert result == 2
```

### Step 3: Assign result = value

```python
result = s.iat[2]
```

**Verification:**
```python
assert result == 2
```

### Step 4: Assign msg = 'index 10 is out of bounds for axis 0 with size 5'

```python
msg = 'index 10 is out of bounds for axis 0 with size 5'
```

### Step 5: Assign msg = 'index -10 is out of bounds for axis 0 with size 5'

```python
msg = 'index -10 is out of bounds for axis 0 with size 5'
```

### Step 6: Assign result = value

```python
result = s.iloc[[2, 3]]
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([2, 3], [2, 2], dtype='int64')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign df = s.to_frame(...)

```python
df = s.to_frame()
```

### Step 10: Assign result = value

```python
result = df.iloc[2]
```

### Step 11: Assign expected = Series(...)

```python
expected = Series(2, index=[0], name=2)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = df.iat[2, 0]
```

**Verification:**
```python
assert result == 2
```

### Step 14: s.iat[10]

```python
s.iat[10]
```

### Step 15: s.iat[-10]

```python
s.iat[-10]
```


## Complete Example

```python
# Workflow
s = Series(range(5), index=[1, 1, 2, 2, 3], dtype='int64')
result = s.iloc[2]
assert result == 2
result = s.iat[2]
assert result == 2
msg = 'index 10 is out of bounds for axis 0 with size 5'
with pytest.raises(IndexError, match=msg):
    s.iat[10]
msg = 'index -10 is out of bounds for axis 0 with size 5'
with pytest.raises(IndexError, match=msg):
    s.iat[-10]
result = s.iloc[[2, 3]]
expected = Series([2, 3], [2, 2], dtype='int64')
tm.assert_series_equal(result, expected)
df = s.to_frame()
result = df.iloc[2]
expected = Series(2, index=[0], name=2)
tm.assert_series_equal(result, expected)
result = df.iat[2, 0]
assert result == 2
```

## Next Steps


---

*Source: test_scalar.py:108 | Complexity: Advanced | Last updated: 2026-06-02*