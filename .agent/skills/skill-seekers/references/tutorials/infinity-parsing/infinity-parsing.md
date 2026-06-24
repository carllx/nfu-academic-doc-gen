# How To: Infinity Parsing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test infinity parsing

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

### Step 2: Assign data = ',A\na,Infinity\nb,-Infinity\nc,+Infinity\n'

```python
data = ',A\na,Infinity\nb,-Infinity\nc,+Infinity\n'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [float('infinity'), float('-infinity'), float('+infinity')]}, index=['a', 'b', 'c'])
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
data = ',A\na,Infinity\nb,-Infinity\nc,+Infinity\n'
expected = DataFrame({'A': [float('infinity'), float('-infinity'), float('+infinity')]}, index=['a', 'b', 'c'])
result = parser.read_csv(StringIO(data), index_col=0, na_filter=na_filter)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_inf.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*