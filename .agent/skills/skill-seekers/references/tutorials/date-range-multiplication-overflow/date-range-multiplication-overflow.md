# How To: Date Range Multiplication Overflow

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range multiplication overflow

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`
- `pandas.tseries.holiday`
- `pandas._libs.tslibs.timezones`
- `pandas._libs.tslibs.timezones`


## Step-by-Step Guide

### Step 1: Assign msg = 'Cannot generate range with'

```python
msg = 'Cannot generate range with'
```

**Verification:**
```python
assert dti[0] == Timestamp('1677-09-22')
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range(start='1677-09-22', periods=213503, freq='D')
```

**Verification:**
```python
assert len(dti) == 213503
```

### Step 3: Call date_range()

```python
date_range('1969-05-04', periods=200000000, freq='30000D')
```


## Complete Example

```python
# Workflow
with tm.assert_produces_warning(None):
    dti = date_range(start='1677-09-22', periods=213503, freq='D')
assert dti[0] == Timestamp('1677-09-22')
assert len(dti) == 213503
msg = 'Cannot generate range with'
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range('1969-05-04', periods=200000000, freq='30000D')
```

## Next Steps


---

*Source: test_date_range.py:225 | Complexity: Beginner | Last updated: 2026-06-02*