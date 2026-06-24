# How To: Read Data List

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read data list

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `csv`
- `io`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign kwargs = value

```python
kwargs = {'index_col': 0}
```

### Step 3: Assign data = 'A,B,C\nfoo,1,2,3\nbar,4,5,6'

```python
data = 'A,B,C\nfoo,1,2,3\nbar,4,5,6'
```

### Step 4: Assign data_list = value

```python
data_list = [['A', 'B', 'C'], ['foo', '1', '2', '3'], ['bar', '4', '5', '6']]
```

### Step 5: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data), **kwargs)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = parser.read(...)

```python
result = parser.read()
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
kwargs = {'index_col': 0}
data = 'A,B,C\nfoo,1,2,3\nbar,4,5,6'
data_list = [['A', 'B', 'C'], ['foo', '1', '2', '3'], ['bar', '4', '5', '6']]
expected = parser.read_csv(StringIO(data), **kwargs)
with TextParser(data_list, chunksize=2, **kwargs) as parser:
    result = parser.read()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_data_list.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*