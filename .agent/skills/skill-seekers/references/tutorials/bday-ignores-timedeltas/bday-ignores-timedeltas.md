# How To: Bday Ignores Timedeltas

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bday ignores timedeltas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`

**Setup Required:**
```python
# Fixtures: unit, td_unit
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2010/02/01', '2010/02/10', freq='12h', unit=unit)
```

### Step 2: Assign td = Timedelta.as_unit(...)

```python
td = Timedelta(3, unit='h').as_unit(td_unit)
```

### Step 3: Assign off = BDay(...)

```python
off = BDay(offset=td)
```

### Step 4: Assign t1 = value

```python
t1 = idx + off
```

### Step 5: Assign exp_unit = tm.get_finest_unit(...)

```python
exp_unit = tm.get_finest_unit(td.unit, idx.unit)
```

### Step 6: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex(['2010-02-02 03:00:00', '2010-02-02 15:00:00', '2010-02-03 03:00:00', '2010-02-03 15:00:00', '2010-02-04 03:00:00', '2010-02-04 15:00:00', '2010-02-05 03:00:00', '2010-02-05 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-09 03:00:00', '2010-02-09 15:00:00', '2010-02-10 03:00:00', '2010-02-10 15:00:00', '2010-02-11 03:00:00'], freq=None).as_unit(exp_unit)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(t1, expected)
```

### Step 8: Assign pointwise = DatetimeIndex.as_unit(...)

```python
pointwise = DatetimeIndex([x + off for x in idx]).as_unit(exp_unit)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pointwise, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit, td_unit

# Workflow
idx = date_range('2010/02/01', '2010/02/10', freq='12h', unit=unit)
td = Timedelta(3, unit='h').as_unit(td_unit)
off = BDay(offset=td)
t1 = idx + off
exp_unit = tm.get_finest_unit(td.unit, idx.unit)
expected = DatetimeIndex(['2010-02-02 03:00:00', '2010-02-02 15:00:00', '2010-02-03 03:00:00', '2010-02-03 15:00:00', '2010-02-04 03:00:00', '2010-02-04 15:00:00', '2010-02-05 03:00:00', '2010-02-05 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-08 03:00:00', '2010-02-08 15:00:00', '2010-02-09 03:00:00', '2010-02-09 15:00:00', '2010-02-10 03:00:00', '2010-02-10 15:00:00', '2010-02-11 03:00:00'], freq=None).as_unit(exp_unit)
tm.assert_index_equal(t1, expected)
pointwise = DatetimeIndex([x + off for x in idx]).as_unit(exp_unit)
tm.assert_index_equal(pointwise, expected)
```

## Next Steps


---

*Source: test_business_hour.py:951 | Complexity: Advanced | Last updated: 2026-06-02*