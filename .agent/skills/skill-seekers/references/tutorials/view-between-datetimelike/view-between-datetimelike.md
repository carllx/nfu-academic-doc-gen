# How To: View Between Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test view between datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: first, second, box
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

**Verification:**
```python
assert obj.dtype == first
```

### Step 2: Assign orig = box(...)

```python
orig = box(dti)
```

**Verification:**
```python
assert res.dtype == second
```

### Step 3: Assign obj = orig.view(...)

```python
obj = orig.view(first)
```

**Verification:**
```python
assert obj.dtype == first
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.asarray(obj.view('i8')), dti.asi8)
```

### Step 5: Assign res = obj.view(...)

```python
res = obj.view(second)
```

**Verification:**
```python
assert res.dtype == second
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.asarray(obj.view('i8')), dti.asi8)
```


## Complete Example

```python
# Setup
# Fixtures: first, second, box

# Workflow
dti = date_range('2016-01-01', periods=3)
orig = box(dti)
obj = orig.view(first)
assert obj.dtype == first
tm.assert_numpy_array_equal(np.asarray(obj.view('i8')), dti.asi8)
res = obj.view(second)
assert res.dtype == second
tm.assert_numpy_array_equal(np.asarray(obj.view('i8')), dti.asi8)
```

## Next Steps


---

*Source: test_view.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*