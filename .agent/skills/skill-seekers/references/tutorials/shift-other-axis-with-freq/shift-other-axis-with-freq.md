# How To: Shift Other Axis With Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift other axis with freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign obj = value

```python
obj = datetime_frame.T
```

**Verification:**
```python
assert len(shifted) == len(obj)
```

### Step 2: Assign offset = offsets.BDay(...)

```python
offset = offsets.BDay()
```

### Step 3: Assign shifted = obj.shift(...)

```python
shifted = obj.shift(5, freq=offset, axis=1)
```

**Verification:**
```python
assert len(shifted) == len(obj)
```

### Step 4: Assign unshifted = shifted.shift(...)

```python
unshifted = shifted.shift(-5, freq=offset, axis=1)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(unshifted, obj)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame

# Workflow
obj = datetime_frame.T
offset = offsets.BDay()
shifted = obj.shift(5, freq=offset, axis=1)
assert len(shifted) == len(obj)
unshifted = shifted.shift(-5, freq=offset, axis=1)
tm.assert_equal(unshifted, obj)
```

## Next Steps


---

*Source: test_shift.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*