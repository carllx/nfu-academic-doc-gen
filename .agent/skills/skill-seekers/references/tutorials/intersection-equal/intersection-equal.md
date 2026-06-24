# How To: Intersection Equal

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection equal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign first = timedelta_range(...)

```python
first = timedelta_range('1 day', periods=4, freq='h')
```

**Verification:**
```python
assert inter is first
```

### Step 2: Assign second = timedelta_range(...)

```python
second = timedelta_range('1 day', periods=4, freq='h')
```

### Step 3: Assign intersect = first.intersection(...)

```python
intersect = first.intersection(second, sort=sort)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(intersect, second)
```

### Step 5: Assign inter = first.intersection(...)

```python
inter = first.intersection(first, sort=sort)
```

**Verification:**
```python
assert inter is first
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(intersect, second.sort_values())
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
first = timedelta_range('1 day', periods=4, freq='h')
second = timedelta_range('1 day', periods=4, freq='h')
intersect = first.intersection(second, sort=sort)
if sort is None:
    tm.assert_index_equal(intersect, second.sort_values())
tm.assert_index_equal(intersect, second)
inter = first.intersection(first, sort=sort)
assert inter is first
```

## Next Steps


---

*Source: test_setops.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*