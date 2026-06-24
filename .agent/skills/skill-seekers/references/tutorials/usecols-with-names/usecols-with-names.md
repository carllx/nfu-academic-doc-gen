# How To: Usecols With Names

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols with names

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'

```python
data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign names = value

```python
names = ['foo', 'bar']
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), names=names, usecols=[1, 2], header=0)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=names)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), names=names, usecols=[1, 2], header=0)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'
parser = all_parsers
names = ['foo', 'bar']
if parser.engine == 'pyarrow':
    with pytest.raises(ValueError, match=_msg_pyarrow_requires_names):
        parser.read_csv(StringIO(data), names=names, usecols=[1, 2], header=0)
    return
result = parser.read_csv(StringIO(data), names=names, usecols=[1, 2], header=0)
expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=names)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*