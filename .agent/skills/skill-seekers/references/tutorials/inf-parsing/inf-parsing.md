# How To: Inf Parsing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test inf parsing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, na_filter
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = ',A\na,inf\nb,-inf\nc,+Inf\nd,-Inf\ne,INF\nf,-INF\ng,+INf\nh,-INf\ni,inF\nj,-inF'

```python
data = ',A\na,inf\nb,-inf\nc,+Inf\nd,-Inf\ne,INF\nf,-INF\ng,+INf\nh,-INf\ni,inF\nj,-inF'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [float('inf'), float('-inf')] * 5}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=0, na_filter=na_filter)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, na_filter

# Workflow
parser = all_parsers
data = ',A\na,inf\nb,-inf\nc,+Inf\nd,-Inf\ne,INF\nf,-INF\ng,+INf\nh,-INf\ni,inF\nj,-inF'
expected = DataFrame({'A': [float('inf'), float('-inf')] * 5}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
result = parser.read_csv(StringIO(data), index_col=0, na_filter=na_filter)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_inf.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*