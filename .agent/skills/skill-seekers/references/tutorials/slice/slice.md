# How To: Slice

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: string_series, object_series, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign original = string_series.copy(...)

```python
original = string_series.copy()
```

**Verification:**
```python
assert string_series.index[9] not in numSlice.index
```

### Step 2: Assign numSlice = value

```python
numSlice = string_series[10:20]
```

**Verification:**
```python
assert object_series.index[9] not in objSlice.index
```

### Step 3: Assign numSliceEnd = value

```python
numSliceEnd = string_series[-10:]
```

**Verification:**
```python
assert len(numSlice) == len(numSlice.index)
```

### Step 4: Assign objSlice = value

```python
objSlice = object_series[10:20]
```

**Verification:**
```python
assert string_series[numSlice.index[0]] == numSlice[numSlice.index[0]]
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(numSliceEnd), np.array(string_series)[-10:])
```

**Verification:**
```python
assert numSlice.index[1] == string_series.index[11]
```

### Step 6: Assign sl = value

```python
sl = string_series[10:20]
```

**Verification:**
```python
assert (string_series[10:20] == 0).all()
```

### Step 7: Assign unknown = 0

```python
sl[:] = 0
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(string_series, original)
```

**Verification:**
```python
assert (string_series[10:20] == 0).all()
```


## Complete Example

```python
# Setup
# Fixtures: string_series, object_series, using_copy_on_write, warn_copy_on_write

# Workflow
original = string_series.copy()
numSlice = string_series[10:20]
numSliceEnd = string_series[-10:]
objSlice = object_series[10:20]
assert string_series.index[9] not in numSlice.index
assert object_series.index[9] not in objSlice.index
assert len(numSlice) == len(numSlice.index)
assert string_series[numSlice.index[0]] == numSlice[numSlice.index[0]]
assert numSlice.index[1] == string_series.index[11]
tm.assert_numpy_array_equal(np.array(numSliceEnd), np.array(string_series)[-10:])
sl = string_series[10:20]
with tm.assert_cow_warning(warn_copy_on_write):
    sl[:] = 0
if using_copy_on_write:
    tm.assert_series_equal(string_series, original)
else:
    assert (string_series[10:20] == 0).all()
```

## Next Steps


---

*Source: test_indexing.py:245 | Complexity: Advanced | Last updated: 2026-06-02*