# How To: Suppress Error Output

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test suppress error output

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `csv`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
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

### Step 2: Assign data = 'a\n1\n1,2,3\n4\n5,6,7'

```python
data = 'a\n1\n1,2,3\n4\n5,6,7'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 4]})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), on_bad_lines='skip')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a\n1\n1,2,3\n4\n5,6,7'
expected = DataFrame({'a': [1, 4]})
result = parser.read_csv(StringIO(data), on_bad_lines='skip')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_errors.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*