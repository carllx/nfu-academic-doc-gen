# How To: Agg Cython Table Raises Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test agg cython table raises series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series, func, expected, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign msg = "[Cc]ould not convert|can't multiply sequence by non-int of type"

```python
msg = "[Cc]ould not convert|can't multiply sequence by non-int of type"
```

### Step 2: Assign msg = value

```python
msg = msg + '|does not support|has no kernel|Cannot perform|cannot perform|operation'
```

### Step 3: Assign warn = value

```python
warn = None if isinstance(func, str) else FutureWarning
```

### Step 4: Assign msg = "Cannot convert \\['a' 'b' 'c'\\] to numeric"

```python
msg = "Cannot convert \\['a' 'b' 'c'\\] to numeric"
```

### Step 5: Assign expected = value

```python
expected = (expected, NotImplementedError)
```

### Step 6: Call series.agg()

```python
series.agg(func)
```


## Complete Example

```python
# Setup
# Fixtures: series, func, expected, using_infer_string

# Workflow
msg = "[Cc]ould not convert|can't multiply sequence by non-int of type"
if func == 'median' or func is np.nanmedian or func is np.median:
    msg = "Cannot convert \\['a' 'b' 'c'\\] to numeric"
if using_infer_string and func in ('cumprod', np.cumprod, np.nancumprod):
    expected = (expected, NotImplementedError)
msg = msg + '|does not support|has no kernel|Cannot perform|cannot perform|operation'
warn = None if isinstance(func, str) else FutureWarning
with pytest.raises(expected, match=msg):
    with tm.assert_produces_warning(warn, match='is currently using Series.*'):
        series.agg(func)
```

## Next Steps


---

*Source: test_invalid_arg.py:250 | Complexity: Intermediate | Last updated: 2026-06-02*