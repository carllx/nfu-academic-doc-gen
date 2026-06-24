# How To: Compare Unaligned Objects

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare unaligned objects

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'

```python
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
```

### Step 2: Assign msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'

```python
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
```

### Step 3: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame([1, 2, 3], index=['a', 'b', 'c'])
```

### Step 4: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame([1, 2, 3], index=['a', 'b', 'd'])
```

### Step 5: Call df1.compare()

```python
df1.compare(df2)
```

### Step 6: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame(np.ones((3, 3)))
```

### Step 7: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame(np.zeros((2, 1)))
```

### Step 8: Call df1.compare()

```python
df1.compare(df2)
```


## Complete Example

```python
# Workflow
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
with pytest.raises(ValueError, match=msg):
    df1 = pd.DataFrame([1, 2, 3], index=['a', 'b', 'c'])
    df2 = pd.DataFrame([1, 2, 3], index=['a', 'b', 'd'])
    df1.compare(df2)
msg = 'Can only compare identically-labeled \\(both index and columns\\) DataFrame objects'
with pytest.raises(ValueError, match=msg):
    df1 = pd.DataFrame(np.ones((3, 3)))
    df2 = pd.DataFrame(np.zeros((2, 1)))
    df1.compare(df2)
```

## Next Steps


---

*Source: test_compare.py:171 | Complexity: Advanced | Last updated: 2026-06-02*