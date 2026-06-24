# How To: Array Equivalent Nested List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array equivalent nested list

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
left = np.array([[50, 70, 90], [20, 30]], dtype=object)
```

**Verification:**
```python
assert array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 2: Assign right = np.array(...)

```python
right = np.array([[50, 70, 90], [20, 30]], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
```

### Step 3: Assign left = np.array(...)

```python
left = np.array([[50, 50, 50], [40, 40]], dtype=object)
```

**Verification:**
```python
assert not array_equivalent(left, right, strict_nan=strict_nan)
```

### Step 4: Assign right = np.array(...)

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
left = np.array([[50, 70, 90], [20, 30]], dtype=object)
right = np.array([[50, 70, 90], [20, 30]], dtype=object)
assert array_equivalent(left, right, strict_nan=strict_nan)
assert not array_equivalent(left, right[::-1], strict_nan=strict_nan)
left = np.array([[50, 50, 50], [40, 40]], dtype=object)
right = np.array([50, 40])
assert not array_equivalent(left, right, strict_nan=strict_nan)
```

## Next Steps


---

*Source: test_missing.py:625 | Complexity: Intermediate | Last updated: 2026-06-02*