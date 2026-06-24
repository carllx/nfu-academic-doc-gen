# How To: Setitem Same Ordered Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test setitem same ordered raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign target = Categorical(...)

```python
target = Categorical(['a', 'b'], categories=['a', 'b'], ordered=True)
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False])
```

### Step 3: Assign msg = 'Cannot set a Categorical with another, without identical categories'

```python
msg = 'Cannot set a Categorical with another, without identical categories'
```

### Step 4: Assign unknown = value

```python
target[mask] = other[mask]
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
target = Categorical(['a', 'b'], categories=['a', 'b'], ordered=True)
mask = np.array([True, False])
msg = 'Cannot set a Categorical with another, without identical categories'
with pytest.raises(TypeError, match=msg):
    target[mask] = other[mask]
```

## Next Steps


---

*Source: test_indexing.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*