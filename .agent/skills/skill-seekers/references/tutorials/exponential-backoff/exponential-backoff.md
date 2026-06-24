# How To: Exponential Backoff

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exponential backoff

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert len(df._mgr.blocks[0].refs.referenced_blocks) == 491
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert len(df._mgr.blocks[0].refs.referenced_blocks) == 531
```

### Step 3: Assign dfs = value

```python
dfs = [df.copy(deep=False) for i in range(510)]
```

**Verification:**
```python
assert df._mgr.blocks[0].refs.clear_counter == 1000
```

### Step 4: Assign dfs = value

```python
dfs = dfs[:300]
```

**Verification:**
```python
assert df._mgr.blocks[0].refs.clear_counter == 1000
```

### Step 5: Call df.copy()

```python
df.copy(deep=False)
```

**Verification:**
```python
assert df._mgr.blocks[0].refs.clear_counter == 500
```

### Step 6: Call df.copy()

```python
df.copy(deep=False)
```

### Step 7: Call df.copy()

```python
df.copy(deep=False)
```

### Step 8: Call df.copy()

```python
df.copy(deep=False)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3]})
for i in range(490):
    df.copy(deep=False)
assert len(df._mgr.blocks[0].refs.referenced_blocks) == 491
df = DataFrame({'a': [1, 2, 3]})
dfs = [df.copy(deep=False) for i in range(510)]
for i in range(20):
    df.copy(deep=False)
assert len(df._mgr.blocks[0].refs.referenced_blocks) == 531
assert df._mgr.blocks[0].refs.clear_counter == 1000
for i in range(500):
    df.copy(deep=False)
assert df._mgr.blocks[0].refs.clear_counter == 1000
dfs = dfs[:300]
for i in range(500):
    df.copy(deep=False)
assert df._mgr.blocks[0].refs.clear_counter == 500
```

## Next Steps


---

*Source: test_internals.py:127 | Complexity: Advanced | Last updated: 2026-06-02*