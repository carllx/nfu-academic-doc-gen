# How To: Set Value With Index Dtype Change

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set value with index dtype change

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_orig = DataFrame(...)

```python
df_orig = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), index=range(3), columns=list('ABC'))
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```

### Step 2: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```

### Step 3: Call df._set_value()

```python
df._set_value('C', 2, 1.0)
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```

### Step 4: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

**Verification:**
```python
assert list(df.columns) == list(df_orig.columns) + ['D']
```

### Step 5: Assign unknown = 1.0

```python
df.loc['C', 2] = 1.0
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```

### Step 6: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

**Verification:**
```python
assert list(df.columns) == list(df_orig.columns) + ['D']
```

### Step 7: Call df._set_value()

```python
df._set_value('C', 'D', 1.0)
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```

### Step 8: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 9: Assign unknown = 1.0

```python
df.loc['C', 'D'] = 1.0
```

**Verification:**
```python
assert list(df.index) == list(df_orig.index) + ['C']
```


## Complete Example

```python
# Workflow
df_orig = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), index=range(3), columns=list('ABC'))
df = df_orig.copy()
df._set_value('C', 2, 1.0)
assert list(df.index) == list(df_orig.index) + ['C']
df = df_orig.copy()
df.loc['C', 2] = 1.0
assert list(df.index) == list(df_orig.index) + ['C']
df = df_orig.copy()
df._set_value('C', 'D', 1.0)
assert list(df.index) == list(df_orig.index) + ['C']
assert list(df.columns) == list(df_orig.columns) + ['D']
df = df_orig.copy()
df.loc['C', 'D'] = 1.0
assert list(df.index) == list(df_orig.index) + ['C']
assert list(df.columns) == list(df_orig.columns) + ['D']
```

## Next Steps


---

*Source: test_set_value.py:49 | Complexity: Advanced | Last updated: 2026-06-02*