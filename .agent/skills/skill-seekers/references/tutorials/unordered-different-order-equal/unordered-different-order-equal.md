# How To: Unordered Different Order Equal

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unordered different order equal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ctor
```

## Step-by-Step Guide

### Step 1: Assign c1 = ctor(...)

```python
c1 = ctor(['a', 'b'], categories=['a', 'b'], ordered=False)
```

**Verification:**
```python
assert (c1 == c2).all()
```

### Step 2: Assign c2 = ctor(...)

```python
c2 = ctor(['a', 'b'], categories=['b', 'a'], ordered=False)
```

**Verification:**
```python
assert (c1 != c2).all()
```

### Step 3: Assign c1 = ctor(...)

```python
c1 = ctor(['a', 'b'], categories=['a', 'b'], ordered=False)
```

**Verification:**
```python
assert (c1 != c2).all()
```

### Step 4: Assign c2 = ctor(...)

```python
c2 = ctor(['b', 'a'], categories=['b', 'a'], ordered=False)
```

**Verification:**
```python
assert (c1 != c2).all()
```

### Step 5: Assign c1 = ctor(...)

```python
c1 = ctor(['a', 'a'], categories=['a', 'b'], ordered=False)
```

### Step 6: Assign c2 = ctor(...)

```python
c2 = ctor(['b', 'b'], categories=['b', 'a'], ordered=False)
```

**Verification:**
```python
assert (c1 != c2).all()
```

### Step 7: Assign c1 = ctor(...)

```python
c1 = ctor(['a', 'a'], categories=['a', 'b'], ordered=False)
```

### Step 8: Assign c2 = ctor(...)

```python
c2 = ctor(['a', 'b'], categories=['b', 'a'], ordered=False)
```

### Step 9: Assign result = value

```python
result = c1 == c2
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result), np.array([True, False]))
```


## Complete Example

```python
# Setup
# Fixtures: ctor

# Workflow
c1 = ctor(['a', 'b'], categories=['a', 'b'], ordered=False)
c2 = ctor(['a', 'b'], categories=['b', 'a'], ordered=False)
assert (c1 == c2).all()
c1 = ctor(['a', 'b'], categories=['a', 'b'], ordered=False)
c2 = ctor(['b', 'a'], categories=['b', 'a'], ordered=False)
assert (c1 != c2).all()
c1 = ctor(['a', 'a'], categories=['a', 'b'], ordered=False)
c2 = ctor(['b', 'b'], categories=['b', 'a'], ordered=False)
assert (c1 != c2).all()
c1 = ctor(['a', 'a'], categories=['a', 'b'], ordered=False)
c2 = ctor(['a', 'b'], categories=['b', 'a'], ordered=False)
result = c1 == c2
tm.assert_numpy_array_equal(np.array(result), np.array([True, False]))
```

## Next Steps


---

*Source: test_operators.py:317 | Complexity: Advanced | Last updated: 2026-06-02*