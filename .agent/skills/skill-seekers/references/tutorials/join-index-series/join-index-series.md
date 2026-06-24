# How To: Join Index Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join index series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign df = float_frame.copy(...)

```python
df = float_frame.copy()
```

### Step 2: Assign ser = df.pop(...)

```python
ser = df.pop(float_frame.columns[-1])
```

### Step 3: Assign joined = df.join(...)

```python
joined = df.join(ser)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, float_frame)
```

### Step 5: Assign ser.name = None

```python
ser.name = None
```

### Step 6: Call df.join()

```python
df.join(ser)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
df = float_frame.copy()
ser = df.pop(float_frame.columns[-1])
joined = df.join(ser)
tm.assert_frame_equal(joined, float_frame)
ser.name = None
with pytest.raises(ValueError, match='must have a name'):
    df.join(ser)
```

## Next Steps


---

*Source: test_join.py:323 | Complexity: Intermediate | Last updated: 2026-06-02*