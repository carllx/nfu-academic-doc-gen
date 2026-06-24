# How To: Compress Group Combinations

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compress group combinations

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign key1 = value

```python
key1 = [str(i) for i in range(10000)]
```

### Step 2: Assign key1 = np.tile(...)

```python
key1 = np.tile(key1, 2)
```

### Step 3: Assign key2 = value

```python
key2 = key1[::-1]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'key1': key1, 'key2': key2, 'value1': np.random.default_rng(2).standard_normal(20000)})
```

### Step 5: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key1': key1[::2], 'key2': key2[::2], 'value2': np.random.default_rng(2).standard_normal(10000)})
```

### Step 6: Call merge()

```python
merge(df, df2, how='outer')
```


## Complete Example

```python
# Workflow
key1 = [str(i) for i in range(10000)]
key1 = np.tile(key1, 2)
key2 = key1[::-1]
df = DataFrame({'key1': key1, 'key2': key2, 'value1': np.random.default_rng(2).standard_normal(20000)})
df2 = DataFrame({'key1': key1[::2], 'key2': key2[::2], 'value2': np.random.default_rng(2).standard_normal(10000)})
merge(df, df2, how='outer')
```

## Next Steps


---

*Source: test_multi.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*