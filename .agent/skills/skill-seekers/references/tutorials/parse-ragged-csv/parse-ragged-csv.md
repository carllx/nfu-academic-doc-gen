# How To: Parse Ragged Csv

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse ragged csv

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only
```

## Step-by-Step Guide

### Step 1: Assign parser = c_parser_only

```python
parser = c_parser_only
```

### Step 2: Assign data = '1,2,3\n1,2,3,4\n1,2,3,4,5\n1,2\n1,2,3,4'

```python
data = '1,2,3\n1,2,3,4\n1,2,3,4,5\n1,2\n1,2,3,4'
```

### Step 3: Assign nice_data = '1,2,3,,\n1,2,3,4,\n1,2,3,4,5\n1,2,,,\n1,2,3,4,'

```python
nice_data = '1,2,3,,\n1,2,3,4,\n1,2,3,4,5\n1,2,,,\n1,2,3,4,'
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, names=['a', 'b', 'c', 'd', 'e'])
```

### Step 5: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(nice_data), header=None, names=['a', 'b', 'c', 'd', 'e'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign data = '1,2\n3,4,5'

```python
data = '1,2\n3,4,5'
```

### Step 8: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None, names=range(50))
```

### Step 9: Assign expected = parser.read_csv.reindex(...)

```python
expected = parser.read_csv(StringIO(data), header=None, names=range(3)).reindex(columns=range(50))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only

# Workflow
parser = c_parser_only
data = '1,2,3\n1,2,3,4\n1,2,3,4,5\n1,2\n1,2,3,4'
nice_data = '1,2,3,,\n1,2,3,4,\n1,2,3,4,5\n1,2,,,\n1,2,3,4,'
result = parser.read_csv(StringIO(data), header=None, names=['a', 'b', 'c', 'd', 'e'])
expected = parser.read_csv(StringIO(nice_data), header=None, names=['a', 'b', 'c', 'd', 'e'])
tm.assert_frame_equal(result, expected)
data = '1,2\n3,4,5'
result = parser.read_csv(StringIO(data), header=None, names=range(50))
expected = parser.read_csv(StringIO(data), header=None, names=range(3)).reindex(columns=range(50))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_c_parser_only.py:246 | Complexity: Advanced | Last updated: 2026-06-02*