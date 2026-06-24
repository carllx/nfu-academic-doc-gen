# How To: Set Flags

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set flags

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `inspect`
- `pydoc`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._config.config`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: allows_duplicate_labels, frame_or_series, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign obj = DataFrame(...)

```python
obj = DataFrame({'A': [1, 2]})
```

**Verification:**
```python
assert result.flags.allows_duplicate_labels is True
```

### Step 2: Assign key = value

```python
key = (0, 0)
```

**Verification:**
```python
assert result.flags.allows_duplicate_labels is allows_duplicate_labels
```

### Step 3: Assign result = obj.set_flags(...)

```python
result = obj.set_flags(allows_duplicate_labels=allows_duplicate_labels)
```

**Verification:**
```python
assert obj is not result
```

### Step 4: Assign result = obj.set_flags(...)

```python
result = obj.set_flags(copy=True, allows_duplicate_labels=allows_duplicate_labels)
```

**Verification:**
```python
assert obj.flags.allows_duplicate_labels is True
```

### Step 5: Assign unknown = 10

```python
result.iloc[key] = 10
```

**Verification:**
```python
assert np.may_share_memory(obj.values, result.values)
```

### Step 6: Assign obj = value

```python
obj = obj['A']
```

**Verification:**
```python
assert np.may_share_memory(obj['A'].values, result['A'].values)
```

### Step 7: Assign key = 0

```python
key = 0
```

**Verification:**
```python
assert obj.iloc[key] == 1
```

### Step 8: Assign unknown = 0

```python
result.iloc[key] = 0
```

**Verification:**
```python
assert obj.iloc[key] == 0
```

### Step 9: Assign unknown = 1

```python
result.iloc[key] = 1
```

**Verification:**
```python
assert obj.iloc[key] == 1
```


## Complete Example

```python
# Setup
# Fixtures: allows_duplicate_labels, frame_or_series, using_copy_on_write, warn_copy_on_write

# Workflow
obj = DataFrame({'A': [1, 2]})
key = (0, 0)
if frame_or_series is Series:
    obj = obj['A']
    key = 0
result = obj.set_flags(allows_duplicate_labels=allows_duplicate_labels)
if allows_duplicate_labels is None:
    assert result.flags.allows_duplicate_labels is True
else:
    assert result.flags.allows_duplicate_labels is allows_duplicate_labels
assert obj is not result
assert obj.flags.allows_duplicate_labels is True
if frame_or_series is Series:
    assert np.may_share_memory(obj.values, result.values)
else:
    assert np.may_share_memory(obj['A'].values, result['A'].values)
with tm.assert_cow_warning(warn_copy_on_write):
    result.iloc[key] = 0
if using_copy_on_write:
    assert obj.iloc[key] == 1
else:
    assert obj.iloc[key] == 0
    with tm.assert_cow_warning(warn_copy_on_write):
        result.iloc[key] = 1
result = obj.set_flags(copy=True, allows_duplicate_labels=allows_duplicate_labels)
result.iloc[key] = 10
assert obj.iloc[key] == 1
```

## Next Steps


---

*Source: test_api.py:328 | Complexity: Advanced | Last updated: 2026-06-02*