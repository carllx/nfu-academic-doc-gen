# How To: Categorical Index Preserver

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical index preserver

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series(np.arange(6, dtype='int64'))
```

### Step 2: Assign b = Series(...)

```python
b = Series(list('aabbca'))
```

### Step 3: Assign df2 = DataFrame.set_index(...)

```python
df2 = DataFrame({'A': a, 'B': b.astype(CategoricalDtype(list('cab')))}).set_index('B')
```

### Step 4: Assign result = pd.concat(...)

```python
result = pd.concat([df2, df2])
```

### Step 5: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'A': pd.concat([a, a]), 'B': pd.concat([b, b]).astype(CategoricalDtype(list('cab')))}).set_index('B')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df3 = DataFrame.set_index(...)

```python
df3 = DataFrame({'A': a, 'B': Categorical(b, categories=list('abe'))}).set_index('B')
```

### Step 8: Assign result = pd.concat(...)

```python
result = pd.concat([df2, df3])
```

### Step 9: Assign expected = pd.concat(...)

```python
expected = pd.concat([df2.set_axis(df2.index.astype(object), axis=0), df3.set_axis(df3.index.astype(object), axis=0)])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Series(np.arange(6, dtype='int64'))
b = Series(list('aabbca'))
df2 = DataFrame({'A': a, 'B': b.astype(CategoricalDtype(list('cab')))}).set_index('B')
result = pd.concat([df2, df2])
expected = DataFrame({'A': pd.concat([a, a]), 'B': pd.concat([b, b]).astype(CategoricalDtype(list('cab')))}).set_index('B')
tm.assert_frame_equal(result, expected)
df3 = DataFrame({'A': a, 'B': Categorical(b, categories=list('abe'))}).set_index('B')
result = pd.concat([df2, df3])
expected = pd.concat([df2.set_axis(df2.index.astype(object), axis=0), df3.set_axis(df3.index.astype(object), axis=0)])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:127 | Complexity: Advanced | Last updated: 2026-06-02*