# How To: Dropincompleterows

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropIncompleteRows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign N = len(...)

```python
N = len(float_frame.index)
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign mat = np.random.default_rng.standard_normal(...)

```python
mat = np.random.default_rng(2).standard_normal(N)
```

**Verification:**
```python
assert (frame['bar'] == 5).all()
```

### Step 3: Assign unknown = value

```python
mat[:5] = np.nan
```

**Verification:**
```python
assert return_value is None
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame({'foo': mat}, index=float_frame.index)
```

### Step 5: Assign unknown = 5

```python
frame['bar'] = 5
```

### Step 6: Assign original = Series(...)

```python
original = Series(mat, index=float_frame.index, name='foo')
```

### Step 7: Assign unknown = value

```python
inp_frame1, inp_frame2 = (frame.copy(), frame.copy())
```

### Step 8: Assign smaller_frame = frame.dropna(...)

```python
smaller_frame = frame.dropna()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(frame['foo'], original)
```

### Step 10: Assign return_value = inp_frame1.dropna(...)

```python
return_value = inp_frame1.dropna(inplace=True)
```

### Step 11: Assign exp = Series(...)

```python
exp = Series(mat[5:], index=float_frame.index[5:], name='foo')
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(smaller_frame['foo'], exp)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(inp_frame1['foo'], exp)
```

**Verification:**
```python
assert return_value is None
```

### Step 14: Assign samesize_frame = frame.dropna(...)

```python
samesize_frame = frame.dropna(subset=['bar'])
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(frame['foo'], original)
```

**Verification:**
```python
assert (frame['bar'] == 5).all()
```

### Step 16: Assign return_value = inp_frame2.dropna(...)

```python
return_value = inp_frame2.dropna(subset=['bar'], inplace=True)
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(samesize_frame.index, float_frame.index)
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inp_frame2.index, float_frame.index)
```

**Verification:**
```python
assert return_value is None
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
N = len(float_frame.index)
mat = np.random.default_rng(2).standard_normal(N)
mat[:5] = np.nan
frame = DataFrame({'foo': mat}, index=float_frame.index)
frame['bar'] = 5
original = Series(mat, index=float_frame.index, name='foo')
inp_frame1, inp_frame2 = (frame.copy(), frame.copy())
smaller_frame = frame.dropna()
tm.assert_series_equal(frame['foo'], original)
return_value = inp_frame1.dropna(inplace=True)
exp = Series(mat[5:], index=float_frame.index[5:], name='foo')
tm.assert_series_equal(smaller_frame['foo'], exp)
tm.assert_series_equal(inp_frame1['foo'], exp)
assert return_value is None
samesize_frame = frame.dropna(subset=['bar'])
tm.assert_series_equal(frame['foo'], original)
assert (frame['bar'] == 5).all()
return_value = inp_frame2.dropna(subset=['bar'], inplace=True)
tm.assert_index_equal(samesize_frame.index, float_frame.index)
tm.assert_index_equal(inp_frame2.index, float_frame.index)
assert return_value is None
```

## Next Steps


---

*Source: test_dropna.py:40 | Complexity: Advanced | Last updated: 2026-06-02*