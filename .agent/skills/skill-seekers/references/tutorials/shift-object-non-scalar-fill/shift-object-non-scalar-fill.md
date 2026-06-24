# How To: Shift Object Non Scalar Fill

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift object non scalar fill

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(3))
```

**Verification:**
```python
assert result[0] == {}
```

### Step 2: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

**Verification:**
```python
assert result.iloc[0, 0] == {}
```

### Step 3: Assign obj_ser = ser.astype(...)

```python
obj_ser = ser.astype(object)
```

### Step 4: Assign result = obj_ser.shift(...)

```python
result = obj_ser.shift(1, fill_value={})
```

**Verification:**
```python
assert result[0] == {}
```

### Step 5: Assign obj_df = obj_ser.to_frame(...)

```python
obj_df = obj_ser.to_frame()
```

### Step 6: Assign result = obj_df.shift(...)

```python
result = obj_df.shift(1, fill_value={})
```

**Verification:**
```python
assert result.iloc[0, 0] == {}
```

### Step 7: Call ser.shift()

```python
ser.shift(1, fill_value=[])
```

### Step 8: Call df.shift()

```python
df.shift(1, fill_value=np.arange(3))
```


## Complete Example

```python
# Workflow
ser = Series(range(3))
with pytest.raises(ValueError, match='fill_value must be a scalar'):
    ser.shift(1, fill_value=[])
df = ser.to_frame()
with pytest.raises(ValueError, match='fill_value must be a scalar'):
    df.shift(1, fill_value=np.arange(3))
obj_ser = ser.astype(object)
result = obj_ser.shift(1, fill_value={})
assert result[0] == {}
obj_df = obj_ser.to_frame()
result = obj_df.shift(1, fill_value={})
assert result.iloc[0, 0] == {}
```

## Next Steps


---

*Source: test_shift.py:106 | Complexity: Advanced | Last updated: 2026-06-02*