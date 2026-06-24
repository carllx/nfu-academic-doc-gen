# How To: Timedelta Floor Div Precision

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timedelta floor div precision

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: val1, val2
```

## Step-by-Step Guide

### Step 1: Assign op1 = np.timedelta64(...)

```python
op1 = np.timedelta64(val1)
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 2: Assign op2 = np.timedelta64(...)

```python
op2 = np.timedelta64(val2)
```

### Step 3: Assign actual = value

```python
actual = op1 // op2
```

### Step 4: Assign expected = value

```python
expected = val1 // val2
```

### Step 5: Call assert_equal()

```python
assert_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: val1, val2

# Workflow
op1 = np.timedelta64(val1)
op2 = np.timedelta64(val2)
actual = op1 // op2
expected = val1 // val2
assert_equal(actual, expected)
```

## Next Steps


---

*Source: test_datetime.py:1387 | Complexity: Intermediate | Last updated: 2026-06-02*