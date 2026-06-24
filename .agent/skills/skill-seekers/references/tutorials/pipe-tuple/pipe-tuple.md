# How To: Pipe Tuple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pipe tuple

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

### Step 4: Assign result = obj.pipe(...)

```python
result = obj.pipe((f, 'y'), 0)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, obj)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = DataFrame({'A': [1, 2, 3]})
obj = tm.get_obj(obj, frame_or_series)
f = lambda x, y: y
result = obj.pipe((f, 'y'), 0)
tm.assert_equal(result, obj)
```

## Next Steps


---

*Source: test_pipe.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*