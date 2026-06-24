# How To: To Csv Dups Cols

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv dups cols

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((1000, 30)), columns=list(range(15)) + list(range(15)), dtype='float64')
```

### Step 2: Assign df_float = DataFrame(...)

```python
df_float = DataFrame(np.random.default_rng(2).standard_normal((1000, 3)), dtype='float64')
```

### Step 3: Assign df_int = DataFrame.astype(...)

```python
df_int = DataFrame(np.random.default_rng(2).standard_normal((1000, 3))).astype('int64')
```

### Step 4: Assign df_bool = DataFrame(...)

```python
df_bool = DataFrame(True, index=df_float.index, columns=range(3))
```

### Step 5: Assign df_object = DataFrame(...)

```python
df_object = DataFrame('foo', index=df_float.index, columns=range(3))
```

### Step 6: Assign df_dt = DataFrame(...)

```python
df_dt = DataFrame(Timestamp('20010101').as_unit('ns'), index=df_float.index, columns=range(3))
```

### Step 7: Assign df = pd.concat(...)

```python
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1, ignore_index=True)
```

### Step 8: Assign df.columns = value

```python
df.columns = [0, 1, 2] * 5
```

### Step 9: Call df.to_csv()

```python
df.to_csv(filename)
```

### Step 10: Assign result = read_csv(...)

```python
result = read_csv(filename, index_col=0)
```

### Step 11: Assign result.columns = value

```python
result.columns = df.columns
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 13: Call df.to_csv()

```python
df.to_csv(filename)
```

### Step 14: Assign result = read_csv(...)

```python
result = read_csv(filename, index_col=0)
```

### Step 15: Assign result.columns = value

```python
result.columns = df.columns
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 17: Assign unknown = to_datetime(...)

```python
result[i] = to_datetime(result[i])
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((1000, 30)), columns=list(range(15)) + list(range(15)), dtype='float64')
with tm.ensure_clean() as filename:
    df.to_csv(filename)
    result = read_csv(filename, index_col=0)
    result.columns = df.columns
    tm.assert_frame_equal(result, df)
df_float = DataFrame(np.random.default_rng(2).standard_normal((1000, 3)), dtype='float64')
df_int = DataFrame(np.random.default_rng(2).standard_normal((1000, 3))).astype('int64')
df_bool = DataFrame(True, index=df_float.index, columns=range(3))
df_object = DataFrame('foo', index=df_float.index, columns=range(3))
df_dt = DataFrame(Timestamp('20010101').as_unit('ns'), index=df_float.index, columns=range(3))
df = pd.concat([df_float, df_int, df_bool, df_object, df_dt], axis=1, ignore_index=True)
df.columns = [0, 1, 2] * 5
with tm.ensure_clean() as filename:
    df.to_csv(filename)
    result = read_csv(filename, index_col=0)
    for i in ['0.4', '1.4', '2.4']:
        result[i] = to_datetime(result[i])
    result.columns = df.columns
    tm.assert_frame_equal(result, df)
```

## Next Steps


---

*Source: test_to_csv.py:769 | Complexity: Advanced | Last updated: 2026-06-02*