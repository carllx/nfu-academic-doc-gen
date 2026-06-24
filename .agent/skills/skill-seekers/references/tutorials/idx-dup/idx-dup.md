# How To: Idx Dup

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: idx dup

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign major_axis = Index(...)

```python
major_axis = Index(['foo', 'bar', 'baz', 'qux'])
```

### Step 2: Assign minor_axis = Index(...)

```python
minor_axis = Index(['one', 'two'])
```

### Step 3: Assign major_codes = np.array(...)

```python
major_codes = np.array([0, 0, 1, 0, 1, 1])
```

### Step 4: Assign minor_codes = np.array(...)

```python
minor_codes = np.array([0, 1, 0, 1, 0, 1])
```

### Step 5: Assign index_names = value

```python
index_names = ['first', 'second']
```

### Step 6: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes], names=index_names, verify_integrity=False)
```


## Complete Example

```python
# Workflow
major_axis = Index(['foo', 'bar', 'baz', 'qux'])
minor_axis = Index(['one', 'two'])
major_codes = np.array([0, 0, 1, 0, 1, 1])
minor_codes = np.array([0, 1, 0, 1, 0, 1])
index_names = ['first', 'second']
mi = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes], names=index_names, verify_integrity=False)
return mi
```

## Next Steps


---

*Source: test_duplicates.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*