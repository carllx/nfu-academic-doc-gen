# How To: Isin Mixed Huge Vals

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test values outside intp range (negative ones if 32bit system)

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
# Fixtures: kind, data
```

## Step-by-Step Guide

### Step 1: 'Test values outside intp range (negative ones if 32bit system)'

```python
'Test values outside intp range (negative ones if 32bit system)'
```

**Verification:**
```python
assert_array_equal(res, [False, True])
```

### Step 2: Assign query = value

```python
query = data[1]
```

**Verification:**
```python
assert_array_equal(res, [False, False])
```

### Step 3: Assign res = np.isin(...)

```python
res = np.isin(data, query, kind=kind)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(res, [False, True])
```

### Step 5: Assign data = data.astype(...)

```python
data = data.astype(np.int32)
```

### Step 6: Assign res = np.isin(...)

```python
res = np.isin(data, query, kind=kind)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res, [False, False])
```


## Complete Example

```python
# Setup
# Fixtures: kind, data

# Workflow
'Test values outside intp range (negative ones if 32bit system)'
query = data[1]
res = np.isin(data, query, kind=kind)
assert_array_equal(res, [False, True])
data = data.astype(np.int32)
res = np.isin(data, query, kind=kind)
assert_array_equal(res, [False, False])
```

## Next Steps


---

*Source: test_arraysetops.py:451 | Complexity: Intermediate | Last updated: 2026-06-02*