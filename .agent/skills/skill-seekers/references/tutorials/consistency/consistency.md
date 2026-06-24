# How To: Consistency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test consistency

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign major_axis = list(...)

```python
major_axis = list(range(70000))
```

**Verification:**
```python
assert index.is_unique is False
```

### Step 2: Assign minor_axis = list(...)

```python
minor_axis = list(range(10))
```

### Step 3: Assign major_codes = np.arange(...)

```python
major_codes = np.arange(70000)
```

### Step 4: Assign minor_codes = np.repeat(...)

```python
minor_codes = np.repeat(range(10), 7000)
```

### Step 5: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
```

### Step 6: Assign major_codes = np.array(...)

```python
major_codes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 3])
```

### Step 7: Assign minor_codes = np.array(...)

```python
minor_codes = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1])
```

### Step 8: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
```

**Verification:**
```python
assert index.is_unique is False
```


## Complete Example

```python
# Workflow
major_axis = list(range(70000))
minor_axis = list(range(10))
major_codes = np.arange(70000)
minor_codes = np.repeat(range(10), 7000)
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
major_codes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 1, 0, 1, 0, 1])
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
assert index.is_unique is False
```

## Next Steps


---

*Source: test_integrity.py:104 | Complexity: Advanced | Last updated: 2026-06-02*