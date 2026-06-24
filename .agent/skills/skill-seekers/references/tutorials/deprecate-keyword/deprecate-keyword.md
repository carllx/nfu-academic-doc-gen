# How To: Deprecate Keyword

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test deprecate keyword

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.util._decorators`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: key
```

## Step-by-Step Guide

### Step 1: Assign x = 9

```python
x = 9
```

**Verification:**
```python
assert _f4(**{key: x}) == expected
```

### Step 2: Assign klass = FutureWarning

```python
klass = FutureWarning
```

### Step 3: Assign expected = value

```python
expected = (x, True)
```

### Step 4: Assign klass = None

```python
klass = None
```

### Step 5: Assign expected = value

```python
expected = (True, x)
```

**Verification:**
```python
assert _f4(**{key: x}) == expected
```


## Complete Example

```python
# Setup
# Fixtures: key

# Workflow
x = 9
if key == 'old':
    klass = FutureWarning
    expected = (x, True)
else:
    klass = None
    expected = (True, x)
with tm.assert_produces_warning(klass):
    assert _f4(**{key: x}) == expected
```

## Next Steps


---

*Source: test_deprecate_kwarg.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*