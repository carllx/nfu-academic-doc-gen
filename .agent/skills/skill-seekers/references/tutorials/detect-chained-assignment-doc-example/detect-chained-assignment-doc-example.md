# How To: Detect Chained Assignment Doc Example

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment doc example

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'], 'c': Series(range(7), dtype='int64')})
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 2: Assign indexer = df.a.str.startswith(...)

```python
indexer = df.a.str.startswith('o')
```

### Step 3: Assign unknown = 42

```python
df[indexer]['c'] = 42
```

### Step 4: Assign unknown = 42

```python
df[indexer]['c'] = 42
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'], 'c': Series(range(7), dtype='int64')})
assert df._is_copy is None
indexer = df.a.str.startswith('o')
if using_copy_on_write or warn_copy_on_write:
    with tm.raises_chained_assignment_error():
        df[indexer]['c'] = 42
else:
    with pytest.raises(SettingWithCopyError, match=msg):
        df[indexer]['c'] = 42
```

## Next Steps


---

*Source: test_chaining_and_caching.py:278 | Complexity: Intermediate | Last updated: 2026-06-02*