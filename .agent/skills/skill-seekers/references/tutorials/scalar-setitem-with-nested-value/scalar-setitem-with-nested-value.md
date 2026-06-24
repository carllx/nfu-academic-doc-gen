# How To: Scalar Setitem With Nested Value

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar setitem with nested value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`

**Setup Required:**
```python
# Fixtures: value
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3]})
```

### Step 2: Assign msg = unknown.join(...)

```python
msg = '|'.join(['Must have equal len keys and value', 'setting an array element with a sequence'])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': np.array([1, 'a', 'b'], dtype=object)})
```

### Step 4: Assign unknown = value

```python
df.loc[0, 'B'] = value
```

### Step 5: Assign unknown = value

```python
df.loc[0, 'B'] = value
```


## Complete Example

```python
# Setup
# Fixtures: value

# Workflow
df = DataFrame({'A': [1, 2, 3]})
msg = '|'.join(['Must have equal len keys and value', 'setting an array element with a sequence'])
with pytest.raises(ValueError, match=msg):
    df.loc[0, 'B'] = value
df = DataFrame({'A': [1, 2, 3], 'B': np.array([1, 'a', 'b'], dtype=object)})
with pytest.raises(ValueError, match='Must have equal len keys and value'):
    df.loc[0, 'B'] = value
```

## Next Steps


---

*Source: test_indexing.py:1055 | Complexity: Intermediate | Last updated: 2026-06-02*