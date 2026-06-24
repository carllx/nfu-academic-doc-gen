# How To: Map Locations Mask

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map locations mask

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

### Step 1: Assign N = 3

```python
N = 3
```

**Verification:**
```python
assert table.get_item(keys[i]) == i
```

### Step 2: Assign table = table_type(...)

```python
table = table_type(uses_mask=True)
```

**Verification:**
```python
assert table.get_na() == 2
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
table.map_locations(keys, np.array([False, False, True]))
```

**Verification:**
```python
assert table.get_na() == 2
```

### Step 6: Call pytest.skip()

```python
pytest.skip('Mask not supported for object')
```

**Verification:**
```python
assert table.get_item(keys[i]) == i
```

### Step 7: Call table.get_item()

```python
table.get_item(keys[N - 1])
```


## Complete Example

```python
# Setup
# Fixtures: table_type, dtype, writable

# Workflow
if table_type == ht.PyObjectHashTable:
    pytest.skip('Mask not supported for object')
N = 3
table = table_type(uses_mask=True)
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys, np.array([False, False, True]))
for i in range(N - 1):
    assert table.get_item(keys[i]) == i
with pytest.raises(KeyError, match=re.escape(str(keys[N - 1]))):
    table.get_item(keys[N - 1])
assert table.get_na() == 2
```

## Next Steps


---

*Source: test_hashtable.py:148 | Complexity: Intermediate | Last updated: 2026-06-02*