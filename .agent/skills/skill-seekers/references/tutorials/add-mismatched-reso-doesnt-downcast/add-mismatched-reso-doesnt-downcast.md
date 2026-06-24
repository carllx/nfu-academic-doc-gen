# How To: Add Mismatched Reso Doesnt Downcast

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add mismatched reso doesnt downcast

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign td = pd.Timedelta(...)

```python
td = pd.Timedelta(microseconds=1)
```

**Verification:**
```python
assert res.unit == 'us'
```

### Step 2: Assign dti = value

```python
dti = pd.date_range('2016-01-01', periods=3) - td
```

### Step 3: Assign dta = dti._data.as_unit(...)

```python
dta = dti._data.as_unit('us')
```

### Step 4: Assign res = value

```python
res = dta + td.as_unit('us')
```

**Verification:**
```python
assert res.unit == 'us'
```


## Complete Example

```python
# Workflow
td = pd.Timedelta(microseconds=1)
dti = pd.date_range('2016-01-01', periods=3) - td
dta = dti._data.as_unit('us')
res = dta + td.as_unit('us')
assert res.unit == 'us'
```

## Next Steps


---

*Source: test_datetimes.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*