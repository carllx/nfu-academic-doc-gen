# How To: Insert Out Of Bounds

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert out of bounds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `weakref`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: index, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign msg = unknown.join(...)

```python
msg = '|'.join(['index -?\\d+ is out of bounds for axis 0 with size \\d+', 'loc must be an integer between'])
```

### Step 2: Assign err = TypeError

```python
err = TypeError
```

### Step 3: Assign err = IndexError

```python
err = IndexError
```

### Step 4: Assign msg = 'index (0|0.5) is out of bounds for axis 0 with size 0'

```python
msg = 'index (0|0.5) is out of bounds for axis 0 with size 0'
```

### Step 5: Assign msg = 'slice indices must be integers or None or have an __index__ method'

```python
msg = 'slice indices must be integers or None or have an __index__ method'
```

### Step 6: Call index.insert()

```python
index.insert(0.5, 'foo')
```

### Step 7: Call index.insert()

```python
index.insert(len(index) + 1, 1)
```

### Step 8: Call index.insert()

```python
index.insert(-len(index) - 1, 1)
```

### Step 9: Assign msg = 'loc must be an integer between'

```python
msg = 'loc must be an integer between'
```

### Step 10: Assign msg = 'loc must be an integer between'

```python
msg = 'loc must be an integer between'
```

### Step 11: Assign err = TypeError

```python
err = TypeError
```


## Complete Example

```python
# Setup
# Fixtures: index, using_infer_string

# Workflow
if len(index) > 0:
    err = TypeError
else:
    err = IndexError
if len(index) == 0:
    msg = 'index (0|0.5) is out of bounds for axis 0 with size 0'
else:
    msg = 'slice indices must be integers or None or have an __index__ method'
if using_infer_string:
    if index.dtype == 'string' or index.dtype == 'category':
        msg = 'loc must be an integer between'
    elif index.dtype == 'object' and len(index) == 0:
        msg = 'loc must be an integer between'
        err = TypeError
with pytest.raises(err, match=msg):
    index.insert(0.5, 'foo')
msg = '|'.join(['index -?\\d+ is out of bounds for axis 0 with size \\d+', 'loc must be an integer between'])
with pytest.raises(IndexError, match=msg):
    index.insert(len(index) + 1, 1)
with pytest.raises(IndexError, match=msg):
    index.insert(-len(index) - 1, 1)
```

## Next Steps


---

*Source: test_old_base.py:432 | Complexity: Advanced | Last updated: 2026-06-02*