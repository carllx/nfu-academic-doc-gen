# How To: Ops

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ops

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
# Fixtures: opname, obj
```

## Step-by-Step Guide

### Step 1: Assign result = getattr(...)

```python
result = getattr(obj, opname)()
```

**Verification:**
```python
assert result._value == expected
```

### Step 2: Assign expected = Period(...)

```python
expected = Period(ordinal=getattr(obj.asi8, opname)(), freq=obj.freq)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = expected.astype.astype(...)

```python
expected = expected.astype('M8[ns]').astype('int64')
```

**Verification:**
```python
assert result._value == expected
```

### Step 4: Assign expected = getattr(...)

```python
expected = getattr(np.array(obj.values), opname)()
```

### Step 5: Assign expected = getattr(...)

```python
expected = getattr(obj.values, opname)()
```


## Complete Example

```python
# Setup
# Fixtures: opname, obj

# Workflow
result = getattr(obj, opname)()
if not isinstance(obj, PeriodIndex):
    if isinstance(obj.values, ArrowStringArrayNumpySemantics):
        expected = getattr(np.array(obj.values), opname)()
    else:
        expected = getattr(obj.values, opname)()
else:
    expected = Period(ordinal=getattr(obj.asi8, opname)(), freq=obj.freq)
if getattr(obj, 'tz', None) is not None:
    expected = expected.astype('M8[ns]').astype('int64')
    assert result._value == expected
else:
    assert result == expected
```

## Next Steps


---

*Source: test_reductions.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*