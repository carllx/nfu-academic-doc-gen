# How To: Sort Values Multicolumn Uint64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values multicolumn uint64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': pd.Series([18446637057563306014, 1162265347240853609]), 'b': pd.Series([1, 2])})
```

### Step 2: Assign unknown = unknown.astype(...)

```python
df['a'] = df['a'].astype(np.uint64)
```

### Step 3: Assign result = df.sort_values(...)

```python
result = df.sort_values(['a', 'b'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': pd.Series([18446637057563306014, 1162265347240853609]), 'b': pd.Series([1, 2])}, index=pd.Index([1, 0]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': pd.Series([18446637057563306014, 1162265347240853609]), 'b': pd.Series([1, 2])})
df['a'] = df['a'].astype(np.uint64)
result = df.sort_values(['a', 'b'])
expected = DataFrame({'a': pd.Series([18446637057563306014, 1162265347240853609]), 'b': pd.Series([1, 2])}, index=pd.Index([1, 0]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_values.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*