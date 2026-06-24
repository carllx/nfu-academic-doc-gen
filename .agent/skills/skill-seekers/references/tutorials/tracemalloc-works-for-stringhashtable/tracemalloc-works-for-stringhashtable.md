# How To: Tracemalloc Works For Stringhashtable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tracemalloc works for StringHashTable

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign N = 1000

```python
N = 1000
```

**Verification:**
```python
assert used == my_size
```

### Step 2: Assign keys = np.arange.astype.astype(...)

```python
keys = np.arange(N).astype(np.str_).astype(np.object_)
```

**Verification:**
```python
assert get_allocated_khash_memory() == 0
```

### Step 3: Assign table = ht.StringHashTable(...)

```python
table = ht.StringHashTable()
```

### Step 4: Call table.map_locations()

```python
table.map_locations(keys)
```

### Step 5: Assign used = get_allocated_khash_memory(...)

```python
used = get_allocated_khash_memory()
```

### Step 6: Assign my_size = table.sizeof(...)

```python
my_size = table.sizeof()
```

**Verification:**
```python
assert used == my_size
```


## Complete Example

```python
# Workflow
N = 1000
keys = np.arange(N).astype(np.str_).astype(np.object_)
with activated_tracemalloc():
    table = ht.StringHashTable()
    table.map_locations(keys)
    used = get_allocated_khash_memory()
    my_size = table.sizeof()
    assert used == my_size
    del table
    assert get_allocated_khash_memory() == 0
```

## Next Steps


---

*Source: test_hashtable.py:462 | Complexity: Intermediate | Last updated: 2026-06-02*