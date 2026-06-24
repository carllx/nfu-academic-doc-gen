# How To: Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dst

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

### Step 1: Assign dr1 = date_range(...)

```python
dr1 = date_range('2013-01-01', periods=3, tz='US/Eastern')
```

**Verification:**
```python
assert isinstance(s1.dtype, DatetimeTZDtype)
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(dr1, name='A')
```

**Verification:**
```python
assert isinstance(s2.dtype, DatetimeTZDtype)
```

### Step 3: Assign dr2 = date_range(...)

```python
dr2 = date_range('2013-08-01', periods=3, tz='US/Eastern')
```

**Verification:**
```python
assert s1.dtype == s2.dtype
```

### Step 4: Assign s2 = Series(...)

```python
s2 = Series(dr2, name='A')
```

**Verification:**
```python
assert isinstance(s2.dtype, DatetimeTZDtype)
```


## Complete Example

```python
# Workflow
dr1 = date_range('2013-01-01', periods=3, tz='US/Eastern')
s1 = Series(dr1, name='A')
assert isinstance(s1.dtype, DatetimeTZDtype)
dr2 = date_range('2013-08-01', periods=3, tz='US/Eastern')
s2 = Series(dr2, name='A')
assert isinstance(s2.dtype, DatetimeTZDtype)
assert s1.dtype == s2.dtype
```

## Next Steps


---

*Source: test_dtypes.py:369 | Complexity: Intermediate | Last updated: 2026-06-02*