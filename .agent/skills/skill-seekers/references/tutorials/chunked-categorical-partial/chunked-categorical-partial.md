# How To: Chunked Categorical Partial

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test chunked categorical partial

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
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign dta_file = datapath(...)

```python
dta_file = datapath('io', 'data', 'stata', 'stata-dta-partially-labeled.dta')
```

**Verification:**
```python
assert list(block.cats) == values[2 * i:2 * (i + 1)]
```

### Step 2: Assign values = value

```python
values = ['a', 'b', 'a', 'b', 3.0]
```

### Step 3: Assign direct = read_stata(...)

```python
direct = read_stata(dta_file)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(direct, large_chunk)
```

### Step 5: Assign large_chunk = reader.__next__(...)

```python
large_chunk = reader.__next__()
```

**Verification:**
```python
assert list(block.cats) == values[2 * i:2 * (i + 1)]
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(block.cats.cat.categories, idx)
```

### Step 7: Assign idx = pd.Index(...)

```python
idx = pd.Index(['a', 'b'])
```

### Step 8: Assign idx = pd.Index(...)

```python
idx = pd.Index([3.0], dtype='float64')
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
dta_file = datapath('io', 'data', 'stata', 'stata-dta-partially-labeled.dta')
values = ['a', 'b', 'a', 'b', 3.0]
with StataReader(dta_file, chunksize=2) as reader:
    with tm.assert_produces_warning(CategoricalConversionWarning):
        for i, block in enumerate(reader):
            assert list(block.cats) == values[2 * i:2 * (i + 1)]
            if i < 2:
                idx = pd.Index(['a', 'b'])
            else:
                idx = pd.Index([3.0], dtype='float64')
            tm.assert_index_equal(block.cats.cat.categories, idx)
with tm.assert_produces_warning(CategoricalConversionWarning):
    with StataReader(dta_file, chunksize=5) as reader:
        large_chunk = reader.__next__()
direct = read_stata(dta_file)
tm.assert_frame_equal(direct, large_chunk)
```

## Next Steps


---

*Source: test_stata.py:2124 | Complexity: Advanced | Last updated: 2026-06-02*