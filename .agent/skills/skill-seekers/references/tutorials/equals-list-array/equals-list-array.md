# How To: Equals List Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test equals list array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `copy`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: val
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2])
```

**Verification:**
```python
assert s1.equals(s2)
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series([arr, arr])
```

**Verification:**
```python
assert not s1.equals(s2)
```

### Step 3: Assign s2 = s1.copy(...)

```python
s2 = s1.copy()
```

**Verification:**
```python
assert s1.equals(s2)
```

### Step 4: Assign unknown = val

```python
s1[1] = val
```

### Step 5: Assign cm = value

```python
cm = tm.assert_produces_warning(FutureWarning, check_stacklevel=False) if isinstance(val, str) and (not np_version_gte1p25) else nullcontext()
```

**Verification:**
```python
assert not s1.equals(s2)
```


## Complete Example

```python
# Setup
# Fixtures: val

# Workflow
arr = np.array([1, 2])
s1 = Series([arr, arr])
s2 = s1.copy()
assert s1.equals(s2)
s1[1] = val
cm = tm.assert_produces_warning(FutureWarning, check_stacklevel=False) if isinstance(val, str) and (not np_version_gte1p25) else nullcontext()
with cm:
    assert not s1.equals(s2)
```

## Next Steps


---

*Source: test_equals.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*