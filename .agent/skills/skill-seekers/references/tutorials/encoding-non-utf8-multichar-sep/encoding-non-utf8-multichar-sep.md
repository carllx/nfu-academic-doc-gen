# How To: Encoding Non Utf8 Multichar Sep

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test encoding non utf8 multichar sep

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
# Fixtures: python_parser_only, sep, encoding
```

## Step-by-Step Guide

### Step 1: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1], 'b': [2]})
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign data = value

```python
data = '1' + sep + '2'
```

### Step 4: Assign encoded_data = data.encode(...)

```python
encoded_data = data.encode(encoding)
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(BytesIO(encoded_data), sep=sep, names=['a', 'b'], encoding=encoding)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only, sep, encoding

# Workflow
expected = DataFrame({'a': [1], 'b': [2]})
parser = python_parser_only
data = '1' + sep + '2'
encoded_data = data.encode(encoding)
result = parser.read_csv(BytesIO(encoded_data), sep=sep, names=['a', 'b'], encoding=encoding)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*