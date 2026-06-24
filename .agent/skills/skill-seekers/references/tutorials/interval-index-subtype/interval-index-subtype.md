# How To: Interval Index Subtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interval index subtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: timezone, inclusive_endpoints_fixture
```

## Step-by-Step Guide

### Step 1: Assign dates = date_range(...)

```python
dates = date_range('2022', periods=3, tz=timezone)
```

### Step 2: Assign dtype = value

```python
dtype = f'interval[datetime64[ns, {timezone}], {inclusive_endpoints_fixture}]'
```

### Step 3: Assign result = IntervalIndex.from_arrays(...)

```python
result = IntervalIndex.from_arrays(['2022-01-01', '2022-01-02'], ['2022-01-02', '2022-01-03'], closed=inclusive_endpoints_fixture, dtype=dtype)
```

### Step 4: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays(dates[:-1], dates[1:], closed=inclusive_endpoints_fixture)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: timezone, inclusive_endpoints_fixture

# Workflow
dates = date_range('2022', periods=3, tz=timezone)
dtype = f'interval[datetime64[ns, {timezone}], {inclusive_endpoints_fixture}]'
result = IntervalIndex.from_arrays(['2022-01-01', '2022-01-02'], ['2022-01-02', '2022-01-03'], closed=inclusive_endpoints_fixture, dtype=dtype)
expected = IntervalIndex.from_arrays(dates[:-1], dates[1:], closed=inclusive_endpoints_fixture)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:495 | Complexity: Intermediate | Last updated: 2026-06-02*