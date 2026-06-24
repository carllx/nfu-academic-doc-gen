# How To: Datetime Compare Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime compare nat

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt_nat = np.datetime64(...)

```python
dt_nat = np.datetime64('NaT', 'D')
```

**Verification:**
```python
assert_(not op(dt_nat, dt_nat))
```

### Step 2: Assign dt_other = np.datetime64(...)

```python
dt_other = np.datetime64('2000-01-01')
```

**Verification:**
```python
assert_(not op(dt_nat, dt_other))
```

### Step 3: Assign td_nat = np.timedelta64(...)

```python
td_nat = np.timedelta64('NaT', 'h')
```

**Verification:**
```python
assert_(not op(dt_other, dt_nat))
```

### Step 4: Assign td_other = np.timedelta64(...)

```python
td_other = np.timedelta64(1, 'h')
```

**Verification:**
```python
assert_(not op(td_nat, td_nat))
```

### Step 5: Call assert_()

```python
assert_(np.not_equal(dt_nat, dt_nat))
```

**Verification:**
```python
assert_(not op(td_nat, td_other))
```

### Step 6: Call assert_()

```python
assert_(np.not_equal(dt_nat, dt_other))
```

**Verification:**
```python
assert_(not op(td_other, td_nat))
```

### Step 7: Call assert_()

```python
assert_(np.not_equal(dt_other, dt_nat))
```

**Verification:**
```python
assert_(np.not_equal(dt_nat, dt_nat))
```

### Step 8: Call assert_()

```python
assert_(np.not_equal(td_nat, td_nat))
```

**Verification:**
```python
assert_(np.not_equal(dt_nat, dt_other))
```

### Step 9: Call assert_()

```python
assert_(np.not_equal(td_nat, td_other))
```

**Verification:**
```python
assert_(np.not_equal(dt_other, dt_nat))
```

### Step 10: Call assert_()

```python
assert_(np.not_equal(td_other, td_nat))
```

**Verification:**
```python
assert_(np.not_equal(td_nat, td_nat))
```

### Step 11: Call assert_()

```python
assert_(not op(dt_nat, dt_nat))
```

**Verification:**
```python
assert_(np.not_equal(td_nat, td_other))
```

### Step 12: Call assert_()

```python
assert_(not op(dt_nat, dt_other))
```

**Verification:**
```python
assert_(np.not_equal(td_other, td_nat))
```

### Step 13: Call assert_()

```python
assert_(not op(dt_other, dt_nat))
```

### Step 14: Call assert_()

```python
assert_(not op(td_nat, td_nat))
```

### Step 15: Call assert_()

```python
assert_(not op(td_nat, td_other))
```

### Step 16: Call assert_()

```python
assert_(not op(td_other, td_nat))
```


## Complete Example

```python
# Workflow
dt_nat = np.datetime64('NaT', 'D')
dt_other = np.datetime64('2000-01-01')
td_nat = np.timedelta64('NaT', 'h')
td_other = np.timedelta64(1, 'h')
for op in [np.equal, np.less, np.less_equal, np.greater, np.greater_equal]:
    assert_(not op(dt_nat, dt_nat))
    assert_(not op(dt_nat, dt_other))
    assert_(not op(dt_other, dt_nat))
    assert_(not op(td_nat, td_nat))
    assert_(not op(td_nat, td_other))
    assert_(not op(td_other, td_nat))
assert_(np.not_equal(dt_nat, dt_nat))
assert_(np.not_equal(dt_nat, dt_other))
assert_(np.not_equal(dt_other, dt_nat))
assert_(np.not_equal(td_nat, td_nat))
assert_(np.not_equal(td_nat, td_other))
assert_(np.not_equal(td_other, td_nat))
```

## Next Steps


---

*Source: test_datetime.py:1545 | Complexity: Advanced | Last updated: 2026-06-02*