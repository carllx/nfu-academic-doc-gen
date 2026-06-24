# How To: Median With Convertible String Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test median with convertible string raises

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
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign msg = "Cannot convert \\['1' '2' '3'\\] to numeric|does not support|Cannot perform"

```python
msg = "Cannot convert \\['1' '2' '3'\\] to numeric|does not support|Cannot perform"
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(['1', '2', '3'])
```

### Step 3: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 4: Call ser.median()

```python
ser.median()
```

### Step 5: Assign msg = "Cannot convert \\[\\['1' '2' '3'\\]\\] to numeric|does not support|Cannot perform"

```python
msg = "Cannot convert \\[\\['1' '2' '3'\\]\\] to numeric|does not support|Cannot perform"
```

### Step 6: Call df.median()

```python
df.median()
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
msg = "Cannot convert \\['1' '2' '3'\\] to numeric|does not support|Cannot perform"
ser = Series(['1', '2', '3'])
with pytest.raises(TypeError, match=msg):
    ser.median()
if not using_array_manager:
    msg = "Cannot convert \\[\\['1' '2' '3'\\]\\] to numeric|does not support|Cannot perform"
df = ser.to_frame()
with pytest.raises(TypeError, match=msg):
    df.median()
```

## Next Steps


---

*Source: test_reductions.py:203 | Complexity: Intermediate | Last updated: 2026-06-02*