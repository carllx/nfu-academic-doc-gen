# How To: Map Locations

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map locations

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections.abc`
- `contextlib`
- `re`
- `struct`
- `tracemalloc`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: table_type, dtype, writable
```

## Step-by-Step Guide

### Step 1: Assign N = 8

```python
N = 8
```

**Verification:**
```python
assert table.get_item(keys[i]) == i
```

### Step 2: Assign table = table_type(...)

```python
table = table_type()
```

### Step 3: Assign keys = unknown.astype(...)

```python
keys = (np.arange(N) + N).astype(dtype)
```

### Step 4: Assign keys.flags.writeable = writable

```python
keys.flags.writeable = writable
```

### Step 5: Call table.map_locations()

```python
table.map_locations(keys)
```

**Verification:**
```python
assert table.get_item(keys[i]) == i
```


## Complete Example

```python
# Setup
# Fixtures: table_type, dtype, writable

# Workflow
N = 8
table = table_type()
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys)
for i in range(N):
    assert table.get_item(keys[i]) == i
```

## Next Steps


---

*Source: test_hashtable.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*