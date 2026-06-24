# How To: Read Csv Buglet 4X Multi Index2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv buglet 4x multi index2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `csv`
- `io`
- `typing`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `collections.abc`

**Setup Required:**
```python
# Fixtures: python_parser_only
```

## Step-by-Step Guide

### Step 1: Assign data = '      A B C\na b c\n1 3 7 0 3 6\n3 1 4 1 5 9'

```python
data = '      A B C\na b c\n1 3 7 0 3 6\n3 1 4 1 5 9'
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign expected = DataFrame.from_records(...)

```python
expected = DataFrame.from_records([(1, 3, 7, 0, 3, 6), (3, 1, 4, 1, 5, 9)], columns=list('abcABC'), index=list('abc'))
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep='\\s+')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only

# Workflow
data = '      A B C\na b c\n1 3 7 0 3 6\n3 1 4 1 5 9'
parser = python_parser_only
expected = DataFrame.from_records([(1, 3, 7, 0, 3, 6), (3, 1, 4, 1, 5, 9)], columns=list('abcABC'), index=list('abc'))
result = parser.read_csv(StringIO(data), sep='\\s+')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*