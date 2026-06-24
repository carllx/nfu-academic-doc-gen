# How To: Mean With Convertible String Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mean with convertible string raises

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
# Fixtures: using_array_manager, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['1', '2'])
```

**Verification:**
```python
assert ser.sum() == '12'
```

### Step 2: Assign msg = "Could not convert string '12' to numeric|does not support|Cannot perform"

```python
msg = "Could not convert string '12' to numeric|does not support|Cannot perform"
```

### Step 3: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 4: Call ser.mean()

```python
ser.mean()
```

### Step 5: Assign msg = "Could not convert \\['12'\\] to numeric|does not support|Cannot perform"

```python
msg = "Could not convert \\['12'\\] to numeric|does not support|Cannot perform"
```

### Step 6: Call df.mean()

```python
df.mean()
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager, using_infer_string

# Workflow
ser = Series(['1', '2'])
assert ser.sum() == '12'
msg = "Could not convert string '12' to numeric|does not support|Cannot perform"
with pytest.raises(TypeError, match=msg):
    ser.mean()
df = ser.to_frame()
if not using_array_manager:
    msg = "Could not convert \\['12'\\] to numeric|does not support|Cannot perform"
with pytest.raises(TypeError, match=msg):
    df.mean()
```

## Next Steps


---

*Source: test_reductions.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*