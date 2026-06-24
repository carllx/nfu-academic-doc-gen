# How To: Equals Numeric

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals numeric

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
assert idx.equals(idx)
```

### Step 2: Assign idx = index_cls(...)

```python
idx = index_cls([1.0, 2.0])
```

**Verification:**
```python
assert idx.identical(idx)
```

### Step 3: Assign idx2 = index_cls(...)

```python
idx2 = index_cls([1.0, 2.0])
```

**Verification:**
```python
assert idx.equals(idx2)
```

### Step 4: Assign idx = index_cls(...)

```python
idx = index_cls([1.0, np.nan])
```

**Verification:**
```python
assert idx.equals(idx)
```

### Step 5: Assign idx2 = index_cls(...)

```python
idx2 = index_cls([1.0, np.nan])
```

**Verification:**
```python
assert idx.identical(idx)
```


## Complete Example

```python
# Workflow
index_cls = Index
idx = index_cls([1.0, 2.0])
assert idx.equals(idx)
assert idx.identical(idx)
idx2 = index_cls([1.0, 2.0])
assert idx.equals(idx2)
idx = index_cls([1.0, np.nan])
assert idx.equals(idx)
assert idx.identical(idx)
idx2 = index_cls([1.0, np.nan])
assert idx.equals(idx2)
```

## Next Steps


---

*Source: test_numeric.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*