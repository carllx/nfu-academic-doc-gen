# How To: Filter Out All Groups In Df

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter out all groups in df

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 2], 'b': [1, 2, 0]})
```

### Step 2: Assign res = df.groupby(...)

```python
res = df.groupby('a')
```

### Step 3: Assign res = res.filter(...)

```python
res = res.filter(lambda x: x['b'].sum() > 5, dropna=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [np.nan] * 3, 'b': [np.nan] * 3})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, res)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 2], 'b': [1, 2, 0]})
```

### Step 7: Assign res = df.groupby(...)

```python
res = df.groupby('a')
```

### Step 8: Assign res = res.filter(...)

```python
res = res.filter(lambda x: x['b'].sum() > 5, dropna=True)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [], 'b': []}, dtype='int64')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, res)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, 2], 'b': [1, 2, 0]})
res = df.groupby('a')
res = res.filter(lambda x: x['b'].sum() > 5, dropna=False)
expected = DataFrame({'a': [np.nan] * 3, 'b': [np.nan] * 3})
tm.assert_frame_equal(expected, res)
df = DataFrame({'a': [1, 1, 2], 'b': [1, 2, 0]})
res = df.groupby('a')
res = res.filter(lambda x: x['b'].sum() > 5, dropna=True)
expected = DataFrame({'a': [], 'b': []}, dtype='int64')
tm.assert_frame_equal(expected, res)
```

## Next Steps


---

*Source: test_filters.py:95 | Complexity: Advanced | Last updated: 2026-06-02*