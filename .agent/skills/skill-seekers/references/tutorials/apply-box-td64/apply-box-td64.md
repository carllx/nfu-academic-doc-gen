# How To: Apply Box Td64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply box td64

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
vals = [pd.Timedelta('1 days'), pd.Timedelta('2 days')]
```

**Verification:**
```python
assert ser.dtype == 'timedelta64[ns]'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(vals)
```

**Verification:**
```python
assert ser.dtype == 'timedelta64[ns]'
```

### Step 3: Assign res = ser.apply(...)

```python
res = ser.apply(lambda x: f'{type(x).__name__}_{x.days}', by_row='compat')
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(['Timedelta_1', 'Timedelta_2'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
vals = [pd.Timedelta('1 days'), pd.Timedelta('2 days')]
ser = Series(vals)
assert ser.dtype == 'timedelta64[ns]'
res = ser.apply(lambda x: f'{type(x).__name__}_{x.days}', by_row='compat')
exp = Series(['Timedelta_1', 'Timedelta_2'])
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_series_apply.py:177 | Complexity: Intermediate | Last updated: 2026-06-02*