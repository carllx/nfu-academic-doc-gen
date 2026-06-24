# How To: Read Chunksize And Nrows

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read chunksize and nrows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, chunksize
```

## Step-by-Step Guide

### Step 1: Assign data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'

```python
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign kwargs = value

```python
kwargs = {'index_col': 0, 'nrows': 5}
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data), **kwargs)
```

### Step 5: Assign msg = "The 'nrows' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concat(reader), expected)
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, chunksize

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
parser = all_parsers
kwargs = {'index_col': 0, 'nrows': 5}
if parser.engine == 'pyarrow':
    msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), **kwargs)
    return
expected = parser.read_csv(StringIO(data), **kwargs)
with parser.read_csv(StringIO(data), chunksize=chunksize, **kwargs) as reader:
    tm.assert_frame_equal(concat(reader), expected)
```

## Next Steps


---

*Source: test_chunksize.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*