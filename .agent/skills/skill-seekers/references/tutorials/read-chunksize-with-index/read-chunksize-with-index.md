# How To: Read Chunksize With Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read chunksize with index

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
# Fixtures: all_parsers, index_col
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'

```python
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([['foo', 2, 3, 4, 5], ['bar', 7, 8, 9, 10], ['baz', 12, 13, 14, 15], ['qux', 12, 13, 14, 15], ['foo2', 12, 13, 14, 15], ['bar2', 12, 13, 14, 15]], columns=['index', 'A', 'B', 'C', 'D'])
```

### Step 4: Assign expected = expected.set_index(...)

```python
expected = expected.set_index('index')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunks[0], expected[:2])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunks[1], expected[2:4])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunks[2], expected[4:])
```

### Step 8: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 9: Assign chunks = list(...)

```python
chunks = list(reader)
```

### Step 10: Call list()

```python
list(reader)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, index_col

# Workflow
parser = all_parsers
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
expected = DataFrame([['foo', 2, 3, 4, 5], ['bar', 7, 8, 9, 10], ['baz', 12, 13, 14, 15], ['qux', 12, 13, 14, 15], ['foo2', 12, 13, 14, 15], ['bar2', 12, 13, 14, 15]], columns=['index', 'A', 'B', 'C', 'D'])
expected = expected.set_index('index')
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with parser.read_csv(StringIO(data), index_col=0, chunksize=2) as reader:
            list(reader)
    return
with parser.read_csv(StringIO(data), index_col=0, chunksize=2) as reader:
    chunks = list(reader)
tm.assert_frame_equal(chunks[0], expected[:2])
tm.assert_frame_equal(chunks[1], expected[2:4])
tm.assert_frame_equal(chunks[2], expected[4:])
```

## Next Steps


---

*Source: test_chunksize.py:25 | Complexity: Advanced | Last updated: 2026-06-02*