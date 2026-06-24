# How To: Array Almost Equal Matrix

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array almost equal matrix

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign m1 = np.matrix(...)

```python
m1 = np.matrix([[1.0, 2.0]])
```

**Verification:**
```python
assert_func(m, m)
```

### Step 2: Assign m2 = np.matrix(...)

```python
m2 = np.matrix([[1.0, np.nan]])
```

**Verification:**
```python
assert_func(a, m)
```

### Step 3: Assign m3 = np.matrix(...)

```python
m3 = np.matrix([[1.0, -np.inf]])
```

**Verification:**
```python
assert_func(m, a)
```

### Step 4: Assign m4 = np.matrix(...)

```python
m4 = np.matrix([[np.nan, np.inf]])
```

### Step 5: Assign m5 = np.matrix(...)

```python
m5 = np.matrix([[1.0, 2.0], [np.nan, np.inf]])
```

### Step 6: Call assert_func()

```python
assert_func(m, m)
```

### Step 7: Assign a = np.array(...)

```python
a = np.array(m)
```

### Step 8: Call assert_func()

```python
assert_func(a, m)
```

### Step 9: Call assert_func()

```python
assert_func(m, a)
```


## Complete Example

```python
# Workflow
m1 = np.matrix([[1.0, 2.0]])
m2 = np.matrix([[1.0, np.nan]])
m3 = np.matrix([[1.0, -np.inf]])
m4 = np.matrix([[np.nan, np.inf]])
m5 = np.matrix([[1.0, 2.0], [np.nan, np.inf]])
for assert_func in (assert_array_almost_equal, assert_almost_equal):
    for m in (m1, m2, m3, m4, m5):
        assert_func(m, m)
        a = np.array(m)
        assert_func(a, m)
        assert_func(m, a)
```

## Next Steps


---

*Source: test_interaction.py:346 | Complexity: Advanced | Last updated: 2026-06-02*