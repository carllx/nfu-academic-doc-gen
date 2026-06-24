# How To: Iterator

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iterator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
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
kwargs = {'index_col': 0}
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data), **kwargs)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(last_chunk, expected[3:])
```

### Step 6: Assign msg = "The 'iterator' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'iterator' option is not supported with the 'pyarrow' engine"
```

### Step 7: Assign first_chunk = reader.read(...)

```python
first_chunk = reader.read(3)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(first_chunk, expected[:3])
```

### Step 9: Assign last_chunk = reader.read(...)

```python
last_chunk = reader.read(5)
```

### Step 10: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), iterator=True, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
parser = all_parsers
kwargs = {'index_col': 0}
expected = parser.read_csv(StringIO(data), **kwargs)
if parser.engine == 'pyarrow':
    msg = "The 'iterator' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), iterator=True, **kwargs)
    return
with parser.read_csv(StringIO(data), iterator=True, **kwargs) as reader:
    first_chunk = reader.read(3)
    tm.assert_frame_equal(first_chunk, expected[:3])
    last_chunk = reader.read(5)
tm.assert_frame_equal(last_chunk, expected[3:])
```

## Next Steps


---

*Source: test_iterator.py:20 | Complexity: Advanced | Last updated: 2026-06-02*