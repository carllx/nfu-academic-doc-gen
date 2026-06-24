# How To: Binary Ufunc Drops Series Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test binary ufunc drops series name

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `re`
- `string`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: ufunc, sparse, arrays_for_binary_ufunc
```

## Step-by-Step Guide

### Step 1: Assign unknown = arrays_for_binary_ufunc

```python
a1, a2 = arrays_for_binary_ufunc
```

**Verification:**
```python
assert result.name is None
```

### Step 2: Assign s1 = pd.Series(...)

```python
s1 = pd.Series(a1, name='a')
```

### Step 3: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(a2, name='b')
```

### Step 4: Assign result = ufunc(...)

```python
result = ufunc(s1, s2)
```

**Verification:**
```python
assert result.name is None
```


## Complete Example

```python
# Setup
# Fixtures: ufunc, sparse, arrays_for_binary_ufunc

# Workflow
a1, a2 = arrays_for_binary_ufunc
s1 = pd.Series(a1, name='a')
s2 = pd.Series(a2, name='b')
result = ufunc(s1, s2)
assert result.name is None
```

## Next Steps


---

*Source: test_ufunc.py:225 | Complexity: Intermediate | Last updated: 2026-06-02*