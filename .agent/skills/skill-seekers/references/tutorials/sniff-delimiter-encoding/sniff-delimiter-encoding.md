# How To: Sniff Delimiter Encoding

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sniff delimiter encoding

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
# Fixtures: python_parser_only, encoding
```

## Step-by-Step Guide

### Step 1: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 2: Assign data = 'ignore this\nignore this too\nindex|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'

```python
data = 'ignore this\nignore this too\nindex|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(data, index_col=0, sep=None, skiprows=2, encoding=encoding)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=Index(['foo', 'bar', 'baz'], name='index'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign data = data.encode(...)

```python
data = data.encode(encoding)
```

### Step 7: Assign data = BytesIO(...)

```python
data = BytesIO(data)
```

### Step 8: Assign data = TextIOWrapper(...)

```python
data = TextIOWrapper(data, encoding=encoding)
```

### Step 9: Assign data = StringIO(...)

```python
data = StringIO(data)
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only, encoding

# Workflow
parser = python_parser_only
data = 'ignore this\nignore this too\nindex|A|B|C\nfoo|1|2|3\nbar|4|5|6\nbaz|7|8|9\n'
if encoding is not None:
    data = data.encode(encoding)
    data = BytesIO(data)
    data = TextIOWrapper(data, encoding=encoding)
else:
    data = StringIO(data)
result = parser.read_csv(data, index_col=0, sep=None, skiprows=2, encoding=encoding)
expected = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'], index=Index(['foo', 'bar', 'baz'], name='index'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:105 | Complexity: Advanced | Last updated: 2026-06-02*