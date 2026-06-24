# How To: Tz Standardize

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz standardize

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign tz = pytz.timezone(...)

```python
tz = pytz.timezone('US/Eastern')
```

**Verification:**
```python
assert dtype.tz == tz
```

### Step 2: Assign dr = date_range(...)

```python
dr = date_range('2013-01-01', periods=3, tz='US/Eastern')
```

**Verification:**
```python
assert dtype.tz == tz
```

### Step 3: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype('ns', dr.tz)
```

**Verification:**
```python
assert dtype.tz == tz
```

### Step 4: Assign dtype = DatetimeTZDtype(...)

```python
dtype = DatetimeTZDtype('ns', dr[0].tz)
```

**Verification:**
```python
assert dtype.tz == tz
```


## Complete Example

```python
# Workflow
tz = pytz.timezone('US/Eastern')
dr = date_range('2013-01-01', periods=3, tz='US/Eastern')
dtype = DatetimeTZDtype('ns', dr.tz)
assert dtype.tz == tz
dtype = DatetimeTZDtype('ns', dr[0].tz)
assert dtype.tz == tz
```

## Next Steps


---

*Source: test_dtypes.py:392 | Complexity: Intermediate | Last updated: 2026-06-02*