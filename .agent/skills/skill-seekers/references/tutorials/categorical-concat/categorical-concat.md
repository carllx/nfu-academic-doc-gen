# How To: Categorical Concat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical concat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(np.arange(18, dtype='int64').reshape(6, 3), columns=['a', 'b', 'c'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.arange(14, dtype='int64').reshape(7, 2), columns=['a', 'c'])
```

### Step 3: Assign cat_values = value

```python
cat_values = ['one', 'one', 'two', 'one', 'two', 'two', 'one']
```

### Step 4: Assign unknown = Series(...)

```python
df2['h'] = Series(Categorical(cat_values))
```

### Step 5: Assign res = pd.concat(...)

```python
res = pd.concat((df1, df2), axis=0, ignore_index=True, sort=sort)
```

### Step 6: Assign exp = DataFrame(...)

```python
exp = DataFrame({'a': [0, 3, 6, 9, 12, 15, 0, 2, 4, 6, 8, 10, 12], 'b': [1, 4, 7, 10, 13, 16, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 'c': [2, 5, 8, 11, 14, 17, 1, 3, 5, 7, 9, 11, 13], 'h': [None] * 6 + cat_values})
```

### Step 7: Assign unknown = unknown.astype(...)

```python
exp['h'] = exp['h'].astype(df2['h'].dtype)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df1 = DataFrame(np.arange(18, dtype='int64').reshape(6, 3), columns=['a', 'b', 'c'])
df2 = DataFrame(np.arange(14, dtype='int64').reshape(7, 2), columns=['a', 'c'])
cat_values = ['one', 'one', 'two', 'one', 'two', 'two', 'one']
df2['h'] = Series(Categorical(cat_values))
res = pd.concat((df1, df2), axis=0, ignore_index=True, sort=sort)
exp = DataFrame({'a': [0, 3, 6, 9, 12, 15, 0, 2, 4, 6, 8, 10, 12], 'b': [1, 4, 7, 10, 13, 16, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 'c': [2, 5, 8, 11, 14, 17, 1, 3, 5, 7, 9, 11, 13], 'h': [None] * 6 + cat_values})
exp['h'] = exp['h'].astype(df2['h'].dtype)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_categorical.py:17 | Complexity: Advanced | Last updated: 2026-06-02*