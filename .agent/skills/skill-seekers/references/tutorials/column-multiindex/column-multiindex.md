# How To: Column Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test column multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b')], names=['first', 'second'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(12).reshape(3, 4), columns=index)
```

### Step 3: Assign expected = df.set_axis(...)

```python
expected = df.set_axis(df.index.to_numpy())
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(12).reshape(3, 4), columns=Index(list('ABCD'), name='foo'))
```

### Step 5: Assign expected = df.set_axis(...)

```python
expected = df.set_axis(df.index.to_numpy())
```

### Step 6: Call store.put()

```python
store.put('df', df)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['df'], expected, check_index_type=True, check_column_type=True)
```

### Step 8: Call store.put()

```python
store.put('df1', df, format='table')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)
```

### Step 10: Assign msg = re.escape(...)

```python
msg = re.escape("cannot use a multi-index on axis [1] with data_columns ['A']")
```

### Step 11: Assign msg = re.escape(...)

```python
msg = re.escape('cannot use a multi-index on axis [1] with data_columns True')
```

### Step 12: Call store.append()

```python
store.append('df2', df)
```

### Step 13: Call store.append()

```python
store.append('df2', df)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['df2'], concat((df, df)))
```

### Step 15: Call store.put()

```python
store.put('df1', df, format='table')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)
```

### Step 17: Assign msg = 'Saving a MultiIndex with an extension dtype is not supported.'

```python
msg = 'Saving a MultiIndex with an extension dtype is not supported.'
```

### Step 18: Call store.put()

```python
store.put('df2', df, format='table', data_columns=['A'])
```

### Step 19: Call store.put()

```python
store.put('df3', df, format='table', data_columns=True)
```

### Step 20: Call store.put()

```python
store.put('df', df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path, using_infer_string

# Workflow
index = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b')], names=['first', 'second'])
df = DataFrame(np.arange(12).reshape(3, 4), columns=index)
expected = df.set_axis(df.index.to_numpy())
with ensure_clean_store(setup_path) as store:
    if using_infer_string:
        msg = 'Saving a MultiIndex with an extension dtype is not supported.'
        with pytest.raises(NotImplementedError, match=msg):
            store.put('df', df)
        return
    store.put('df', df)
    tm.assert_frame_equal(store['df'], expected, check_index_type=True, check_column_type=True)
    store.put('df1', df, format='table')
    tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)
    msg = re.escape("cannot use a multi-index on axis [1] with data_columns ['A']")
    with pytest.raises(ValueError, match=msg):
        store.put('df2', df, format='table', data_columns=['A'])
    msg = re.escape('cannot use a multi-index on axis [1] with data_columns True')
    with pytest.raises(ValueError, match=msg):
        store.put('df3', df, format='table', data_columns=True)
with ensure_clean_store(setup_path) as store:
    store.append('df2', df)
    store.append('df2', df)
    tm.assert_frame_equal(store['df2'], concat((df, df)))
df = DataFrame(np.arange(12).reshape(3, 4), columns=Index(list('ABCD'), name='foo'))
expected = df.set_axis(df.index.to_numpy())
with ensure_clean_store(setup_path) as store:
    store.put('df1', df, format='table')
    tm.assert_frame_equal(store['df1'], expected, check_index_type=True, check_column_type=True)
```

## Next Steps


---

*Source: test_put.py:290 | Complexity: Advanced | Last updated: 2026-06-02*