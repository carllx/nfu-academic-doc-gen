# How To: Is Strictly Monotonic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is strictly monotonic

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index_cls = Index

```python
index_cls = Index
```

**Verification:**
```python
assert index.is_monotonic_increasing is True
```

### Step 2: Assign index = index_cls(...)

```python
index = index_cls([1, 1, 2, 3])
```

**Verification:**
```python
assert index._is_strictly_monotonic_increasing is False
```

### Step 3: Assign index = index_cls(...)

```python
index = index_cls([3, 2, 1, 1])
```

**Verification:**
```python
assert index.is_monotonic_decreasing is True
```

### Step 4: Assign index = index_cls(...)

```python
index = index_cls([1, 1])
```

**Verification:**
```python
assert index._is_strictly_monotonic_decreasing is False
```


## Complete Example

```python
# Workflow
index_cls = Index
index = index_cls([1, 1, 2, 3])
assert index.is_monotonic_increasing is True
assert index._is_strictly_monotonic_increasing is False
index = index_cls([3, 2, 1, 1])
assert index.is_monotonic_decreasing is True
assert index._is_strictly_monotonic_decreasing is False
index = index_cls([1, 1])
assert index.is_monotonic_increasing
assert index.is_monotonic_decreasing
assert not index._is_strictly_monotonic_increasing
assert not index._is_strictly_monotonic_decreasing
```

## Next Steps


---

*Source: test_numeric.py:270 | Complexity: Intermediate | Last updated: 2026-06-02*