# How To: Count Cross Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test count cross type

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals = np.hstack.astype(...)

```python
vals = np.hstack((np.random.default_rng(2).integers(0, 5, (100, 2)), np.random.default_rng(2).integers(0, 2, (100, 2)))).astype('float64')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(vals, columns=['a', 'b', 'c', 'd'])
```

### Step 3: Assign unknown = value

```python
df[df == 2] = np.nan
```

### Step 4: Assign expected = df.groupby.count(...)

```python
expected = df.groupby(['c', 'd']).count()
```

### Step 5: Assign unknown = unknown.astype(...)

```python
df['a'] = df['a'].astype(t)
```

### Step 6: Assign unknown = unknown.astype(...)

```python
df['b'] = df['b'].astype(t)
```

### Step 7: Assign result = df.groupby.count(...)

```python
result = df.groupby(['c', 'd']).count()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
vals = np.hstack((np.random.default_rng(2).integers(0, 5, (100, 2)), np.random.default_rng(2).integers(0, 2, (100, 2)))).astype('float64')
df = DataFrame(vals, columns=['a', 'b', 'c', 'd'])
df[df == 2] = np.nan
expected = df.groupby(['c', 'd']).count()
for t in ['float32', 'object']:
    df['a'] = df['a'].astype(t)
    df['b'] = df['b'].astype(t)
    result = df.groupby(['c', 'd']).count()
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_counting.py:330 | Complexity: Advanced | Last updated: 2026-06-02*