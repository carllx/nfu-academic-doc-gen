# How To: First Last Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test first last raises

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
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = DataFrame(...)

```python
obj = DataFrame([[1, 2, 3], [4, 5, 6]])
```

### Step 2: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 3: Assign msg = "'first' only supports a DatetimeIndex index"

```python
msg = "'first' only supports a DatetimeIndex index"
```

### Step 4: Assign msg = "'last' only supports a DatetimeIndex index"

```python
msg = "'last' only supports a DatetimeIndex index"
```

### Step 5: Call obj.first()

```python
obj.first('1D')
```

### Step 6: Call obj.last()

```python
obj.last('1D')
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = DataFrame([[1, 2, 3], [4, 5, 6]])
obj = tm.get_obj(obj, frame_or_series)
msg = "'first' only supports a DatetimeIndex index"
with tm.assert_produces_warning(FutureWarning, match=deprecated_msg), pytest.raises(TypeError, match=msg):
    obj.first('1D')
msg = "'last' only supports a DatetimeIndex index"
with tm.assert_produces_warning(FutureWarning, match=last_deprecated_msg), pytest.raises(TypeError, match=msg):
    obj.last('1D')
```

## Next Steps


---

*Source: test_first_and_last.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*