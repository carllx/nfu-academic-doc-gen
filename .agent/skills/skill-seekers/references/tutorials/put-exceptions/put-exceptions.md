# How To: Put Exceptions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test put exceptions

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.zeros(...)

```python
a = np.zeros((5, 5))
```

**Verification:**
```python
assert_raises(IndexError, a.put, 100, 0)
```

### Step 2: Call assert_raises()

```python
assert_raises(IndexError, a.put, 100, 0)
```

**Verification:**
```python
assert_raises(IndexError, a.put, 100, 0)
```

### Step 3: Assign a = np.zeros(...)

```python
a = np.zeros((5, 5), dtype=object)
```

**Verification:**
```python
assert_raises(IndexError, a.put, 100, 0)
```

### Step 4: Call assert_raises()

```python
assert_raises(IndexError, a.put, 100, 0)
```

**Verification:**
```python
assert_raises(IndexError, a.put, 100, 0)
```

### Step 5: Assign a = np.zeros(...)

```python
a = np.zeros((5, 5, 0))
```

### Step 6: Call assert_raises()

```python
assert_raises(IndexError, a.put, 100, 0)
```

### Step 7: Assign a = np.zeros(...)

```python
a = np.zeros((5, 5, 0), dtype=object)
```

### Step 8: Call assert_raises()

```python
assert_raises(IndexError, a.put, 100, 0)
```


## Complete Example

```python
# Workflow
a = np.zeros((5, 5))
assert_raises(IndexError, a.put, 100, 0)
a = np.zeros((5, 5), dtype=object)
assert_raises(IndexError, a.put, 100, 0)
a = np.zeros((5, 5, 0))
assert_raises(IndexError, a.put, 100, 0)
a = np.zeros((5, 5, 0), dtype=object)
assert_raises(IndexError, a.put, 100, 0)
```

## Next Steps


---

*Source: test_indexerrors.py:35 | Complexity: Advanced | Last updated: 2026-06-02*