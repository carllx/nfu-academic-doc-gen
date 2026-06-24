# How To: Read Chunksize And Nrows Changing Size

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read chunksize and nrows changing size

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
# Fixtures: all_parsers
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
tm.assert_frame_equal(reader.get_chunk(size=2), expected.iloc[:2])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(reader.get_chunk(size=4), expected.iloc[2:5])
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), **kwargs)
```

### Step 9: Call reader.get_chunk()

```python
reader.get_chunk(size=3)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

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
with parser.read_csv(StringIO(data), chunksize=8, **kwargs) as reader:
    tm.assert_frame_equal(reader.get_chunk(size=2), expected.iloc[:2])
    tm.assert_frame_equal(reader.get_chunk(size=4), expected.iloc[2:5])
    with pytest.raises(StopIteration, match=''):
        reader.get_chunk(size=3)
```

## Next Steps


---

*Source: test_chunksize.py:108 | Complexity: Advanced | Last updated: 2026-06-02*