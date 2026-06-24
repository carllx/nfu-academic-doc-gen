# How To: Apply Box Period

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply box period

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`


## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = [pd.Period('2011-01-01', freq='M'), pd.Period('2011-01-02', freq='M')]
```

**Verification:**
```python
assert ser.dtype == 'Period[M]'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(vals)
```

**Verification:**
```python
assert ser.dtype == 'Period[M]'
```

### Step 3: Assign res = ser.apply(...)

```python
res = ser.apply(lambda x: f'{type(x).__name__}_{x.freqstr}', by_row='compat')
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(['Period_M', 'Period_M'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
vals = [pd.Period('2011-01-01', freq='M'), pd.Period('2011-01-02', freq='M')]
ser = Series(vals)
assert ser.dtype == 'Period[M]'
res = ser.apply(lambda x: f'{type(x).__name__}_{x.freqstr}', by_row='compat')
exp = Series(['Period_M', 'Period_M'])
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_series_apply.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*