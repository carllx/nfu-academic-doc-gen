# How To: To Csv Mixed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv mixed

## Prerequisites

**Required Modules:**
- `csv`
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`
- `pandas.io.common`


## Step-by-Step Guide

### Step 1: Assign df_float = DataFrame(...)

```python
df_float = DataFrame(np.random.default_rng(2).standard_normal((100, 5)), dtype='float64', columns=create_cols('float'))
```

### Step 2: Assign df_int = DataFrame(...)

```python
df_int = DataFrame(np.random.default_rng(2).standard_normal((100, 5)).astype('int64'), dtype='int64', columns=create_cols('int'))
```

### Step 3: Assign df_bool = DataFrame(...)

```python
df_bool = DataFrame(True, index=df_float.index, columns=create_cols('bool'))
```

### Step 4: Assign df_object = DataFrame(...)

```python
df_object = DataFrame('foo', index=df_float.index, columns=create_cols('object'), dtype='object')
```

### Step 5: Assign df_dt = DataFrame(...)

```python
df_dt = DataFrame(Timestamp('20010101').as_unit('ns'), index=df_float.index, columns=create_cols('date'))
```

### Step 6: Assign unknown = value

```python
df_float.iloc[30:50, 1:3] = np.nan
```

### Step 7: Assign unknown = value

```python
df_dt.iloc[30:50, 1:3] = np.nan
```

### Step 8: Assign df = pd.concat(...)

```python
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)
```

### Step 9: Assign dtypes = value

```python
dtypes = {}
```

### Step 10: Call df.to_csv()

```python
df.to_csv(filename)
```

### Step 11: Assign rs = read_csv(...)

```python
rs = read_csv(filename, index_col=0, dtype=dtypes, parse_dates=create_cols('date'))
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, df)
```

### Step 13: Assign unknown = dtype

```python
dtypes[c] = dtype
```


## Complete Example

```python
# Workflow
def create_cols(name):
    return [f'{name}{i:03d}' for i in range(5)]
df_float = DataFrame(np.random.default_rng(2).standard_normal((100, 5)), dtype='float64', columns=create_cols('float'))
df_int = DataFrame(np.random.default_rng(2).standard_normal((100, 5)).astype('int64'), dtype='int64', columns=create_cols('int'))
df_bool = DataFrame(True, index=df_float.index, columns=create_cols('bool'))
df_object = DataFrame('foo', index=df_float.index, columns=create_cols('object'), dtype='object')
df_dt = DataFrame(Timestamp('20010101').as_unit('ns'), index=df_float.index, columns=create_cols('date'))
df_float.iloc[30:50, 1:3] = np.nan
df_dt.iloc[30:50, 1:3] = np.nan
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1)
dtypes = {}
for n, dtype in [('float', np.float64), ('int', np.int64), ('bool', np.bool_), ('object', object)]:
    for c in create_cols(n):
        dtypes[c] = dtype
with tm.ensure_clean() as filename:
    df.to_csv(filename)
    rs = read_csv(filename, index_col=0, dtype=dtypes, parse_dates=create_cols('date'))
    tm.assert_frame_equal(rs, df)
```

## Next Steps


---

*Source: test_to_csv.py:721 | Complexity: Advanced | Last updated: 2026-06-02*