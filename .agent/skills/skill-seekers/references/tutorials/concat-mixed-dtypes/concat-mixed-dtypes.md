# How To: Concat Mixed Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat mixed dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'A': data[:3]})
```

### Step 2: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'A': [1, 2, 3]})
```

### Step 3: Assign df3 = pd.DataFrame.astype(...)

```python
df3 = pd.DataFrame({'A': ['a', 'b', 'c']}).astype('category')
```

### Step 4: Assign dfs = value

```python
dfs = [df1, df2, df3]
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat(dfs)
```

### Step 6: Assign expected = pd.concat(...)

```python
expected = pd.concat([x.apply(lambda s: np.asarray(s).astype(object)) for x in dfs])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
df1 = pd.DataFrame({'A': data[:3]})
df2 = pd.DataFrame({'A': [1, 2, 3]})
df3 = pd.DataFrame({'A': ['a', 'b', 'c']}).astype('category')
dfs = [df1, df2, df3]
result = pd.concat(dfs)
expected = pd.concat([x.apply(lambda s: np.asarray(s).astype(object)) for x in dfs])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sparse.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*