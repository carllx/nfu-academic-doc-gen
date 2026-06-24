# How To: Ix Categorical Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ix categorical index

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), index=list('ABC'), columns=list('XYZ'))
```

### Step 2: Assign cdf = df.copy(...)

```python
cdf = df.copy()
```

### Step 3: Assign cdf.index = CategoricalIndex(...)

```python
cdf.index = CategoricalIndex(df.index)
```

### Step 4: Assign cdf.columns = CategoricalIndex(...)

```python
cdf.columns = CategoricalIndex(df.columns)
```

### Step 5: Assign expect = Series(...)

```python
expect = Series(df.loc['A', :], index=cdf.columns, name='A')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(cdf.loc['A', :], expect)
```

### Step 7: Assign expect = Series(...)

```python
expect = Series(df.loc[:, 'X'], index=cdf.index, name='X')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(cdf.loc[:, 'X'], expect)
```

### Step 9: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(list('AB'), categories=['A', 'B', 'C'])
```

### Step 10: Assign expect = DataFrame(...)

```python
expect = DataFrame(df.loc[['A', 'B'], :], columns=cdf.columns, index=exp_index)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(cdf.loc[['A', 'B'], :], expect)
```

### Step 12: Assign exp_columns = CategoricalIndex(...)

```python
exp_columns = CategoricalIndex(list('XY'), categories=['X', 'Y', 'Z'])
```

### Step 13: Assign expect = DataFrame(...)

```python
expect = DataFrame(df.loc[:, ['X', 'Y']], index=cdf.index, columns=exp_columns)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(cdf.loc[:, ['X', 'Y']], expect)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)), index=list('ABC'), columns=list('XYZ'))
cdf = df.copy()
cdf.index = CategoricalIndex(df.index)
cdf.columns = CategoricalIndex(df.columns)
expect = Series(df.loc['A', :], index=cdf.columns, name='A')
tm.assert_series_equal(cdf.loc['A', :], expect)
expect = Series(df.loc[:, 'X'], index=cdf.index, name='X')
tm.assert_series_equal(cdf.loc[:, 'X'], expect)
exp_index = CategoricalIndex(list('AB'), categories=['A', 'B', 'C'])
expect = DataFrame(df.loc[['A', 'B'], :], columns=cdf.columns, index=exp_index)
tm.assert_frame_equal(cdf.loc[['A', 'B'], :], expect)
exp_columns = CategoricalIndex(list('XY'), categories=['X', 'Y', 'Z'])
expect = DataFrame(df.loc[:, ['X', 'Y']], index=cdf.index, columns=exp_columns)
tm.assert_frame_equal(cdf.loc[:, ['X', 'Y']], expect)
```

## Next Steps


---

*Source: test_categorical.py:409 | Complexity: Advanced | Last updated: 2026-06-02*