# How To: Get Chunk Passed Chunksize

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get chunk passed chunksize

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C\n1,2,3\n4,5,6\n7,8,9\n1,2,3'

```python
data = 'A,B,C\n1,2,3\n4,5,6\n7,8,9\n1,2,3'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 6: Assign result = reader.get_chunk(...)

```python
result = reader.get_chunk()
```

### Step 7: Call reader.get_chunk()

```python
reader.get_chunk()
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'A,B,C\n1,2,3\n4,5,6\n7,8,9\n1,2,3'
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with parser.read_csv(StringIO(data), chunksize=2) as reader:
            reader.get_chunk()
    return
with parser.read_csv(StringIO(data), chunksize=2) as reader:
    result = reader.get_chunk()
expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_chunksize.py:135 | Complexity: Intermediate | Last updated: 2026-06-02*