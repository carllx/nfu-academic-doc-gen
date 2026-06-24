# How To: Update

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1.5, np.nan, 3.0, 4.0, np.nan])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([np.nan, 3.5, np.nan, 5.0])
```

### Step 3: Call s.update()

```python
s.update(s2)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.5, 3.5, 3.0, 5.0, np.nan])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame([{'a': 1}, {'a': 3, 'b': 2}])
```

### Step 7: Assign unknown = value

```python
df['c'] = np.nan
```

### Step 8: Assign unknown = unknown.astype(...)

```python
df['c'] = df['c'].astype(object)
```

### Step 9: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 11: Assign expected = df_orig

```python
expected = df_orig
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, np.nan, 'foo'], [3, 2.0, np.nan]], columns=['a', 'b', 'c'])
```

### Step 13: Assign unknown = unknown.astype(...)

```python
expected['c'] = expected['c'].astype(object)
```

### Step 14: Call unknown.update()

```python
df['c'].update(Series(['foo'], index=[0]))
```

### Step 15: Call unknown.update()

```python
df['c'].update(Series(['foo'], index=[0]))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
s = Series([1.5, np.nan, 3.0, 4.0, np.nan])
s2 = Series([np.nan, 3.5, np.nan, 5.0])
s.update(s2)
expected = Series([1.5, 3.5, 3.0, 5.0, np.nan])
tm.assert_series_equal(s, expected)
df = DataFrame([{'a': 1}, {'a': 3, 'b': 2}])
df['c'] = np.nan
df['c'] = df['c'].astype(object)
df_orig = df.copy()
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['c'].update(Series(['foo'], index=[0]))
    expected = df_orig
else:
    with tm.assert_produces_warning(FutureWarning if not WARNING_CHECK_DISABLED else None, match='inplace method'):
        df['c'].update(Series(['foo'], index=[0]))
    expected = DataFrame([[1, np.nan, 'foo'], [3, 2.0, np.nan]], columns=['a', 'b', 'c'])
    expected['c'] = expected['c'].astype(object)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_update.py:18 | Complexity: Advanced | Last updated: 2026-06-02*