# How To: Is Dict Like Duck Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test is dict like duck type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: has_keys, has_getitem, has_contains
```

## Step-by-Step Guide

### Step 1: Assign d = DictLike(...)

```python
d = DictLike({1: 2})
```

**Verification:**
```python
assert result is expected
```

### Step 2: Assign result = inference.is_dict_like(...)

```python
result = inference.is_dict_like(d)
```

### Step 3: Assign expected = value

```python
expected = has_keys and has_getitem and has_contains
```

**Verification:**
```python
assert result is expected
```

### Step 4: Assign self.d = d

```python
self.d = d
```


## Complete Example

```python
# Setup
# Fixtures: has_keys, has_getitem, has_contains

# Workflow
class DictLike:

    def __init__(self, d) -> None:
        self.d = d
    if has_keys:

        def keys(self):
            return self.d.keys()
    if has_getitem:

        def __getitem__(self, key):
            return self.d.__getitem__(key)
    if has_contains:

        def __contains__(self, key) -> bool:
            return self.d.__contains__(key)
d = DictLike({1: 2})
result = inference.is_dict_like(d)
expected = has_keys and has_getitem and has_contains
assert result is expected
```

## Next Steps


---

*Source: test_inference.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*