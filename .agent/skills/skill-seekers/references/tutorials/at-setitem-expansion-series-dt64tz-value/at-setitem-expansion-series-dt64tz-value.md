# How To: At Setitem Expansion Series Dt64Tz Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at setitem expansion series dt64tz value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2017-08-05 00:00:00+0100', tz=tz_naive_fixture)
```

### Step 2: Assign result = Series(...)

```python
result = Series(ts)
```

### Step 3: Assign unknown = ts

```python
result.at[1] = ts
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([ts, ts])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
ts = Timestamp('2017-08-05 00:00:00+0100', tz=tz_naive_fixture)
result = Series(ts)
result.at[1] = ts
expected = Series([ts, ts])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_at.py:132 | Complexity: Intermediate | Last updated: 2026-06-02*