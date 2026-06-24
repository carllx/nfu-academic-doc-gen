# How To: No Rounding Occurs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no rounding occurs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range(start='2016-01-01', periods=5, freq='2Min', tz=tz)
```

### Step 3: Assign expected_rng = DatetimeIndex.as_unit(...)

```python
expected_rng = DatetimeIndex([Timestamp('2016-01-01 00:00:00', tz=tz), Timestamp('2016-01-01 00:02:00', tz=tz), Timestamp('2016-01-01 00:04:00', tz=tz), Timestamp('2016-01-01 00:06:00', tz=tz), Timestamp('2016-01-01 00:08:00', tz=tz)]).as_unit('ns')
```

### Step 4: Assign result = rng.round(...)

```python
result = rng.round(freq='2min')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected_rng)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
rng = date_range(start='2016-01-01', periods=5, freq='2Min', tz=tz)
expected_rng = DatetimeIndex([Timestamp('2016-01-01 00:00:00', tz=tz), Timestamp('2016-01-01 00:02:00', tz=tz), Timestamp('2016-01-01 00:04:00', tz=tz), Timestamp('2016-01-01 00:06:00', tz=tz), Timestamp('2016-01-01 00:08:00', tz=tz)]).as_unit('ns')
result = rng.round(freq='2min')
tm.assert_index_equal(result, expected_rng)
```

## Next Steps


---

*Source: test_round.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*