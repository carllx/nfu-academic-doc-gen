# How To: Apply Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`

**Setup Required:**
```python
# Fixtures: case
```

## Step-by-Step Guide

### Step 1: Assign unknown = case

```python
offset, cases = case
```

### Step 2: Assign shift = DatetimeIndex(...)

```python
shift = DatetimeIndex(cases.keys())
```

### Step 3: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex(cases.values())
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 5: Assign result = value

```python
result = offset + shift
```


## Complete Example

```python
# Setup
# Fixtures: case

# Workflow
offset, cases = case
shift = DatetimeIndex(cases.keys())
with tm.assert_produces_warning(None):
    result = offset + shift
exp = DatetimeIndex(cases.values())
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_month.py:441 | Complexity: Intermediate | Last updated: 2026-06-02*