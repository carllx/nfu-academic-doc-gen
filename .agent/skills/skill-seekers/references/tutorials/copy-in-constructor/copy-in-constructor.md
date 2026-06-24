# How To: Copy In Constructor

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy in constructor

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign levels = np.array(...)

```python
levels = np.array(['a', 'b', 'c'])
```

**Verification:**
```python
assert mi.codes[0][0] == val
```

### Step 2: Assign codes = np.array(...)

```python
codes = np.array([1, 1, 2, 0, 0, 1, 1])
```

**Verification:**
```python
assert mi.codes[0][0] == val
```

### Step 3: Assign val = value

```python
val = codes[0]
```

**Verification:**
```python
assert mi.levels[0][0] == val
```

### Step 4: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=[levels, levels], codes=[codes, codes], copy=True)
```

**Verification:**
```python
assert mi.codes[0][0] == val
```

### Step 5: Assign unknown = 15

```python
codes[0] = 15
```

**Verification:**
```python
assert mi.codes[0][0] == val
```

### Step 6: Assign val = value

```python
val = levels[0]
```

### Step 7: Assign unknown = 'PANDA'

```python
levels[0] = 'PANDA'
```

**Verification:**
```python
assert mi.levels[0][0] == val
```


## Complete Example

```python
# Workflow
levels = np.array(['a', 'b', 'c'])
codes = np.array([1, 1, 2, 0, 0, 1, 1])
val = codes[0]
mi = MultiIndex(levels=[levels, levels], codes=[codes, codes], copy=True)
assert mi.codes[0][0] == val
codes[0] = 15
assert mi.codes[0][0] == val
val = levels[0]
levels[0] = 'PANDA'
assert mi.levels[0][0] == val
```

## Next Steps


---

*Source: test_constructors.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*