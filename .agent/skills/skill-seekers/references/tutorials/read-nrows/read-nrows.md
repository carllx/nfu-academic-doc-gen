# How To: Read Nrows

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read nrows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`

**Setup Required:**
```python
# Fixtures: all_parsers, nrows
```

## Step-by-Step Guide

### Step 1: Assign data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'

```python
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([['foo', 2, 3, 4, 5], ['bar', 7, 8, 9, 10], ['baz', 12, 13, 14, 15]], columns=['index', 'A', 'B', 'C', 'D'])
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), nrows=nrows)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The 'nrows' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), nrows=nrows)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, nrows

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
expected = DataFrame([['foo', 2, 3, 4, 5], ['bar', 7, 8, 9, 10], ['baz', 12, 13, 14, 15]], columns=['index', 'A', 'B', 'C', 'D'])
parser = all_parsers
if parser.engine == 'pyarrow':
    msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), nrows=nrows)
    return
result = parser.read_csv(StringIO(data), nrows=nrows)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*