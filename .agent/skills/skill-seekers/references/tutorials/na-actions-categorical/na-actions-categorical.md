# How To: Na Actions Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na actions categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical([1, 2, 3, np.nan], categories=[1, 2, 3])
```

### Step 2: Assign vals = value

```python
vals = ['a', 'b', np.nan, 'd']
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'cats': cat, 'vals': vals})
```

### Step 4: Assign cat2 = Categorical(...)

```python
cat2 = Categorical([1, 2, 3, 3], categories=[1, 2, 3])
```

### Step 5: Assign vals2 = value

```python
vals2 = ['a', 'b', 'b', 'd']
```

### Step 6: Assign df_exp_fill = DataFrame(...)

```python
df_exp_fill = DataFrame({'cats': cat2, 'vals': vals2})
```

### Step 7: Assign cat3 = Categorical(...)

```python
cat3 = Categorical([1, 2, 3], categories=[1, 2, 3])
```

### Step 8: Assign vals3 = value

```python
vals3 = ['a', 'b', np.nan]
```

### Step 9: Assign df_exp_drop_cats = DataFrame(...)

```python
df_exp_drop_cats = DataFrame({'cats': cat3, 'vals': vals3})
```

### Step 10: Assign cat4 = Categorical(...)

```python
cat4 = Categorical([1, 2], categories=[1, 2, 3])
```

### Step 11: Assign vals4 = value

```python
vals4 = ['a', 'b']
```

### Step 12: Assign df_exp_drop_all = DataFrame(...)

```python
df_exp_drop_all = DataFrame({'cats': cat4, 'vals': vals4})
```

### Step 13: Assign res = df.fillna(...)

```python
res = df.fillna(value={'cats': 3, 'vals': 'b'})
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, df_exp_fill)
```

### Step 15: Assign msg = 'Cannot setitem on a Categorical with a new category'

```python
msg = 'Cannot setitem on a Categorical with a new category'
```

### Step 16: Assign msg = "DataFrame.fillna with 'method' is deprecated"

```python
msg = "DataFrame.fillna with 'method' is deprecated"
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, df_exp_fill)
```

### Step 18: Assign res = df.dropna(...)

```python
res = df.dropna(subset=['cats'])
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, df_exp_drop_cats)
```

### Step 20: Assign res = df.dropna(...)

```python
res = df.dropna()
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, df_exp_drop_all)
```

### Step 22: Assign c = Categorical(...)

```python
c = Categorical([np.nan, 'b', np.nan], categories=['a', 'b'])
```

### Step 23: Assign df = DataFrame(...)

```python
df = DataFrame({'cats': c, 'vals': [1, 2, 3]})
```

### Step 24: Assign cat_exp = Categorical(...)

```python
cat_exp = Categorical(['a', 'b', 'a'], categories=['a', 'b'])
```

### Step 25: Assign df_exp = DataFrame(...)

```python
df_exp = DataFrame({'cats': cat_exp, 'vals': [1, 2, 3]})
```

### Step 26: Assign res = df.fillna(...)

```python
res = df.fillna('a')
```

### Step 27: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, df_exp)
```

### Step 28: Call df.fillna()

```python
df.fillna(value={'cats': 4, 'vals': 'c'})
```

### Step 29: Assign res = df.fillna(...)

```python
res = df.fillna(method='pad')
```


## Complete Example

```python
# Workflow
cat = Categorical([1, 2, 3, np.nan], categories=[1, 2, 3])
vals = ['a', 'b', np.nan, 'd']
df = DataFrame({'cats': cat, 'vals': vals})
cat2 = Categorical([1, 2, 3, 3], categories=[1, 2, 3])
vals2 = ['a', 'b', 'b', 'd']
df_exp_fill = DataFrame({'cats': cat2, 'vals': vals2})
cat3 = Categorical([1, 2, 3], categories=[1, 2, 3])
vals3 = ['a', 'b', np.nan]
df_exp_drop_cats = DataFrame({'cats': cat3, 'vals': vals3})
cat4 = Categorical([1, 2], categories=[1, 2, 3])
vals4 = ['a', 'b']
df_exp_drop_all = DataFrame({'cats': cat4, 'vals': vals4})
res = df.fillna(value={'cats': 3, 'vals': 'b'})
tm.assert_frame_equal(res, df_exp_fill)
msg = 'Cannot setitem on a Categorical with a new category'
with pytest.raises(TypeError, match=msg):
    df.fillna(value={'cats': 4, 'vals': 'c'})
msg = "DataFrame.fillna with 'method' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = df.fillna(method='pad')
tm.assert_frame_equal(res, df_exp_fill)
res = df.dropna(subset=['cats'])
tm.assert_frame_equal(res, df_exp_drop_cats)
res = df.dropna()
tm.assert_frame_equal(res, df_exp_drop_all)
c = Categorical([np.nan, 'b', np.nan], categories=['a', 'b'])
df = DataFrame({'cats': c, 'vals': [1, 2, 3]})
cat_exp = Categorical(['a', 'b', 'a'], categories=['a', 'b'])
df_exp = DataFrame({'cats': cat_exp, 'vals': [1, 2, 3]})
res = df.fillna('a')
tm.assert_frame_equal(res, df_exp)
```

## Next Steps


---

*Source: test_fillna.py:225 | Complexity: Advanced | Last updated: 2026-06-02*