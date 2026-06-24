# How To: Numeric Only Flag

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric only flag

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: meth
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['foo', 'bar', 'baz'])
```

### Step 2: Assign df1 = df1.astype(...)

```python
df1 = df1.astype({'foo': object})
```

### Step 3: Assign unknown = '100'

```python
df1.loc[0, 'foo'] = '100'
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['foo', 'bar', 'baz'])
```

### Step 5: Assign df2 = df2.astype(...)

```python
df2 = df2.astype({'foo': object})
```

### Step 6: Assign unknown = 'a'

```python
df2.loc[0, 'foo'] = 'a'
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(df1, meth)(axis=1, numeric_only=True)
```

### Step 8: Assign expected = getattr(...)

```python
expected = getattr(df1[['bar', 'baz']], meth)(axis=1)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 10: Assign result = getattr(...)

```python
result = getattr(df2, meth)(axis=1, numeric_only=True)
```

### Step 11: Assign expected = getattr(...)

```python
expected = getattr(df2[['bar', 'baz']], meth)(axis=1)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 13: Assign msg = "unsupported operand type\\(s\\) for -: 'float' and 'str'"

```python
msg = "unsupported operand type\\(s\\) for -: 'float' and 'str'"
```

### Step 14: Assign msg = "could not convert string to float: 'a'"

```python
msg = "could not convert string to float: 'a'"
```

### Step 15: Call getattr()

```python
getattr(df1, meth)(axis=1, numeric_only=False)
```

### Step 16: Call getattr()

```python
getattr(df2, meth)(axis=1, numeric_only=False)
```


## Complete Example

```python
# Setup
# Fixtures: meth

# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['foo', 'bar', 'baz'])
df1 = df1.astype({'foo': object})
df1.loc[0, 'foo'] = '100'
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), columns=['foo', 'bar', 'baz'])
df2 = df2.astype({'foo': object})
df2.loc[0, 'foo'] = 'a'
result = getattr(df1, meth)(axis=1, numeric_only=True)
expected = getattr(df1[['bar', 'baz']], meth)(axis=1)
tm.assert_series_equal(expected, result)
result = getattr(df2, meth)(axis=1, numeric_only=True)
expected = getattr(df2[['bar', 'baz']], meth)(axis=1)
tm.assert_series_equal(expected, result)
msg = "unsupported operand type\\(s\\) for -: 'float' and 'str'"
with pytest.raises(TypeError, match=msg):
    getattr(df1, meth)(axis=1, numeric_only=False)
msg = "could not convert string to float: 'a'"
with pytest.raises(TypeError, match=msg):
    getattr(df2, meth)(axis=1, numeric_only=False)
```

## Next Steps


---

*Source: test_reductions.py:545 | Complexity: Advanced | Last updated: 2026-06-02*