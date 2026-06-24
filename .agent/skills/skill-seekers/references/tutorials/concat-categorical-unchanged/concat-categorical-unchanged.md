# How To: Concat Categorical Unchanged

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categorical unchanged

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(Series(['a', 'b', 'c'], dtype='category', name='A'))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([0, 1, 2], index=[0, 1, 3], name='B')
```

### Step 3: Assign result = pd.concat(...)

```python
result = pd.concat([df, ser], axis=1)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': Series(['a', 'b', 'c', np.nan], dtype='category'), 'B': Series([0, 1, np.nan, 2], dtype='float')})
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(Series(['a', 'b', 'c'], dtype='category', name='A'))
ser = Series([0, 1, 2], index=[0, 1, 3], name='B')
result = pd.concat([df, ser], axis=1)
expected = DataFrame({'A': Series(['a', 'b', 'c', np.nan], dtype='category'), 'B': Series([0, 1, np.nan, 2], dtype='float')})
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*