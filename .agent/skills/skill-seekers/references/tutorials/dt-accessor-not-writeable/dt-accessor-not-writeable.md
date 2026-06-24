# How To: Dt Accessor Not Writeable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt accessor not writeable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
```

### Step 2: Assign msg = 'modifications to a property of a datetimelike.+not supported'

```python
msg = 'modifications to a property of a datetimelike.+not supported'
```

### Step 3: Assign ser.dt.hour = 5

```python
ser.dt.hour = 5
```

### Step 4: Assign unknown = 5

```python
ser.dt.hour[0] = 5
```

### Step 5: Assign unknown = 5

```python
ser.dt.hour[0] = 5
```

### Step 6: Assign unknown = 5

```python
ser.dt.hour[0] = 5
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
ser = Series(date_range('20130101', periods=5, freq='D'), name='xxx')
with pytest.raises(ValueError, match='modifications'):
    ser.dt.hour = 5
msg = 'modifications to a property of a datetimelike.+not supported'
with pd.option_context('chained_assignment', 'raise'):
    if using_copy_on_write:
        with tm.raises_chained_assignment_error():
            ser.dt.hour[0] = 5
    elif warn_copy_on_write:
        with tm.assert_produces_warning(FutureWarning, match='ChainedAssignmentError'):
            ser.dt.hour[0] = 5
    else:
        with pytest.raises(SettingWithCopyError, match=msg):
            ser.dt.hour[0] = 5
```

## Next Steps


---

*Source: test_dt_accessor.py:285 | Complexity: Intermediate | Last updated: 2026-06-02*