# How To: No Reallocation Stringhashtable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test no reallocation StringHashTable

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
# Fixtures: N
```

## Step-by-Step Guide

### Step 1: Assign keys = np.arange.astype.astype(...)

```python
keys = np.arange(N).astype(np.str_).astype(np.object_)
```

**Verification:**
```python
assert n_buckets_start == n_buckets_end
```

### Step 2: Assign preallocated_table = ht.StringHashTable(...)

```python
preallocated_table = ht.StringHashTable(N)
```

**Verification:**
```python
assert n_buckets_start == clean_table.get_state()['n_buckets']
```

### Step 3: Assign n_buckets_start = value

```python
n_buckets_start = preallocated_table.get_state()['n_buckets']
```

### Step 4: Call preallocated_table.map_locations()

```python
preallocated_table.map_locations(keys)
```

### Step 5: Assign n_buckets_end = value

```python
n_buckets_end = preallocated_table.get_state()['n_buckets']
```

**Verification:**
```python
assert n_buckets_start == n_buckets_end
```

### Step 6: Assign clean_table = ht.StringHashTable(...)

```python
clean_table = ht.StringHashTable()
```

### Step 7: Call clean_table.map_locations()

```python
clean_table.map_locations(keys)
```

**Verification:**
```python
assert n_buckets_start == clean_table.get_state()['n_buckets']
```


## Complete Example

```python
# Setup
# Fixtures: N

# Workflow
keys = np.arange(N).astype(np.str_).astype(np.object_)
preallocated_table = ht.StringHashTable(N)
n_buckets_start = preallocated_table.get_state()['n_buckets']
preallocated_table.map_locations(keys)
n_buckets_end = preallocated_table.get_state()['n_buckets']
assert n_buckets_start == n_buckets_end
clean_table = ht.StringHashTable()
clean_table.map_locations(keys)
assert n_buckets_start == clean_table.get_state()['n_buckets']
```

## Next Steps


---

*Source: test_hashtable.py:486 | Complexity: Intermediate | Last updated: 2026-06-02*