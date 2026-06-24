# How To: Isin Df Dupe Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin df dupe values

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
df1 = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['B', 'B'])
```

### Step 3: Assign msg = 'cannot compute isin with a duplicate axis\\.'

```python
msg = 'cannot compute isin with a duplicate axis\\.'
```

### Step 4: Assign df2 = DataFrame(...)

```python
df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['A', 'B'], index=[0, 0, 1, 1])
```

### Step 5: Assign df2.columns = value

```python
df2.columns = ['B', 'B']
```

### Step 6: Call df1.isin()

```python
df1.isin(df2)
```

### Step 7: Call df1.isin()

```python
df1.isin(df2)
```

### Step 8: Call df1.isin()

```python
df1.isin(df2)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]})
df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['B', 'B'])
msg = 'cannot compute isin with a duplicate axis\\.'
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)
df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=['A', 'B'], index=[0, 0, 1, 1])
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)
df2.columns = ['B', 'B']
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)
```

## Next Steps


---

*Source: test_isin.py:99 | Complexity: Advanced | Last updated: 2026-06-02*