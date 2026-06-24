# How To: Cast Internals

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cast internals

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.internals.blocks`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign msg = 'Passing a BlockManager to DataFrame'

```python
msg = 'Passing a BlockManager to DataFrame'
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame(float_frame._series, dtype=int)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(float_frame._series, dtype=np.int32)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(casted, expected)
```

### Step 6: Assign casted = DataFrame(...)

```python
casted = DataFrame(float_frame._mgr, dtype=int)
```

### Step 7: Assign casted = DataFrame(...)

```python
casted = DataFrame(float_frame._mgr, dtype=np.int32)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
msg = 'Passing a BlockManager to DataFrame'
with tm.assert_produces_warning(DeprecationWarning, match=msg, check_stacklevel=False):
    casted = DataFrame(float_frame._mgr, dtype=int)
expected = DataFrame(float_frame._series, dtype=int)
tm.assert_frame_equal(casted, expected)
with tm.assert_produces_warning(DeprecationWarning, match=msg, check_stacklevel=False):
    casted = DataFrame(float_frame._mgr, dtype=np.int32)
expected = DataFrame(float_frame._series, dtype=np.int32)
tm.assert_frame_equal(casted, expected)
```

## Next Steps


---

*Source: test_block_internals.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*