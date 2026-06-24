# How To: To Csv Cols Reordering

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv cols reordering

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
df = DataFrame(np.ones((N, 3)), index=Index([f'i-{i}' for i in range(N)], name='a'), columns=Index([f'i-{i}' for i in range(3)], name='a'))
```

### Step 4: Assign cs = value

```python
cs = df.columns
```

### Step 5: Assign cols = value

```python
cols = [cs[2], cs[0]]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df[cols], rs_c, check_names=False)
```

### Step 7: Call df.to_csv()

```python
df.to_csv(path, columns=cols, chunksize=chunksize)
```

### Step 8: Assign rs_c = read_csv(...)

```python
rs_c = read_csv(path, index_col=0)
```


## Complete Example

```python
# Workflow
chunksize = 5
N = int(chunksize * 2.5)
df = DataFrame(np.ones((N, 3)), index=Index([f'i-{i}' for i in range(N)], name='a'), columns=Index([f'i-{i}' for i in range(3)], name='a'))
cs = df.columns
cols = [cs[2], cs[0]]
with tm.ensure_clean() as path:
    df.to_csv(path, columns=cols, chunksize=chunksize)
    rs_c = read_csv(path, index_col=0)
tm.assert_frame_equal(df[cols], rs_c, check_names=False)
```

## Next Steps


---

*Source: test_to_csv.py:154 | Complexity: Advanced | Last updated: 2026-06-02*