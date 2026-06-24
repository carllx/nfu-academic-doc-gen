# How To: Timedelta Array Str

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta array str

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([-1, 0, 100], dtype='m')
```

**Verification:**
```python
assert_equal(str(a), '[ -1   0 100]')
```

### Step 2: Call assert_equal()

```python
assert_equal(str(a), '[ -1   0 100]')
```

**Verification:**
```python
assert_equal(str(a), "['NaT' 'NaT']")
```

### Step 3: Assign a = np.array(...)

```python
a = np.array(['NaT', 'NaT'], dtype='m')
```

**Verification:**
```python
assert_equal(str(a), "[   -1 'NaT'     0]")
```

### Step 4: Call assert_equal()

```python
assert_equal(str(a), "['NaT' 'NaT']")
```

**Verification:**
```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

### Step 5: Assign a = np.array(...)

```python
a = np.array([-1, 'NaT', 0], dtype='m')
```

**Verification:**
```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

### Step 6: Call assert_equal()

```python
assert_equal(str(a), "[   -1 'NaT'     0]")
```

**Verification:**
```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

### Step 7: Assign a = np.array(...)

```python
a = np.array([-1, 'NaT', 1234567], dtype='m')
```

### Step 8: Call assert_equal()

```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

### Step 9: Assign a = np.array(...)

```python
a = np.array([-1, 'NaT', 1234567], dtype='>m')
```

### Step 10: Call assert_equal()

```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

### Step 11: Assign a = np.array(...)

```python
a = np.array([-1, 'NaT', 1234567], dtype='<m')
```

### Step 12: Call assert_equal()

```python
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```


## Complete Example

```python
# Workflow
a = np.array([-1, 0, 100], dtype='m')
assert_equal(str(a), '[ -1   0 100]')
a = np.array(['NaT', 'NaT'], dtype='m')
assert_equal(str(a), "['NaT' 'NaT']")
a = np.array([-1, 'NaT', 0], dtype='m')
assert_equal(str(a), "[   -1 'NaT'     0]")
a = np.array([-1, 'NaT', 1234567], dtype='m')
assert_equal(str(a), "[     -1   'NaT' 1234567]")
a = np.array([-1, 'NaT', 1234567], dtype='>m')
assert_equal(str(a), "[     -1   'NaT' 1234567]")
a = np.array([-1, 'NaT', 1234567], dtype='<m')
assert_equal(str(a), "[     -1   'NaT' 1234567]")
```

## Next Steps


---

*Source: test_datetime.py:830 | Complexity: Advanced | Last updated: 2026-06-02*