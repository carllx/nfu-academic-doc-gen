# How To: Sniff Delimiter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sniff delimiter

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
# Fixtures: python_parser_only, kwargs
```

## Step-by-Step Guide

### Step 1: Assign data = 'index|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'

```python
data = 'index|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), index_col=0, **kwargs)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=Index(['foo', 'bar', 'baz'], name='index'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only, kwargs

# Workflow
data = 'index|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'
parser = python_parser_only
result = parser.read_csv(StringIO(data), index_col=0, **kwargs)
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=Index(['foo', 'bar', 'baz'], name='index'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*