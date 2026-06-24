# How To: Corrwith With Objects

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corrwith with objects

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 2: Assign df2 = df1.copy(...)

```python
df2 = df1.copy()
```

### Step 3: Assign cols = value

```python
cols = ['A', 'B', 'C', 'D']
```

### Step 4: Assign unknown = 'foo'

```python
df1['obj'] = 'foo'
```

### Step 5: Assign unknown = 'bar'

```python
df2['obj'] = 'bar'
```

### Step 6: Assign result = df1.corrwith(...)

```python
result = df1.corrwith(df2, numeric_only=True)
```

### Step 7: Assign expected = unknown.corrwith(...)

```python
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = df1.corrwith(...)

```python
result = df1.corrwith(df2, axis=1, numeric_only=True)
```

### Step 10: Assign expected = unknown.corrwith(...)

```python
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols], axis=1)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign msg = "Cannot perform reduction 'mean' with string dtype"

```python
msg = "Cannot perform reduction 'mean' with string dtype"
```

### Step 13: Call df1.corrwith()

```python
df1.corrwith(df2, axis=1)
```

### Step 14: Call df1.corrwith()

```python
df1.corrwith(df2)
```

### Step 15: Call df1.corrwith()

```python
df1.corrwith(df2)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df1 = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
df2 = df1.copy()
cols = ['A', 'B', 'C', 'D']
df1['obj'] = 'foo'
df2['obj'] = 'bar'
if using_infer_string:
    msg = "Cannot perform reduction 'mean' with string dtype"
    with pytest.raises(TypeError, match=msg):
        df1.corrwith(df2)
else:
    with pytest.raises(TypeError, match='Could not convert'):
        df1.corrwith(df2)
result = df1.corrwith(df2, numeric_only=True)
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols])
tm.assert_series_equal(result, expected)
with pytest.raises(TypeError, match='unsupported operand type'):
    df1.corrwith(df2, axis=1)
result = df1.corrwith(df2, axis=1, numeric_only=True)
expected = df1.loc[:, cols].corrwith(df2.loc[:, cols], axis=1)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cov_corr.py:329 | Complexity: Advanced | Last updated: 2026-06-02*