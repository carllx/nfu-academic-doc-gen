# How To: Categorical Equality

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical equality

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: ordered1, ordered2
```

## Step-by-Step Guide

### Step 1: Assign c1 = CategoricalDtype(...)

```python
c1 = CategoricalDtype(list('abc'), ordered1)
```

**Verification:**
```python
assert result is expected
```

### Step 2: Assign c2 = CategoricalDtype(...)

```python
c2 = CategoricalDtype(list('abc'), ordered2)
```

**Verification:**
```python
assert result is expected
```

### Step 3: Assign result = value

```python
result = c1 == c2
```

**Verification:**
```python
assert c1 != c2
```

### Step 4: Assign expected = value

```python
expected = bool(ordered1) is bool(ordered2)
```

**Verification:**
```python
assert c1 != c2
```

### Step 5: Assign c1 = CategoricalDtype(...)

```python
c1 = CategoricalDtype(list('abc'), ordered1)
```

**Verification:**
```python
assert c2 != c1
```

### Step 6: Assign c2 = CategoricalDtype(...)

```python
c2 = CategoricalDtype(list('cab'), ordered2)
```

**Verification:**
```python
assert c2 == c3
```

### Step 7: Assign result = value

```python
result = c1 == c2
```

### Step 8: Assign expected = value

```python
expected = bool(ordered1) is False and bool(ordered2) is False
```

**Verification:**
```python
assert result is expected
```

### Step 9: Assign c2 = CategoricalDtype(...)

```python
c2 = CategoricalDtype([1, 2, 3], ordered2)
```

**Verification:**
```python
assert c1 != c2
```

### Step 10: Assign c1 = CategoricalDtype(...)

```python
c1 = CategoricalDtype(list('abc'), ordered1)
```

### Step 11: Assign c2 = CategoricalDtype(...)

```python
c2 = CategoricalDtype(None, ordered2)
```

### Step 12: Assign c3 = CategoricalDtype(...)

```python
c3 = CategoricalDtype(None, ordered1)
```

**Verification:**
```python
assert c1 != c2
```


## Complete Example

```python
# Setup
# Fixtures: ordered1, ordered2

# Workflow
c1 = CategoricalDtype(list('abc'), ordered1)
c2 = CategoricalDtype(list('abc'), ordered2)
result = c1 == c2
expected = bool(ordered1) is bool(ordered2)
assert result is expected
c1 = CategoricalDtype(list('abc'), ordered1)
c2 = CategoricalDtype(list('cab'), ordered2)
result = c1 == c2
expected = bool(ordered1) is False and bool(ordered2) is False
assert result is expected
c2 = CategoricalDtype([1, 2, 3], ordered2)
assert c1 != c2
c1 = CategoricalDtype(list('abc'), ordered1)
c2 = CategoricalDtype(None, ordered2)
c3 = CategoricalDtype(None, ordered1)
assert c1 != c2
assert c2 != c1
assert c2 == c3
```

## Next Steps


---

*Source: test_dtypes.py:964 | Complexity: Advanced | Last updated: 2026-06-02*