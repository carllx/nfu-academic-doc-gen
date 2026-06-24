# How To: Default Separator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default separator

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

### Step 1: Assign data = 'aob\n1o2\n3o4'

```python
data = 'aob\n1o2\n3o4'
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 3], 'b': [2, 4]})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), sep=None)
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
data = 'aob\n1o2\n3o4'
parser = python_parser_only
expected = DataFrame({'a': [1, 3], 'b': [2, 4]})
result = parser.read_csv(StringIO(data), sep=None)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*