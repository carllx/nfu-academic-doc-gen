# How To: Dti Timetz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti timetz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(tz_naive_fixture)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([time(10, 20, 30, tzinfo=tz), NaT])
```

### Step 3: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(['2018-06-04 10:20:30', NaT], tz=tz)
```

### Step 4: Assign result = value

```python
result = index.timetz
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = timezones.maybe_get_tz(tz_naive_fixture)
expected = np.array([time(10, 20, 30, tzinfo=tz), NaT])
index = DatetimeIndex(['2018-06-04 10:20:30', NaT], tz=tz)
result = index.timetz
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_scalar_compat.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*