# How To: Union2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`
- `pandas`
- `pandas`
- `pandas._libs.tslibs.timezones`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign everything = date_range(...)

```python
everything = date_range('2020-01-01', periods=10)
```

### Step 2: Assign first = value

```python
first = everything[:5]
```

### Step 3: Assign second = value

```python
second = everything[5:]
```

### Step 4: Assign union = first.union(...)

```python
union = first.union(second, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(union, everything)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
everything = date_range('2020-01-01', periods=10)
first = everything[:5]
second = everything[5:]
union = first.union(second, sort=sort)
tm.assert_index_equal(union, everything)
```

## Next Steps


---

*Source: test_setops.py:44 | Complexity: Intermediate | Last updated: 2026-06-02*