# How To: Pipe Tuple Error

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pipe tuple error

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = DataFrame(...)

```python
obj = DataFrame({'A': [1, 2, 3]})
```

### Step 2: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 3: Assign f = value

```python
f = lambda x, y: y
```

### Step 4: Assign msg = 'y is both the pipe target and a keyword argument'

```python
msg = 'y is both the pipe target and a keyword argument'
```

### Step 5: Call obj.pipe()

```python
obj.pipe((f, 'y'), x=1, y=0)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = DataFrame({'A': [1, 2, 3]})
obj = tm.get_obj(obj, frame_or_series)
f = lambda x, y: y
msg = 'y is both the pipe target and a keyword argument'
with pytest.raises(ValueError, match=msg):
    obj.pipe((f, 'y'), x=1, y=0)
```

## Next Steps


---

*Source: test_pipe.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*