# How To: Chunked Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test chunked categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`

**Setup Required:**
```python
# Fixtures: version
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'cats': Series(['a', 'b', 'a', 'b', 'c'], dtype='category')})
```

**Verification:**
```python
assert 'cats' in block
```

### Step 2: Assign df.index.name = 'index'

```python
df.index.name = 'index'
```

### Step 3: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 4: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(np.int32)
```

### Step 5: Call df.to_stata()

```python
df.to_stata(path, version=version)
```

### Step 6: Assign block = block.set_index(...)

```python
block = block.set_index('index')
```

**Verification:**
```python
assert 'cats' in block
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(block.cats, expected.cats.iloc[2 * i:2 * (i + 1)])
```


## Complete Example

```python
# Setup
# Fixtures: version

# Workflow
df = DataFrame({'cats': Series(['a', 'b', 'a', 'b', 'c'], dtype='category')})
df.index.name = 'index'
expected = df.copy()
expected.index = expected.index.astype(np.int32)
with tm.ensure_clean() as path:
    df.to_stata(path, version=version)
    with StataReader(path, chunksize=2, order_categoricals=False) as reader:
        for i, block in enumerate(reader):
            block = block.set_index('index')
            assert 'cats' in block
            tm.assert_series_equal(block.cats, expected.cats.iloc[2 * i:2 * (i + 1)])
```

## Next Steps


---

*Source: test_stata.py:2106 | Complexity: Intermediate | Last updated: 2026-06-02*