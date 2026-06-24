# How To: Dropna With Duplicate Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dropna with duplicate columns

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.random.default_rng(2).standard_normal(5), 'B': np.random.default_rng(2).standard_normal(5), 'C': np.random.default_rng(2).standard_normal(5), 'D': ['a', 'b', 'c', 'd', 'e']})
```

### Step 2: Assign unknown = value

```python
df.iloc[2, [0, 1, 2]] = np.nan
```

### Step 3: Assign unknown = value

```python
df.iloc[0, 0] = np.nan
```

### Step 4: Assign unknown = value

```python
df.iloc[1, 1] = np.nan
```

### Step 5: Assign unknown = value

```python
df.iloc[:, 3] = np.nan
```

### Step 6: Assign expected = df.dropna(...)

```python
expected = df.dropna(subset=['A', 'B', 'C'], how='all')
```

### Step 7: Assign expected.columns = value

```python
expected.columns = ['A', 'A', 'B', 'C']
```

### Step 8: Assign df.columns = value

```python
df.columns = ['A', 'A', 'B', 'C']
```

### Step 9: Assign result = df.dropna(...)

```python
result = df.dropna(subset=['A', 'C'], how='all')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.random.default_rng(2).standard_normal(5), 'B': np.random.default_rng(2).standard_normal(5), 'C': np.random.default_rng(2).standard_normal(5), 'D': ['a', 'b', 'c', 'd', 'e']})
df.iloc[2, [0, 1, 2]] = np.nan
df.iloc[0, 0] = np.nan
df.iloc[1, 1] = np.nan
df.iloc[:, 3] = np.nan
expected = df.dropna(subset=['A', 'B', 'C'], how='all')
expected.columns = ['A', 'A', 'B', 'C']
df.columns = ['A', 'A', 'B', 'C']
result = df.dropna(subset=['A', 'C'], how='all')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dropna.py:211 | Complexity: Advanced | Last updated: 2026-06-02*