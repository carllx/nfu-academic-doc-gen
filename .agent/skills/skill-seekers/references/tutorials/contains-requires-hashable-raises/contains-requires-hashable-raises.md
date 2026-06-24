# How To: Contains Requires Hashable Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains requires hashable raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `enum`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign msg = "unhashable type: 'list'"

```python
msg = "unhashable type: 'list'"
```

### Step 2: Assign msg = unknown.join(...)

```python
msg = '|'.join(["unhashable type: 'dict'", 'must be real number, not dict', 'an integer is required', '\\{\\}', f"pandas\\._libs\\.interval\\.IntervalTree' is not {container_or_iterable}"])
```

### Step 3: [] in index

```python
[] in index
```

### Step 4: Assign container_or_iterable = 'a container or iterable'

```python
container_or_iterable = 'a container or iterable'
```

### Step 5: Assign container_or_iterable = 'iterable'

```python
container_or_iterable = 'iterable'
```

### Step 6: {} in index._engine

```python
{} in index._engine
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
if isinstance(index, MultiIndex):
    return
msg = "unhashable type: 'list'"
with pytest.raises(TypeError, match=msg):
    [] in index
if PY314:
    container_or_iterable = 'a container or iterable'
else:
    container_or_iterable = 'iterable'
msg = '|'.join(["unhashable type: 'dict'", 'must be real number, not dict', 'an integer is required', '\\{\\}', f"pandas\\._libs\\.interval\\.IntervalTree' is not {container_or_iterable}"])
with pytest.raises(TypeError, match=msg):
    {} in index._engine
```

## Next Steps


---

*Source: test_indexing.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*