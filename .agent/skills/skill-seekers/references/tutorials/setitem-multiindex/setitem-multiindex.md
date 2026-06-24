# How To: Setitem Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cols = value

```python
cols = ['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit']
```

### Step 2: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([np.arange(0, 100), np.arange(0, 80)], names=['time', 'firm'])
```

### Step 3: Assign unknown = value

```python
t, n = (0, 2)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.nan, columns=cols, index=index)
```

### Step 5: Call self.check()

```python
self.check(target=df, indexers=((t, n), 'X'), value=0)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame(-999, columns=cols, index=index)
```

### Step 7: Call self.check()

```python
self.check(target=df, indexers=((t, n), 'X'), value=1)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(columns=cols, index=index)
```

### Step 9: Call self.check()

```python
self.check(target=df, indexers=((t, n), 'X'), value=2)
```

### Step 10: Assign df = DataFrame(...)

```python
df = DataFrame(-999, columns=cols, index=index)
```

### Step 11: Call self.check()

```python
self.check(target=df, indexers=((t, n), 'X'), value=np.array(3), expected=3)
```


## Complete Example

```python
# Workflow
cols = ['A', 'w', 'l', 'a', 'x', 'X', 'd', 'profit']
index = MultiIndex.from_product([np.arange(0, 100), np.arange(0, 80)], names=['time', 'firm'])
t, n = (0, 2)
df = DataFrame(np.nan, columns=cols, index=index)
self.check(target=df, indexers=((t, n), 'X'), value=0)
df = DataFrame(-999, columns=cols, index=index)
self.check(target=df, indexers=((t, n), 'X'), value=1)
df = DataFrame(columns=cols, index=index)
self.check(target=df, indexers=((t, n), 'X'), value=2)
df = DataFrame(-999, columns=cols, index=index)
self.check(target=df, indexers=((t, n), 'X'), value=np.array(3), expected=3)
```

## Next Steps


---

*Source: test_setitem.py:31 | Complexity: Advanced | Last updated: 2026-06-02*