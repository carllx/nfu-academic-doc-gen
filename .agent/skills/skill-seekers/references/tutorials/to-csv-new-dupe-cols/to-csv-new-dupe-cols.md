# How To: To Csv New Dupe Cols

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to csv new dupe cols

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: cols
```

## Step-by-Step Guide

### Step 1: Assign chunksize = 5

```python
chunksize = 5
```

### Step 2: Assign N = int(...)

```python
N = int(chunksize * 2.5)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((N, 3)), index=Index([f'i-{i}' for i in range(N)], name='a'), columns=['a', 'a', 'b'])
```

### Step 4: Call df.to_csv()

```python
df.to_csv(path, columns=cols, chunksize=chunksize)
```

### Step 5: Assign rs_c = read_csv(...)

```python
rs_c = read_csv(path, index_col=0)
```

### Step 6: Assign rs_c.columns = value

```python
rs_c.columns = df.columns
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, rs_c, check_names=False)
```

### Step 8: Assign rs_c.columns = cols

```python
rs_c.columns = cols
```

### Step 9: Assign unknown = df.columns.get_indexer_non_unique(...)

```python
indexer, missing = df.columns.get_indexer_non_unique(cols)
```

### Step 10: Assign rs_c.columns = df.columns.take(...)

```python
rs_c.columns = df.columns.take(indexer)
```

### Step 11: Assign obj_df = value

```python
obj_df = df[c]
```

### Step 12: Assign obj_rs = value

```python
obj_rs = rs_c[c]
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(obj_df, obj_rs)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(obj_df, obj_rs, check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: cols

# Workflow
chunksize = 5
N = int(chunksize * 2.5)
df = DataFrame(np.ones((N, 3)), index=Index([f'i-{i}' for i in range(N)], name='a'), columns=['a', 'a', 'b'])
with tm.ensure_clean() as path:
    df.to_csv(path, columns=cols, chunksize=chunksize)
    rs_c = read_csv(path, index_col=0)
    if cols is not None:
        if df.columns.is_unique:
            rs_c.columns = cols
        else:
            indexer, missing = df.columns.get_indexer_non_unique(cols)
            rs_c.columns = df.columns.take(indexer)
        for c in cols:
            obj_df = df[c]
            obj_rs = rs_c[c]
            if isinstance(obj_df, Series):
                tm.assert_series_equal(obj_df, obj_rs)
            else:
                tm.assert_frame_equal(obj_df, obj_rs, check_names=False)
    else:
        rs_c.columns = df.columns
        tm.assert_frame_equal(df, rs_c, check_names=False)
```

## Next Steps


---

*Source: test_to_csv.py:174 | Complexity: Advanced | Last updated: 2026-06-02*