# How To: Integer Comparison

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test integer comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `hypothesis`
- `pytest`
- `hypothesis`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: sctype, other_val, comp
```

## Step-by-Step Guide

### Step 1: Assign val_obj = 10

```python
val_obj = 10
```

**Verification:**
```python
assert comp(10, other_val) == comp(val, other_val)
```

### Step 2: Assign val = sctype(...)

```python
val = sctype(val_obj)
```

**Verification:**
```python
assert comp(val, other_val) == comp(10, other_val)
```

### Step 3: Assign val_obj = np.array(...)

```python
val_obj = np.array([10, 10], dtype=object)
```

**Verification:**
```python
assert type(comp(val, other_val)) is np.bool
```

### Step 4: Assign val = val_obj.astype(...)

```python
val = val_obj.astype(sctype)
```

**Verification:**
```python
assert_array_equal(comp(val_obj, other_val), comp(val, other_val))
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(comp(val_obj, other_val), comp(val, other_val))
```

**Verification:**
```python
assert_array_equal(comp(other_val, val_obj), comp(other_val, val))
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(comp(other_val, val_obj), comp(other_val, val))
```


## Complete Example

```python
# Setup
# Fixtures: sctype, other_val, comp

# Workflow
val_obj = 10
val = sctype(val_obj)
assert comp(10, other_val) == comp(val, other_val)
assert comp(val, other_val) == comp(10, other_val)
assert type(comp(val, other_val)) is np.bool
val_obj = np.array([10, 10], dtype=object)
val = val_obj.astype(sctype)
assert_array_equal(comp(val_obj, other_val), comp(val, other_val))
assert_array_equal(comp(other_val, val_obj), comp(other_val, val))
```

## Next Steps


---

*Source: test_nep50_promotions.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*