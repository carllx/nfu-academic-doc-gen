# How To: Header Not First Line

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test header not first line

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'got,to,ignore,this,line\ngot,to,ignore,this,line\nindex,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'

```python
data = 'got,to,ignore,this,line\ngot,to,ignore,this,line\nindex,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'
```

### Step 3: Assign data2 = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'

```python
data2 = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=2, index_col=0)
```

### Step 5: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data2), header=0, index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'got,to,ignore,this,line\ngot,to,ignore,this,line\nindex,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'
data2 = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\n'
result = parser.read_csv(StringIO(data), header=2, index_col=0)
expected = parser.read_csv(StringIO(data2), header=0, index_col=0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_header.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*