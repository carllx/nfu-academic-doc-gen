# How To: Objarr Add Invalid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test objarr add invalid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: op, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign obj_ser = Series(...)

```python
obj_ser = Series(list('abc'), dtype=object, name='objects')
```

### Step 3: Assign obj_ser = tm.box_expected(...)

```python
obj_ser = tm.box_expected(obj_ser, box)
```

### Step 4: Assign msg = unknown.join(...)

```python
msg = '|'.join(['can only concatenate str', 'unsupported operand type', 'must be str', 'has no kernel', "operation 'add' not supported", "operation 'radd' not supported", "operation 'sub' not supported", "operation 'rsub' not supported"])
```

### Step 5: Call op()

```python
op(obj_ser, 1)
```

### Step 6: Call op()

```python
op(obj_ser, np.array(1, dtype=np.int64))
```


## Complete Example

```python
# Setup
# Fixtures: op, box_with_array

# Workflow
box = box_with_array
obj_ser = Series(list('abc'), dtype=object, name='objects')
obj_ser = tm.box_expected(obj_ser, box)
msg = '|'.join(['can only concatenate str', 'unsupported operand type', 'must be str', 'has no kernel', "operation 'add' not supported", "operation 'radd' not supported", "operation 'sub' not supported", "operation 'rsub' not supported"])
with pytest.raises(Exception, match=msg):
    op(obj_ser, 1)
with pytest.raises(Exception, match=msg):
    op(obj_ser, np.array(1, dtype=np.int64))
```

## Next Steps


---

*Source: test_object.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*