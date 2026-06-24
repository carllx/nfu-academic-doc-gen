# How To: Construction With Alt

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test construction with alt

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: kwargs, tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign i = date_range(...)

```python
i = date_range('20130101', periods=5, freq='h', tz=tz)
```

### Step 3: Assign kwargs = value

```python
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
```

### Step 4: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(i, **kwargs)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(i, result)
```


## Complete Example

```python
# Setup
# Fixtures: kwargs, tz_aware_fixture

# Workflow
tz = tz_aware_fixture
i = date_range('20130101', periods=5, freq='h', tz=tz)
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
result = DatetimeIndex(i, **kwargs)
tm.assert_index_equal(i, result)
```

## Next Steps


---

*Source: test_constructors.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*