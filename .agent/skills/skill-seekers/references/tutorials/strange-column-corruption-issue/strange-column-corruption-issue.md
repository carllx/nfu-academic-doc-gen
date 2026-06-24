# How To: Strange Column Corruption Issue

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test strange column corruption issue

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.internals.blocks`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=[0, 1])
```

**Verification:**
```python
assert first == second == 0
```

### Step 2: Assign unknown = value

```python
df[0] = np.nan
```

### Step 3: Assign wasCol = value

```python
wasCol = {}
```

### Step 4: Assign myid = 100

```python
myid = 100
```

### Step 5: Assign first = len(...)

```python
first = len(df.loc[pd.isna(df[myid]), [myid]])
```

### Step 6: Assign second = len(...)

```python
second = len(df.loc[pd.isna(df[myid]), [myid]])
```

**Verification:**
```python
assert first == second == 0
```

### Step 7: Assign unknown = 1

```python
wasCol[col] = 1
```

### Step 8: Assign unknown = value

```python
df[col] = np.nan
```

### Step 9: Assign unknown = i

```python
df.loc[dt, col] = i
```

### Step 10: Assign unknown = i

```python
df[col][dt] = i
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame(index=[0, 1])
df[0] = np.nan
wasCol = {}
with tm.assert_produces_warning(PerformanceWarning, raise_on_extra_warnings=False):
    for i, dt in enumerate(df.index):
        for col in range(100, 200):
            if col not in wasCol:
                wasCol[col] = 1
                df[col] = np.nan
            if using_copy_on_write:
                df.loc[dt, col] = i
            else:
                df[col][dt] = i
myid = 100
first = len(df.loc[pd.isna(df[myid]), [myid]])
second = len(df.loc[pd.isna(df[myid]), [myid]])
assert first == second == 0
```

## Next Steps


---

*Source: test_block_internals.py:351 | Complexity: Advanced | Last updated: 2026-06-02*