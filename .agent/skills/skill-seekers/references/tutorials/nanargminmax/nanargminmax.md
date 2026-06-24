# How To: Nanargminmax

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nanargminmax

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: opname, index_or_series
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

**Verification:**
```python
assert getattr(obj, arg_op)() == 1
```

### Step 2: Assign arg_op = value

```python
arg_op = 'arg' + opname if klass is Index else 'idx' + opname
```

**Verification:**
```python
assert np.isnan(result)
```

### Step 3: Assign obj = klass(...)

```python
obj = klass([NaT, datetime(2011, 11, 1)])
```

**Verification:**
```python
assert result == -1
```

### Step 4: Assign msg = 'The behavior of (DatetimeIndex|Series).argmax/argmin with skipna=False and NAs'

```python
msg = 'The behavior of (DatetimeIndex|Series).argmax/argmin with skipna=False and NAs'
```

**Verification:**
```python
assert getattr(obj, arg_op)() == 1
```

### Step 5: Assign obj = klass(...)

```python
obj = klass([NaT, datetime(2011, 11, 1), NaT])
```

**Verification:**
```python
assert np.isnan(result)
```

### Step 6: Assign msg = 'The behavior of Series.(idxmax|idxmin) with all-NA'

```python
msg = 'The behavior of Series.(idxmax|idxmin) with all-NA'
```

**Verification:**
```python
assert result == -1
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(obj, arg_op)(skipna=False)
```

**Verification:**
```python
assert np.isnan(result)
```

### Step 8: Assign result = getattr(...)

```python
result = getattr(obj, arg_op)(skipna=False)
```

**Verification:**
```python
assert np.isnan(result)
```


## Complete Example

```python
# Setup
# Fixtures: opname, index_or_series

# Workflow
klass = index_or_series
arg_op = 'arg' + opname if klass is Index else 'idx' + opname
obj = klass([NaT, datetime(2011, 11, 1)])
assert getattr(obj, arg_op)() == 1
msg = 'The behavior of (DatetimeIndex|Series).argmax/argmin with skipna=False and NAs'
if klass is Series:
    msg = 'The behavior of Series.(idxmax|idxmin) with all-NA'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = getattr(obj, arg_op)(skipna=False)
if klass is Series:
    assert np.isnan(result)
else:
    assert result == -1
obj = klass([NaT, datetime(2011, 11, 1), NaT])
assert getattr(obj, arg_op)() == 1
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = getattr(obj, arg_op)(skipna=False)
if klass is Series:
    assert np.isnan(result)
else:
    assert result == -1
```

## Next Steps


---

*Source: test_reductions.py:123 | Complexity: Advanced | Last updated: 2026-06-02*