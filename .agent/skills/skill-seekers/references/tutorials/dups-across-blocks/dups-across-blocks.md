# How To: Dups Across Blocks

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dups across blocks

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign df_float = DataFrame(...)

```python
df_float = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), dtype='float64')
```

**Verification:**
```python
assert len(df._mgr.blknos) == len(df.columns)
```

### Step 2: Assign df_int = DataFrame(...)

```python
df_int = DataFrame(np.random.default_rng(2).standard_normal((10, 3)).astype('int64'))
```

**Verification:**
```python
assert len(df._mgr.blklocs) == len(df.columns)
```

### Step 3: Assign df_bool = DataFrame(...)

```python
df_bool = DataFrame(True, index=df_float.index, columns=df_float.columns)
```

### Step 4: Assign df_object = DataFrame(...)

```python
df_object = DataFrame('foo', index=df_float.index, columns=df_float.columns)
```

### Step 5: Assign df_dt = DataFrame(...)

```python
df_dt = DataFrame(pd.Timestamp('20010101'), index=df_float.index, columns=df_float.columns)
```

### Step 6: Assign df = pd.concat(...)

```python
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)
```

**Verification:**
```python
assert len(df._mgr.blknos) == len(df.columns)
```

### Step 7: df.iloc[:, i]

```python
df.iloc[:, i]
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
df_float = DataFrame(np.random.default_rng(2).standard_normal((10, 3)), dtype='float64')
df_int = DataFrame(np.random.default_rng(2).standard_normal((10, 3)).astype('int64'))
df_bool = DataFrame(True, index=df_float.index, columns=df_float.columns)
df_object = DataFrame('foo', index=df_float.index, columns=df_float.columns)
df_dt = DataFrame(pd.Timestamp('20010101'), index=df_float.index, columns=df_float.columns)
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)
if not using_array_manager:
    assert len(df._mgr.blknos) == len(df.columns)
    assert len(df._mgr.blklocs) == len(df.columns)
for i in range(len(df.columns)):
    df.iloc[:, i]
```

## Next Steps


---

*Source: test_nonunique_indexes.py:287 | Complexity: Intermediate | Last updated: 2026-06-02*