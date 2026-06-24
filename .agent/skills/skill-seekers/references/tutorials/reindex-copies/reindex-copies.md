# How To: Reindex Copies

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex copies

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert not np.shares_memory(result[0]._values, df[0]._values)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((N * 10, N)))
```

**Verification:**
```python
assert not np.shares_memory(result2[0]._values, df[0]._values)
```

### Step 3: Assign cols = np.arange(...)

```python
cols = np.arange(N)
```

### Step 4: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(cols)
```

### Step 5: Assign result = df.reindex(...)

```python
result = df.reindex(columns=cols, copy=True)
```

**Verification:**
```python
assert not np.shares_memory(result[0]._values, df[0]._values)
```

### Step 6: Assign result2 = df.reindex(...)

```python
result2 = df.reindex(columns=cols, index=df.index, copy=True)
```

**Verification:**
```python
assert not np.shares_memory(result2[0]._values, df[0]._values)
```


## Complete Example

```python
# Workflow
N = 10
df = DataFrame(np.random.default_rng(2).standard_normal((N * 10, N)))
cols = np.arange(N)
np.random.default_rng(2).shuffle(cols)
result = df.reindex(columns=cols, copy=True)
assert not np.shares_memory(result[0]._values, df[0]._values)
result2 = df.reindex(columns=cols, index=df.index, copy=True)
assert not np.shares_memory(result2[0]._values, df[0]._values)
```

## Next Steps


---

*Source: test_reindex.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*