# How To: Date Range Int64 Overflow Non Recoverable

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range int64 overflow non recoverable

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

### Step 2: Call date_range()

```python
date_range(start='1970-02-01', periods=106752 * 24, freq='h')
```

### Step 3: Call date_range()

```python
date_range(end='1969-11-14', periods=106752 * 24, freq='h')
```


## Complete Example

```python
# Workflow
msg = 'Cannot generate range with'
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(start='1970-02-01', periods=106752 * 24, freq='h')
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range(end='1969-11-14', periods=106752 * 24, freq='h')
```

## Next Steps


---

*Source: test_date_range.py:252 | Complexity: Beginner | Last updated: 2026-06-02*