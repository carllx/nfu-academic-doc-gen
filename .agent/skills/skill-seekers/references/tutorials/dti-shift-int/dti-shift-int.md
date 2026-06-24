# How To: Dti Shift Int

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti shift int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', periods=20, unit=unit)
```

### Step 2: Assign result = value

```python
result = rng + 5 * rng.freq
```

### Step 3: Assign expected = rng.shift(...)

```python
expected = rng.shift(5)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = rng - 5 * rng.freq
```

### Step 6: Assign expected = rng.shift(...)

```python
expected = rng.shift(-5)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
rng = date_range('1/1/2000', periods=20, unit=unit)
result = rng + 5 * rng.freq
expected = rng.shift(5)
tm.assert_index_equal(result, expected)
result = rng - 5 * rng.freq
expected = rng.shift(-5)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*