# How To: Transpose Object To Tzaware Mixed Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transpose object to tzaware mixed tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-04-05 04:30', periods=3, tz='UTC')
```

**Verification:**
```python
assert (df2.dtypes == object).all()
```

### Step 2: Assign dti2 = dti.tz_convert(...)

```python
dti2 = dti.tz_convert('US/Pacific')
```

**Verification:**
```python
assert (res2.dtypes == object).all()
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([dti, dti2])
```

**Verification:**
```python
assert (df2.dtypes == object).all()
```

### Step 4: Assign res2 = value

```python
res2 = df2.T
```

**Verification:**
```python
assert (res2.dtypes == object).all()
```


## Complete Example

```python
# Workflow
dti = date_range('2016-04-05 04:30', periods=3, tz='UTC')
dti2 = dti.tz_convert('US/Pacific')
df2 = DataFrame([dti, dti2])
assert (df2.dtypes == object).all()
res2 = df2.T
assert (res2.dtypes == object).all()
```

## Next Steps


---

*Source: test_transpose.py:83 | Complexity: Intermediate | Last updated: 2026-06-02*