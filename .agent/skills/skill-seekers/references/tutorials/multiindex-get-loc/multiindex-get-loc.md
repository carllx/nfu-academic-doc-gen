# How To: Multiindex Get Loc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiindex get loc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: request, lexsort_depth, keys, frame_fixture, cols
```

## Step-by-Step Guide

### Step 1: Assign frame = request.getfixturevalue(...)

```python
frame = request.getfixturevalue(frame_fixture)
```

**Verification:**
```python
assert not mi.index._lexsort_depth < lexsort_depth
```

### Step 2: Assign mi = df.set_index(...)

```python
mi = df.set_index(cols[:-1])
```

**Verification:**
```python
assert key[:i + 1] not in mi.index
```

### Step 3: Assign df = frame.copy(...)

```python
df = frame.copy(deep=False)
```

**Verification:**
```python
assert key[:i + 1] in mi.index
```

### Step 4: Assign df = frame.sort_values(...)

```python
df = frame.sort_values(by=cols[:lexsort_depth])
```

**Verification:**
```python
assert return_value is None
```

### Step 5: Assign mask = np.ones(...)

```python
mask = np.ones(len(df), dtype=bool)
```

**Verification:**
```python
assert return_value is None
```

### Step 6: Assign right = unknown.copy(...)

```python
right = df[mask].copy(deep=False)
```

**Verification:**
```python
assert return_value is None
```

### Step 7: Assign return_value = right.drop(...)

```python
return_value = right.drop(cols[:i + 1], axis=1, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 8: Assign return_value = right.set_index(...)

```python
return_value = right.set_index(cols[i + 1:-1], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(mi.loc[key[:i + 1]], right)
```

### Step 10: Assign return_value = right.set_index(...)

```python
return_value = right.set_index(cols[:-1], inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 11: Assign right = Series(...)

```python
right = Series(right['jolia'].values, name=right.index[0], index=['jolia'])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(mi.loc[key[:i + 1]], right)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(mi.loc[key[:i + 1]], right)
```


## Complete Example

```python
# Setup
# Fixtures: request, lexsort_depth, keys, frame_fixture, cols

# Workflow
frame = request.getfixturevalue(frame_fixture)
if lexsort_depth == 0:
    df = frame.copy(deep=False)
else:
    df = frame.sort_values(by=cols[:lexsort_depth])
mi = df.set_index(cols[:-1])
assert not mi.index._lexsort_depth < lexsort_depth
for key in keys:
    mask = np.ones(len(df), dtype=bool)
    for i, k in enumerate(key):
        mask &= df.iloc[:, i] == k
        if not mask.any():
            assert key[:i + 1] not in mi.index
            continue
        assert key[:i + 1] in mi.index
        right = df[mask].copy(deep=False)
        if i + 1 != len(key):
            return_value = right.drop(cols[:i + 1], axis=1, inplace=True)
            assert return_value is None
            return_value = right.set_index(cols[i + 1:-1], inplace=True)
            assert return_value is None
            tm.assert_frame_equal(mi.loc[key[:i + 1]], right)
        else:
            return_value = right.set_index(cols[:-1], inplace=True)
            assert return_value is None
            if len(right) == 1:
                right = Series(right['jolia'].values, name=right.index[0], index=['jolia'])
                tm.assert_series_equal(mi.loc[key[:i + 1]], right)
            else:
                tm.assert_frame_equal(mi.loc[key[:i + 1]], right)
```

## Next Steps


---

*Source: test_indexing_slow.py:77 | Complexity: Advanced | Last updated: 2026-06-02*