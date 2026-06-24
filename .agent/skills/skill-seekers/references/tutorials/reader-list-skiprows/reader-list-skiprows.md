# How To: Reader List Skiprows

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reader list skiprows

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

### Step 4: Assign lines = list(...)

```python
lines = list(csv.reader(StringIO(data)))
```

### Step 5: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data), **kwargs)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(chunks[0], expected[1:3])
```

### Step 7: Assign chunks = list(...)

```python
chunks = list(reader)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'index,A,B,C,D\nfoo,2,3,4,5\nbar,7,8,9,10\nbaz,12,13,14,15\nqux,12,13,14,15\nfoo2,12,13,14,15\nbar2,12,13,14,15\n'
parser = all_parsers
kwargs = {'index_col': 0}
lines = list(csv.reader(StringIO(data)))
with TextParser(lines, chunksize=2, skiprows=[1], **kwargs) as reader:
    chunks = list(reader)
expected = parser.read_csv(StringIO(data), **kwargs)
tm.assert_frame_equal(chunks[0], expected[1:3])
```

## Next Steps


---

*Source: test_data_list.py:60 | Complexity: Intermediate | Last updated: 2026-06-02*