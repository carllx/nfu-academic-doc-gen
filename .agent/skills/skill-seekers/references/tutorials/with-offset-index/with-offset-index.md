# How To: With Offset Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test with offset index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: td, dt, offset
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([dt])
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([datetime(2008, 1, 2, 2)])
```

### Step 3: Assign result = value

```python
result = dti + (td + offset)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = dti + (offset + td)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: td, dt, offset

# Workflow
dti = DatetimeIndex([dt])
expected = DatetimeIndex([datetime(2008, 1, 2, 2)])
result = dti + (td + offset)
tm.assert_index_equal(result, expected)
result = dti + (offset + td)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_business_day.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*