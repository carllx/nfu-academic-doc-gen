# How To: Lexsort Depth

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lexsort depth

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
assert index._lexsort_depth == 2
```

### Step 2: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]], sortorder=2)
```

**Verification:**
```python
assert index._lexsort_depth == 1
```

### Step 3: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 2, 1]], sortorder=1)
```

**Verification:**
```python
assert index._lexsort_depth == 0
```

### Step 4: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=levels, codes=[[0, 0, 1, 0, 1, 1], [0, 1, 0, 2, 2, 1]], sortorder=0)
```

**Verification:**
```python
assert index._lexsort_depth == 0
```


## Complete Example

```python
# Workflow
levels = [[0, 1], [0, 1, 2]]
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]], sortorder=2)
assert index._lexsort_depth == 2
index = MultiIndex(levels=levels, codes=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 2, 1]], sortorder=1)
assert index._lexsort_depth == 1
index = MultiIndex(levels=levels, codes=[[0, 0, 1, 0, 1, 1], [0, 1, 0, 2, 2, 1]], sortorder=0)
assert index._lexsort_depth == 0
```

## Next Steps


---

*Source: test_lexsort.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*