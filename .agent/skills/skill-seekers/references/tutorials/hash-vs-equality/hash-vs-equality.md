# How To: Hash Vs Equality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hash vs equality

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype2 = IntervalDtype(...)

```python
dtype2 = IntervalDtype('int64', 'right')
```

**Verification:**
```python
assert dtype == dtype2
```

### Step 2: Assign dtype3 = IntervalDtype(...)

```python
dtype3 = IntervalDtype(dtype2)
```

**Verification:**
```python
assert dtype2 == dtype
```

### Step 3: Assign dtype1 = IntervalDtype(...)

```python
dtype1 = IntervalDtype('interval')
```

**Verification:**
```python
assert dtype3 == dtype
```

### Step 4: Assign dtype2 = IntervalDtype(...)

```python
dtype2 = IntervalDtype(dtype1)
```

**Verification:**
```python
assert dtype is not dtype2
```

### Step 5: Assign dtype3 = IntervalDtype(...)

```python
dtype3 = IntervalDtype('interval')
```

**Verification:**
```python
assert dtype2 is not dtype3
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
dtype2 = IntervalDtype('int64', 'right')
dtype3 = IntervalDtype(dtype2)
assert dtype == dtype2
assert dtype2 == dtype
assert dtype3 == dtype
assert dtype is not dtype2
assert dtype2 is not dtype3
assert dtype3 is not dtype
assert hash(dtype) == hash(dtype2)
assert hash(dtype) == hash(dtype3)
dtype1 = IntervalDtype('interval')
dtype2 = IntervalDtype(dtype1)
dtype3 = IntervalDtype('interval')
assert dtype2 == dtype1
assert dtype2 == dtype2
assert dtype2 == dtype3
assert dtype2 is not dtype1
assert dtype2 is dtype2
assert dtype2 is not dtype3
assert hash(dtype2) == hash(dtype1)
assert hash(dtype2) == hash(dtype2)
assert hash(dtype2) == hash(dtype3)
```

## Next Steps


---

*Source: test_dtypes.py:589 | Complexity: Intermediate | Last updated: 2026-06-02*