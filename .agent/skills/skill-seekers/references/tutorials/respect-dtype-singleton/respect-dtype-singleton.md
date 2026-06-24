# How To: Respect Dtype Singleton

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test respect dtype singleton

## Prerequisites

**Required Modules:**
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `hashlib`
- `threading`


## Step-by-Step Guide

### Step 1: Assign rng = random.RandomState(...)

```python
rng = random.RandomState()
```

**Verification:**
```python
assert_equal(sample.dtype, np.dtype(dt))
```

### Step 2: Assign lbnd = value

```python
lbnd = 0 if dt is np.bool else np.iinfo(dt).min
```

**Verification:**
```python
assert_(not hasattr(sample, 'dtype'))
```

### Step 3: Assign ubnd = value

```python
ubnd = 2 if dt is np.bool else np.iinfo(dt).max + 1
```

**Verification:**
```python
assert_equal(type(sample), dt)
```

### Step 4: Assign sample = rng.randint(...)

```python
sample = rng.randint(lbnd, ubnd, dtype=dt)
```

### Step 5: Call assert_equal()

```python
assert_equal(sample.dtype, np.dtype(dt))
```

### Step 6: Assign lbnd = value

```python
lbnd = 0 if dt is bool else np.iinfo('long').min
```

### Step 7: Assign ubnd = value

```python
ubnd = 2 if dt is bool else np.iinfo('long').max + 1
```

### Step 8: Assign sample = rng.randint(...)

```python
sample = rng.randint(lbnd, ubnd, dtype=dt)
```

### Step 9: Call assert_()

```python
assert_(not hasattr(sample, 'dtype'))
```

### Step 10: Call assert_equal()

```python
assert_equal(type(sample), dt)
```


## Complete Example

```python
# Workflow
rng = random.RandomState()
for dt in self.itype:
    lbnd = 0 if dt is np.bool else np.iinfo(dt).min
    ubnd = 2 if dt is np.bool else np.iinfo(dt).max + 1
    sample = rng.randint(lbnd, ubnd, dtype=dt)
    assert_equal(sample.dtype, np.dtype(dt))
for dt in (bool, int):
    lbnd = 0 if dt is bool else np.iinfo('long').min
    ubnd = 2 if dt is bool else np.iinfo('long').max + 1
    sample = rng.randint(lbnd, ubnd, dtype=dt)
    assert_(not hasattr(sample, 'dtype'))
    assert_equal(type(sample), dt)
```

## Next Steps


---

*Source: test_random.py:287 | Complexity: Advanced | Last updated: 2026-06-02*