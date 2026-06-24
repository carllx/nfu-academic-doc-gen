# How To: Maybe Cast Slice Bound

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe cast slice bound

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: make_range, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign idx = make_range(...)

```python
idx = make_range(start='2013/10/01', freq='D', periods=10)
```

### Step 2: Assign obj = DataFrame(...)

```python
obj = DataFrame({'units': [100 + i for i in range(10)]}, index=idx)
```

### Step 3: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 4: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(idx).__name__} with these indexers \\[foo\\] of type str'
```

### Step 5: Call idx._maybe_cast_slice_bound()

```python
idx._maybe_cast_slice_bound('foo', 'left')
```

### Step 6: Call idx.get_slice_bound()

```python
idx.get_slice_bound('foo', 'left')
```

### Step 7: obj['2013/09/30':'foo']

```python
obj['2013/09/30':'foo']
```

### Step 8: obj['foo':'2013/09/30']

```python
obj['foo':'2013/09/30']
```

### Step 9: obj.loc['2013/09/30':'foo']

```python
obj.loc['2013/09/30':'foo']
```

### Step 10: obj.loc['foo':'2013/09/30']

```python
obj.loc['foo':'2013/09/30']
```


## Complete Example

```python
# Setup
# Fixtures: make_range, frame_or_series

# Workflow
idx = make_range(start='2013/10/01', freq='D', periods=10)
obj = DataFrame({'units': [100 + i for i in range(10)]}, index=idx)
obj = tm.get_obj(obj, frame_or_series)
msg = f'cannot do slice indexing on {type(idx).__name__} with these indexers \\[foo\\] of type str'
with pytest.raises(TypeError, match=msg):
    idx._maybe_cast_slice_bound('foo', 'left')
with pytest.raises(TypeError, match=msg):
    idx.get_slice_bound('foo', 'left')
with pytest.raises(TypeError, match=msg):
    obj['2013/09/30':'foo']
with pytest.raises(TypeError, match=msg):
    obj['foo':'2013/09/30']
with pytest.raises(TypeError, match=msg):
    obj.loc['2013/09/30':'foo']
with pytest.raises(TypeError, match=msg):
    obj.loc['foo':'2013/09/30']
```

## Next Steps


---

*Source: test_partial_slicing.py:132 | Complexity: Advanced | Last updated: 2026-06-02*