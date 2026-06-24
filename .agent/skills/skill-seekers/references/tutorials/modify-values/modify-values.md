# How To: Modify Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test modify values

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
# Fixtures: float_frame, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign unknown = 5

```python
float_frame.values[5] = 5
```

**Verification:**
```python
assert (float_frame.values[5] != 5).all()
```

### Step 2: Assign unknown = 7.0

```python
float_frame['E'] = 7.0
```

**Verification:**
```python
assert (float_frame.values[5] == 5).all()
```

### Step 3: Assign col = value

```python
col = float_frame['E']
```

**Verification:**
```python
assert not (float_frame.values[6] == 6).all()
```

### Step 4: Assign unknown = 6

```python
float_frame.values[6] = 6
```

**Verification:**
```python
assert (col == 7).all()
```

### Step 5: Assign unknown = 5

```python
float_frame.values[5] = 5
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, using_copy_on_write

# Workflow
if using_copy_on_write:
    with pytest.raises(ValueError, match='read-only'):
        float_frame.values[5] = 5
    assert (float_frame.values[5] != 5).all()
    return
float_frame.values[5] = 5
assert (float_frame.values[5] == 5).all()
float_frame['E'] = 7.0
col = float_frame['E']
float_frame.values[6] = 6
assert not (float_frame.values[6] == 6).all()
assert (col == 7).all()
```

## Next Steps


---

*Source: test_block_internals.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*