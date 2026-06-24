# How To: Frame Describe Tupleindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame describe tupleindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'x': [1, 2, 3, 4, 5] * 3, 'y': [10, 20, 30, 40, 50] * 3, 'z': [100, 200, 300, 400, 500] * 3})
```

### Step 2: Assign unknown = value

```python
df1['k'] = [(0, 0, 1), (0, 1, 0), (1, 0, 0)] * 5
```

### Step 3: Assign df2 = df1.rename(...)

```python
df2 = df1.rename(columns={'k': 'key'})
```

### Step 4: Assign msg = 'Names should be list-like for a MultiIndex'

```python
msg = 'Names should be list-like for a MultiIndex'
```

### Step 5: Call df1.groupby.describe()

```python
df1.groupby('k').describe()
```

### Step 6: Call df2.groupby.describe()

```python
df2.groupby('key').describe()
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'x': [1, 2, 3, 4, 5] * 3, 'y': [10, 20, 30, 40, 50] * 3, 'z': [100, 200, 300, 400, 500] * 3})
df1['k'] = [(0, 0, 1), (0, 1, 0), (1, 0, 0)] * 5
df2 = df1.rename(columns={'k': 'key'})
msg = 'Names should be list-like for a MultiIndex'
with pytest.raises(ValueError, match=msg):
    df1.groupby('k').describe()
with pytest.raises(ValueError, match=msg):
    df2.groupby('key').describe()
```

## Next Steps


---

*Source: test_describe.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*