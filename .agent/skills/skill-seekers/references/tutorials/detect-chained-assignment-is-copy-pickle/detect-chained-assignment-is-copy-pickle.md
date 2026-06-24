# How To: Detect Chained Assignment Is Copy Pickle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment is copy pickle

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2]})
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 2: Call df.to_pickle()

```python
df.to_pickle(path)
```

### Step 3: Assign df2 = pd.read_pickle(...)

```python
df2 = pd.read_pickle(path)
```

### Step 4: Assign unknown = value

```python
df2['B'] = df2['A']
```

### Step 5: Assign unknown = value

```python
df2['B'] = df2['A']
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2]})
assert df._is_copy is None
with tm.ensure_clean('__tmp__pickle') as path:
    df.to_pickle(path)
    df2 = pd.read_pickle(path)
    df2['B'] = df2['A']
    df2['B'] = df2['A']
```

## Next Steps


---

*Source: test_chaining_and_caching.py:334 | Complexity: Intermediate | Last updated: 2026-06-02*