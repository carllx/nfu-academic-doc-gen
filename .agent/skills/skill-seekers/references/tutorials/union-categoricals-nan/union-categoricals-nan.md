# How To: Union Categoricals Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categoricals nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign res = union_categoricals(...)

```python
res = union_categoricals([Categorical([1, 2, np.nan]), Categorical([3, 2, np.nan])])
```

### Step 2: Assign exp = Categorical(...)

```python
exp = Categorical([1, 2, np.nan, 3, 2, np.nan])
```

### Step 3: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 4: Assign res = union_categoricals(...)

```python
res = union_categoricals([Categorical(['A', 'B']), Categorical(['B', 'B', np.nan])])
```

### Step 5: Assign exp = Categorical(...)

```python
exp = Categorical(['A', 'B', 'B', 'B', np.nan])
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 7: Assign val1 = value

```python
val1 = [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.NaT]
```

### Step 8: Assign val2 = value

```python
val2 = [pd.NaT, pd.Timestamp('2011-01-01'), pd.Timestamp('2011-02-01')]
```

### Step 9: Assign res = union_categoricals(...)

```python
res = union_categoricals([Categorical(val1), Categorical(val2)])
```

### Step 10: Assign exp = Categorical(...)

```python
exp = Categorical(val1 + val2, categories=[pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.Timestamp('2011-02-01')])
```

### Step 11: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 12: Assign res = union_categoricals(...)

```python
res = union_categoricals([Categorical(np.array([np.nan, np.nan], dtype=object)), Categorical(['X'], categories=pd.Index(['X'], dtype=object))])
```

### Step 13: Assign exp = Categorical(...)

```python
exp = Categorical([np.nan, np.nan, 'X'])
```

### Step 14: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```

### Step 15: Assign res = union_categoricals(...)

```python
res = union_categoricals([Categorical([np.nan, np.nan]), Categorical([np.nan, np.nan])])
```

### Step 16: Assign exp = Categorical(...)

```python
exp = Categorical([np.nan, np.nan, np.nan, np.nan])
```

### Step 17: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```


## Complete Example

```python
# Workflow
res = union_categoricals([Categorical([1, 2, np.nan]), Categorical([3, 2, np.nan])])
exp = Categorical([1, 2, np.nan, 3, 2, np.nan])
tm.assert_categorical_equal(res, exp)
res = union_categoricals([Categorical(['A', 'B']), Categorical(['B', 'B', np.nan])])
exp = Categorical(['A', 'B', 'B', 'B', np.nan])
tm.assert_categorical_equal(res, exp)
val1 = [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.NaT]
val2 = [pd.NaT, pd.Timestamp('2011-01-01'), pd.Timestamp('2011-02-01')]
res = union_categoricals([Categorical(val1), Categorical(val2)])
exp = Categorical(val1 + val2, categories=[pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.Timestamp('2011-02-01')])
tm.assert_categorical_equal(res, exp)
res = union_categoricals([Categorical(np.array([np.nan, np.nan], dtype=object)), Categorical(['X'], categories=pd.Index(['X'], dtype=object))])
exp = Categorical([np.nan, np.nan, 'X'])
tm.assert_categorical_equal(res, exp)
res = union_categoricals([Categorical([np.nan, np.nan]), Categorical([np.nan, np.nan])])
exp = Categorical([np.nan, np.nan, np.nan, np.nan])
tm.assert_categorical_equal(res, exp)
```

## Next Steps


---

*Source: test_union_categoricals.py:81 | Complexity: Advanced | Last updated: 2026-06-02*