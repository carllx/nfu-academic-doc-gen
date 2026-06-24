# How To: Unexpected Keyword

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unexpected keyword

## Prerequisites

**Required Modules:**
- `copy`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=['jim', 'joe'])
```

### Step 2: Assign ca = pd.Categorical(...)

```python
ca = pd.Categorical([0, 0, 2, 2, 3, np.nan])
```

### Step 3: Assign ts = unknown.copy(...)

```python
ts = df['joe'].copy()
```

### Step 4: Assign unknown = value

```python
ts[2] = np.nan
```

### Step 5: Assign msg = 'unexpected keyword'

```python
msg = 'unexpected keyword'
```

### Step 6: Call df.drop()

```python
df.drop('joe', axis=1, in_place=True)
```

### Step 7: Call df.reindex()

```python
df.reindex([1, 0], inplace=True)
```

### Step 8: Call ca.fillna()

```python
ca.fillna(0, inplace=True)
```

### Step 9: Call ts.fillna()

```python
ts.fillna(0, in_place=True)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), columns=['jim', 'joe'])
ca = pd.Categorical([0, 0, 2, 2, 3, np.nan])
ts = df['joe'].copy()
ts[2] = np.nan
msg = 'unexpected keyword'
with pytest.raises(TypeError, match=msg):
    df.drop('joe', axis=1, in_place=True)
with pytest.raises(TypeError, match=msg):
    df.reindex([1, 0], inplace=True)
with pytest.raises(TypeError, match=msg):
    ca.fillna(0, inplace=True)
with pytest.raises(TypeError, match=msg):
    ts.fillna(0, in_place=True)
```

## Next Steps


---

*Source: test_frame.py:189 | Complexity: Advanced | Last updated: 2026-06-02*