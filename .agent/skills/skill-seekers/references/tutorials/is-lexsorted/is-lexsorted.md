# How To: Is Lexsorted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is lexsorted

## Prerequisites

**Required Modules:**
- `pandas`


## Step-by-Step Guide

### Step 1: Assign levels = value

```python
levels = [[0, 1], [0, 1, 2]]
```

**Verification:**
```python
assert index._is_lexsorted()
```

### Step 2: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
```

**Verification:**
```python
assert not index._is_lexsorted()
```

### Step 3: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 2, 1]])
```

**Verification:**
```python
assert not index._is_lexsorted()
```

### Step 4: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 1, 0, 1, 1], [0, 1, 0, 2, 2, 1]])
```

**Verification:**
```python
assert index._lexsort_depth == 0
```


## Complete Example

```python
# Workflow
levels = [[0, 1], [0, 1, 2]]
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])
assert index._is_lexsorted()
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 2, 1]])
assert not index._is_lexsorted()
index = MultiIndex(levels=levels, codes=[[0, 0, 1, 0, 1, 1], [0, 1, 0, 2, 2, 1]])
assert not index._is_lexsorted()
assert index._lexsort_depth == 0
```

## Next Steps


---

*Source: test_lexsort.py:5 | Complexity: Intermediate | Last updated: 2026-06-02*