# How To: Pydatetime Creation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pydatetime creation

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
a = np.array(['1960-03-12', datetime.date(1960, 3, 12)], dtype='M8[D]')
```

**Verification:**
```python
assert_equal(a[0], a[1])
```

### Step 2: Call assert_equal()

```python
assert_equal(a[0], a[1])
```

**Verification:**
```python
assert_equal(a[0], a[1])
```

### Step 3: Assign a = np.array(...)

```python
a = np.array(['1999-12-31', datetime.date(1999, 12, 31)], dtype='M8[D]')
```

**Verification:**
```python
assert_equal(a[0], a[1])
```

### Step 4: Call assert_equal()

```python
assert_equal(a[0], a[1])
```

**Verification:**
```python
assert_equal(a[0], a[1])
```

### Step 5: Assign a = np.array(...)

```python
a = np.array(['2000-01-01', datetime.date(2000, 1, 1)], dtype='M8[D]')
```

**Verification:**
```python
assert_equal(np.array(datetime.date(1960, 3, 12), dtype='M8[s]'), np.array(np.datetime64('1960-03-12T00:00:00')))
```

### Step 6: Call assert_equal()

```python
assert_equal(a[0], a[1])
```

### Step 7: Assign a = np.array(...)

```python
a = np.array(['today', datetime.date.today()], dtype='M8[D]')
```

### Step 8: Call assert_equal()

```python
assert_equal(a[0], a[1])
```

### Step 9: Call assert_equal()

```python
assert_equal(np.array(datetime.date(1960, 3, 12), dtype='M8[s]'), np.array(np.datetime64('1960-03-12T00:00:00')))
```


## Complete Example

```python
# Workflow
a = np.array(['1960-03-12', datetime.date(1960, 3, 12)], dtype='M8[D]')
assert_equal(a[0], a[1])
a = np.array(['1999-12-31', datetime.date(1999, 12, 31)], dtype='M8[D]')
assert_equal(a[0], a[1])
a = np.array(['2000-01-01', datetime.date(2000, 1, 1)], dtype='M8[D]')
assert_equal(a[0], a[1])
a = np.array(['today', datetime.date.today()], dtype='M8[D]')
assert_equal(a[0], a[1])
assert_equal(np.array(datetime.date(1960, 3, 12), dtype='M8[s]'), np.array(np.datetime64('1960-03-12T00:00:00')))
```

## Next Steps


---

*Source: test_datetime.py:703 | Complexity: Advanced | Last updated: 2026-06-02*