# How To: Identity Hashtable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test identity hashtable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `numpy._core._multiarray_tests`

**Setup Required:**
```python
# Fixtures: key_length, length
```

## Step-by-Step Guide

### Step 1: Assign pool = value

```python
pool = [object() for i in range(20)]
```

**Verification:**
```python
assert res is expected
```

### Step 2: Assign keys_vals = value

```python
keys_vals = []
```

### Step 3: Assign dictionary = dict(...)

```python
dictionary = dict(keys_vals)
```

### Step 4: Call keys_vals.append()

```python
keys_vals.append(random.choice(keys_vals))
```

### Step 5: Assign expected = value

```python
expected = dictionary[keys_vals[-1][0]]
```

### Step 6: Assign res = identityhash_tester(...)

```python
res = identityhash_tester(key_length, keys_vals, replace=True)
```

**Verification:**
```python
assert res is expected
```

### Step 7: Assign new_key = value

```python
new_key = (keys_vals[1][0], object())
```

### Step 8: Assign unknown = new_key

```python
keys_vals[0] = new_key
```

### Step 9: Assign keys = tuple(...)

```python
keys = tuple(random.choices(pool, k=key_length))
```

### Step 10: Call keys_vals.append()

```python
keys_vals.append((keys, random.choice(pool)))
```

### Step 11: Call identityhash_tester()

```python
identityhash_tester(key_length, keys_vals)
```


## Complete Example

```python
# Setup
# Fixtures: key_length, length

# Workflow
pool = [object() for i in range(20)]
keys_vals = []
for i in range(length):
    keys = tuple(random.choices(pool, k=key_length))
    keys_vals.append((keys, random.choice(pool)))
dictionary = dict(keys_vals)
keys_vals.append(random.choice(keys_vals))
expected = dictionary[keys_vals[-1][0]]
res = identityhash_tester(key_length, keys_vals, replace=True)
assert res is expected
if length == 1:
    return
new_key = (keys_vals[1][0], object())
keys_vals[0] = new_key
with pytest.raises(RuntimeError):
    identityhash_tester(key_length, keys_vals)
```

## Next Steps


---

*Source: test_hashtable.py:10 | Complexity: Advanced | Last updated: 2026-06-02*