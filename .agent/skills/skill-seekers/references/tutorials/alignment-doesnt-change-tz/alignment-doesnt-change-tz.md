# How To: Alignment Doesnt Change Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test alignment doesnt change tz

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=10, tz='CET')
```

**Verification:**
```python
assert ser.index is dti
```

### Step 2: Assign dti_utc = dti.tz_convert(...)

```python
dti_utc = dti.tz_convert('UTC')
```

**Verification:**
```python
assert ser_utc.index is dti_utc
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(10, index=dti)
```

### Step 4: Assign ser_utc = Series(...)

```python
ser_utc = Series(10, index=dti_utc)
```

### Step 5: ser * ser_utc

```python
ser * ser_utc
```

**Verification:**
```python
assert ser.index is dti
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=10, tz='CET')
dti_utc = dti.tz_convert('UTC')
ser = Series(10, index=dti)
ser_utc = Series(10, index=dti_utc)
ser * ser_utc
assert ser.index is dti
assert ser_utc.index is dti_utc
```

## Next Steps


---

*Source: test_arithmetic.py:279 | Complexity: Intermediate | Last updated: 2026-06-02*