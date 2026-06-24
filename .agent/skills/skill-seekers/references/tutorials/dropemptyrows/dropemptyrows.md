# How To: Dropemptyrows

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropEmptyRows

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
assert return_value is None
```

### Step 3: Assign unknown = value

```python
mat[:5] = np.nan
```

### Step 4: Assign frame = DataFrame(...)

```python
frame = DataFrame({'foo': mat}, index=float_frame.index)
```

### Step 5: Assign original = Series(...)

```python
original = Series(mat, index=float_frame.index, name='foo')
```

### Step 6: Assign expected = original.dropna(...)

```python
expected = original.dropna()
```

### Step 7: Assign unknown = value

```python
inplace_frame1, inplace_frame2 = (frame.copy(), frame.copy())
```

### Step 8: Assign smaller_frame = frame.dropna(...)

```python
smaller_frame = frame.dropna(how='all')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(frame['foo'], original)
```

### Step 10: Assign return_value = inplace_frame1.dropna(...)

```python
return_value = inplace_frame1.dropna(how='all', inplace=True)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(smaller_frame['foo'], expected)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(inplace_frame1['foo'], expected)
```

**Verification:**
```python
assert return_value is None
```

### Step 13: Assign smaller_frame = frame.dropna(...)

```python
smaller_frame = frame.dropna(how='all', subset=['foo'])
```

### Step 14: Assign return_value = inplace_frame2.dropna(...)

```python
return_value = inplace_frame2.dropna(how='all', subset=['foo'], inplace=True)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(smaller_frame['foo'], expected)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(inplace_frame2['foo'], expected)
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
original = Series(mat, index=float_frame.index, name='foo')
expected = original.dropna()
inplace_frame1, inplace_frame2 = (frame.copy(), frame.copy())
smaller_frame = frame.dropna(how='all')
tm.assert_series_equal(frame['foo'], original)
return_value = inplace_frame1.dropna(how='all', inplace=True)
tm.assert_series_equal(smaller_frame['foo'], expected)
tm.assert_series_equal(inplace_frame1['foo'], expected)
assert return_value is None
smaller_frame = frame.dropna(how='all', subset=['foo'])
return_value = inplace_frame2.dropna(how='all', subset=['foo'], inplace=True)
tm.assert_series_equal(smaller_frame['foo'], expected)
tm.assert_series_equal(inplace_frame2['foo'], expected)
assert return_value is None
```

## Next Steps


---

*Source: test_dropna.py:16 | Complexity: Advanced | Last updated: 2026-06-02*