# How To: Isin Timedelta

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that isin works for timedelta input

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.dtypes`
- `numpy.exceptions`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: 'Test that isin works for timedelta input'

```python
'Test that isin works for timedelta input'
```

**Verification:**
```python
assert_array_equal(truth, isin(a_timedelta, b_timedelta, kind=kind))
```

### Step 2: Assign rstate = np.random.RandomState(...)

```python
rstate = np.random.RandomState(0)
```

### Step 3: Assign a = rstate.randint(...)

```python
a = rstate.randint(0, 100, size=10)
```

### Step 4: Assign b = rstate.randint(...)

```python
b = rstate.randint(0, 100, size=10)
```

### Step 5: Assign truth = isin(...)

```python
truth = isin(a, b)
```

### Step 6: Assign a_timedelta = a.astype(...)

```python
a_timedelta = a.astype('timedelta64[s]')
```

### Step 7: Assign b_timedelta = b.astype(...)

```python
b_timedelta = b.astype('timedelta64[s]')
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(truth, isin(a_timedelta, b_timedelta, kind=kind))
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
'Test that isin works for timedelta input'
rstate = np.random.RandomState(0)
a = rstate.randint(0, 100, size=10)
b = rstate.randint(0, 100, size=10)
truth = isin(a, b)
a_timedelta = a.astype('timedelta64[s]')
b_timedelta = b.astype('timedelta64[s]')
assert_array_equal(truth, isin(a_timedelta, b_timedelta, kind=kind))
```

## Next Steps


---

*Source: test_arraysetops.py:395 | Complexity: Advanced | Last updated: 2026-06-02*