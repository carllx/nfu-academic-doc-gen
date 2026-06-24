# How To: Is Dtype No Warning

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is dtype no warning

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: check
```

## Step-by-Step Guide

### Step 1: Assign data = pd.DataFrame(...)

```python
data = pd.DataFrame({'A': [1, 2]})
```

### Step 2: Assign warn = None

```python
warn = None
```

### Step 3: Assign msg = value

```python
msg = f'{check.__name__} is deprecated'
```

### Step 4: Assign warn = DeprecationWarning

```python
warn = DeprecationWarning
```

### Step 5: Call check()

```python
check(data)
```

### Step 6: Call check()

```python
check(data['A'])
```


## Complete Example

```python
# Setup
# Fixtures: check

# Workflow
data = pd.DataFrame({'A': [1, 2]})
warn = None
msg = f'{check.__name__} is deprecated'
if check is is_categorical_dtype or check is is_interval_dtype or check is is_datetime64tz_dtype or (check is is_period_dtype):
    warn = DeprecationWarning
with tm.assert_produces_warning(warn, match=msg):
    check(data)
with tm.assert_produces_warning(warn, match=msg):
    check(data['A'])
```

## Next Steps


---

*Source: test_dtypes.py:1170 | Complexity: Intermediate | Last updated: 2026-06-02*