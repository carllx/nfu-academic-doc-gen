# How To: Usecols Relative To Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols relative to names

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
# Fixtures: all_parsers, names, usecols
```

## Step-by-Step Guide

### Step 1: Assign data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'

```python
data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), names=names, header=None, usecols=usecols)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=['b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call pytest.skip()

```python
pytest.skip(reason='https://github.com/apache/arrow/issues/38676')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, names, usecols

# Workflow
data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'
parser = all_parsers
if parser.engine == 'pyarrow' and (not isinstance(usecols[0], int)):
    pytest.skip(reason='https://github.com/apache/arrow/issues/38676')
result = parser.read_csv(StringIO(data), names=names, header=None, usecols=usecols)
expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=['b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_usecols_basic.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*