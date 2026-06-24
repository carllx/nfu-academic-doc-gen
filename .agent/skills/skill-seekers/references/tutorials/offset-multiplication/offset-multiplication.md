# How To: Offset Multiplication

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test offset multiplication

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: n_months, scaling_factor, start_timestamp, expected_timestamp
```

## Step-by-Step Guide

### Step 1: Assign mo1 = DateOffset(...)

```python
mo1 = DateOffset(months=n_months)
```

**Verification:**
```python
assert resultscalar == expectedscalar
```

### Step 2: Assign startscalar = Timestamp(...)

```python
startscalar = Timestamp(start_timestamp)
```

### Step 3: Assign startarray = Series(...)

```python
startarray = Series([startscalar])
```

### Step 4: Assign resultscalar = value

```python
resultscalar = startscalar + mo1 * scaling_factor
```

### Step 5: Assign resultarray = value

```python
resultarray = startarray + mo1 * scaling_factor
```

### Step 6: Assign expectedscalar = Timestamp(...)

```python
expectedscalar = Timestamp(expected_timestamp)
```

### Step 7: Assign expectedarray = Series(...)

```python
expectedarray = Series([expectedscalar])
```

**Verification:**
```python
assert resultscalar == expectedscalar
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(resultarray, expectedarray)
```


## Complete Example

```python
# Setup
# Fixtures: n_months, scaling_factor, start_timestamp, expected_timestamp

# Workflow
mo1 = DateOffset(months=n_months)
startscalar = Timestamp(start_timestamp)
startarray = Series([startscalar])
resultscalar = startscalar + mo1 * scaling_factor
resultarray = startarray + mo1 * scaling_factor
expectedscalar = Timestamp(expected_timestamp)
expectedarray = Series([expectedscalar])
assert resultscalar == expectedscalar
tm.assert_series_equal(resultarray, expectedarray)
```

## Next Steps


---

*Source: test_offsets.py:1103 | Complexity: Advanced | Last updated: 2026-06-02*