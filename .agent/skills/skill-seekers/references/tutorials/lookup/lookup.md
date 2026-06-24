# How To: Lookup

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lookup

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

### Step 6: Assign result = table.lookup(...)

```python
result = table.lookup(keys)
```

### Step 7: Assign expected = np.arange(...)

```python
expected = np.arange(N)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result.astype(np.int64), expected.astype(np.int64))
```


## Complete Example

```python
# Setup
# Fixtures: table_type, dtype, writable

# Workflow
N = 3
table = table_type()
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys)
result = table.lookup(keys)
expected = np.arange(N)
tm.assert_numpy_array_equal(result.astype(np.int64), expected.astype(np.int64))
```

## Next Steps


---

*Source: test_hashtable.py:164 | Complexity: Advanced | Last updated: 2026-06-02*