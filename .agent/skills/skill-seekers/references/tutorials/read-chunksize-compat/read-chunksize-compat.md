# How To: Read Chunksize Compat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read chunksize compat

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
# Fixtures: all_parsers, kwargs
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

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), **kwargs)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(via_reader, result)
```

### Step 5: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 6: Assign via_reader = concat(...)

```python
via_reader = concat(reader)
```

### Step 7: Call concat()

```python
concat(reader)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, kwargs

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
parser = all_parsers
result = parser.read_csv(StringIO(data), **kwargs)
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with parser.read_csv(StringIO(data), chunksize=2, **kwargs) as reader:
            concat(reader)
    return
with parser.read_csv(StringIO(data), chunksize=2, **kwargs) as reader:
    via_reader = concat(reader)
tm.assert_frame_equal(via_reader, result)
```

## Next Steps


---

*Source: test_chunksize.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*