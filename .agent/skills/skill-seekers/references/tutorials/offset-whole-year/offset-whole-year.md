# How To: Offset Whole Year

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test offset whole year

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = (datetime(2007, 12, 15), datetime(2008, 1, 1), datetime(2008, 1, 15), datetime(2008, 2, 1), datetime(2008, 2, 15), datetime(2008, 3, 1), datetime(2008, 3, 15), datetime(2008, 4, 1), datetime(2008, 4, 15), datetime(2008, 5, 1), datetime(2008, 5, 15), datetime(2008, 6, 1), datetime(2008, 6, 15), datetime(2008, 7, 1), datetime(2008, 7, 15), datetime(2008, 8, 1), datetime(2008, 8, 15), datetime(2008, 9, 1), datetime(2008, 9, 15), datetime(2008, 10, 1), datetime(2008, 10, 15), datetime(2008, 11, 1), datetime(2008, 11, 15), datetime(2008, 12, 1), datetime(2008, 12, 15))
```

**Verification:**
```python
assert_offset_equal(SemiMonthBegin(), base, exp_date)
```

### Step 2: Assign shift = DatetimeIndex(...)

```python
shift = DatetimeIndex(dates[:-1])
```

### Step 3: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex(dates[1:])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 5: Call assert_offset_equal()

```python
assert_offset_equal(SemiMonthBegin(), base, exp_date)
```

### Step 6: Assign result = value

```python
result = SemiMonthBegin() + shift
```


## Complete Example

```python
# Workflow
dates = (datetime(2007, 12, 15), datetime(2008, 1, 1), datetime(2008, 1, 15), datetime(2008, 2, 1), datetime(2008, 2, 15), datetime(2008, 3, 1), datetime(2008, 3, 15), datetime(2008, 4, 1), datetime(2008, 4, 15), datetime(2008, 5, 1), datetime(2008, 5, 15), datetime(2008, 6, 1), datetime(2008, 6, 15), datetime(2008, 7, 1), datetime(2008, 7, 15), datetime(2008, 8, 1), datetime(2008, 8, 15), datetime(2008, 9, 1), datetime(2008, 9, 15), datetime(2008, 10, 1), datetime(2008, 10, 15), datetime(2008, 11, 1), datetime(2008, 11, 15), datetime(2008, 12, 1), datetime(2008, 12, 15))
for base, exp_date in zip(dates[:-1], dates[1:]):
    assert_offset_equal(SemiMonthBegin(), base, exp_date)
shift = DatetimeIndex(dates[:-1])
with tm.assert_produces_warning(None):
    result = SemiMonthBegin() + shift
exp = DatetimeIndex(dates[1:])
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_month.py:285 | Complexity: Intermediate | Last updated: 2026-06-02*