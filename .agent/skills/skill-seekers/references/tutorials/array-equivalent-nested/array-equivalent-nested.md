# How To: Array Equivalent Nested

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array equivalent nested

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: strict_nan
```

## Step-by-Step Guide

### Step 1: Assign left = np.array(...)

```python
left = np.array([np.array([50, 70, 90]), np.array([20, 30])], dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 2: Assign right = np.array(...)

```python
right = np.array([np.array([50, 70, 90]), np.array([20, 30])], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 3: Assign left = np.empty(...)

```python
left = np.empty(2, dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 4: Assign unknown = value

```python
left[:] = [np.array([50, 70, 90]), np.array([20, 30, 40])]
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 5: Assign right = np.empty(...)

```python
right = np.empty(2, dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 6: Assign unknown = value

```python
right[:] = [np.array([50, 70, 90]), np.array([20, 30, 40])]
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 7: Assign left = np.array(...)

```python
left = np.array([np.array([50, 50, 50]), np.array([40, 40])], dtype=object)
```

### Step 8: Assign right = np.array(...)

```python
right = np.array([50, 40])
```

**Verification:**
```python
assert not array_equivalent(left, right, strict_nan=strict_nan)
```


## Complete Example

```python
# Setup
# Fixtures: strict_nan

# Workflow
left = np.array([np.array([50, 70, 90]), np.array([20, 30])], dtype=object)
right = np.array([np.array([50, 70, 90]), np.array([20, 30])], dtype=object)
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
left = np.empty(2, dtype=object)
left[:] = [np.array([50, 70, 90]), np.array([20, 30, 40])]
right = np.empty(2, dtype=object)
right[:] = [np.array([50, 70, 90]), np.array([20, 30, 40])]
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
left = np.array([np.array([50, 50, 50]), np.array([40, 40])], dtype=object)
right = np.array([50, 40])
assert not array_equivalent(left, right, strict_nan=strict_nan)
```

## Next Steps


---

*Source: test_missing.py:577 | Complexity: Advanced | Last updated: 2026-06-02*