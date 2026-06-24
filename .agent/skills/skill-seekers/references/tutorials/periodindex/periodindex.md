# How To: Periodindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test periodindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, cons
```

## Step-by-Step Guide

### Step 1: Assign dt = period_range(...)

```python
dt = period_range('2019-12-31', periods=3, freq='D')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dt)
```

### Step 3: Assign idx = cons(...)

```python
idx = cons(ser)
```

### Step 4: Assign expected = idx.copy(...)

```python
expected = idx.copy(deep=True)
```

### Step 5: Assign unknown = Period(...)

```python
ser.iloc[0] = Period('2020-12-31')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, cons

# Workflow
dt = period_range('2019-12-31', periods=3, freq='D')
ser = Series(dt)
idx = cons(ser)
expected = idx.copy(deep=True)
ser.iloc[0] = Period('2020-12-31')
if using_copy_on_write:
    tm.assert_index_equal(idx, expected)
```

## Next Steps


---

*Source: test_periodindex.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*