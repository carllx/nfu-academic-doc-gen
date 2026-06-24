# How To: Union3

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union3

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
# Fixtures: sort, box
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

### Step 4: Assign expected = first.union(...)

```python
expected = first.union(second, sort=sort)
```

### Step 5: Assign case = box(...)

```python
case = box(second.values)
```

### Step 6: Assign result = first.union(...)

```python
result = first.union(case, sort=sort)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort, box

# Workflow
everything = date_range('2020-01-01', periods=10)
first = everything[:5]
second = everything[5:]
expected = first.union(second, sort=sort)
case = box(second.values)
result = first.union(case, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*