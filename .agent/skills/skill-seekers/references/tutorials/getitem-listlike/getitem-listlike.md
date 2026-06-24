# How To: Getitem Listlike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem listlike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: idx_type, levels, float_frame
```

## Step-by-Step Guide

### Step 1: Assign keys = value

```python
keys = [frame.columns[1], frame.columns[0]]
```

### Step 2: Assign idx = idx_type(...)

```python
idx = idx_type(keys)
```

### Step 3: Assign idx_check = list(...)

```python
idx_check = list(idx_type(keys))
```

### Step 4: Assign expected = value

```python
expected = frame.loc[:, idx_check]
```

### Step 5: Assign expected.columns.names = value

```python
expected.columns.names = frame.columns.names
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign idx = idx_type(...)

```python
idx = idx_type(keys + [missing])
```

### Step 8: Assign unknown = value

```python
frame, missing = (float_frame, 'food')
```

### Step 9: Assign frame = DataFrame(...)

```python
frame = DataFrame(np.random.default_rng(2).standard_normal((8, 3)), columns=Index([('foo', 'bar'), ('baz', 'qux'), ('peek', 'aboo')], name=('sth', 'sth2')))
```

### Step 10: Assign missing = value

```python
missing = ('good', 'food')
```

### Step 11: Assign result = value

```python
result = frame[idx]
```

### Step 12: frame[idx]

```python
frame[idx]
```

### Step 13: frame[idx]

```python
frame[idx]
```


## Complete Example

```python
# Setup
# Fixtures: idx_type, levels, float_frame

# Workflow
if levels == 1:
    frame, missing = (float_frame, 'food')
else:
    frame = DataFrame(np.random.default_rng(2).standard_normal((8, 3)), columns=Index([('foo', 'bar'), ('baz', 'qux'), ('peek', 'aboo')], name=('sth', 'sth2')))
    missing = ('good', 'food')
keys = [frame.columns[1], frame.columns[0]]
idx = idx_type(keys)
idx_check = list(idx_type(keys))
if isinstance(idx, (set, dict)):
    with pytest.raises(TypeError, match='as an indexer is not supported'):
        frame[idx]
    return
else:
    result = frame[idx]
expected = frame.loc[:, idx_check]
expected.columns.names = frame.columns.names
tm.assert_frame_equal(result, expected)
idx = idx_type(keys + [missing])
with pytest.raises(KeyError, match='not in index'):
    frame[idx]
```

## Next Steps


---

*Source: test_getitem.py:123 | Complexity: Advanced | Last updated: 2026-06-02*