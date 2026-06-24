# How To: Usecols Index Col Conflict

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols index col conflict

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, usecols, index_col, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'

```python
data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': [1, 2]}, index=Index(['a', 'b'], name='b'))
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols, index_col=index_col)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), usecols=usecols, index_col=index_col)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, usecols, index_col, request

# Workflow
parser = all_parsers
data = 'a,b,c,d\nA,a,1,one\nB,b,2,two'
if parser.engine == 'pyarrow' and isinstance(usecols[0], int):
    with pytest.raises(ValueError, match=_msg_pyarrow_requires_names):
        parser.read_csv(StringIO(data), usecols=usecols, index_col=index_col)
    return
expected = DataFrame({'c': [1, 2]}, index=Index(['a', 'b'], name='b'))
result = parser.read_csv(StringIO(data), usecols=usecols, index_col=index_col)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*