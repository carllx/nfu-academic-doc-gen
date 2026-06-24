# How To: Select Dtypes Not An Attr But Still Valid Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes not an attr but still valid dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
```

**Verification:**
```python
assert not hasattr(np, 'u8')
```

### Step 2: Assign unknown = df.f.diff(...)

```python
df['g'] = df.f.diff()
```

**Verification:**
```python
assert not hasattr(np, 'u8')
```

### Step 3: Assign r = df.select_dtypes(...)

```python
r = df.select_dtypes(include=['i8', 'O'], exclude=['timedelta'])
```

### Step 4: Assign e = value

```python
e = df[['a', 'b']]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(r, e)
```

### Step 6: Assign r = df.select_dtypes(...)

```python
r = df.select_dtypes(include=['i8', 'O', 'timedelta64[ns]'])
```

### Step 7: Assign e = value

```python
e = df[['a', 'b', 'g']]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(r, e)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df = DataFrame({'a': list('abc'), 'b': list(range(1, 4)), 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
df['g'] = df.f.diff()
assert not hasattr(np, 'u8')
r = df.select_dtypes(include=['i8', 'O'], exclude=['timedelta'])
e = df[['a', 'b']]
tm.assert_frame_equal(r, e)
r = df.select_dtypes(include=['i8', 'O', 'timedelta64[ns]'])
e = df[['a', 'b', 'g']]
tm.assert_frame_equal(r, e)
```

## Next Steps


---

*Source: test_select_dtypes.py:302 | Complexity: Advanced | Last updated: 2026-06-02*