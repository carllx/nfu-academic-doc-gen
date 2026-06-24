# How To: Get Nan Multiple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get nan multiple

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
# Fixtures: float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Index.to_series(...)

```python
s = Index(range(10), dtype=float_numpy_dtype).to_series()
```

**Verification:**
```python
assert s.get(idx) is None
```

### Step 2: Assign idx = value

```python
idx = [2, 30]
```

**Verification:**
```python
assert s.get(idx) is None
```

### Step 3: Assign idx = value

```python
idx = [2, np.nan]
```

**Verification:**
```python
assert s.get(idx) is None
```

### Step 4: Assign idx = value

```python
idx = [20, 30]
```

**Verification:**
```python
assert s.get(idx) is None
```

### Step 5: Assign idx = value

```python
idx = [np.nan, np.nan]
```

**Verification:**
```python
assert s.get(idx) is None
```


## Complete Example

```python
# Setup
# Fixtures: float_numpy_dtype

# Workflow
s = Index(range(10), dtype=float_numpy_dtype).to_series()
idx = [2, 30]
assert s.get(idx) is None
idx = [2, np.nan]
assert s.get(idx) is None
idx = [20, 30]
assert s.get(idx) is None
idx = [np.nan, np.nan]
assert s.get(idx) is None
```

## Next Steps


---

*Source: test_get.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*