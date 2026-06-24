# How To: Custom Lineterminator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom lineterminator

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only
```

## Step-by-Step Guide

### Step 1: Assign parser = c_parser_only

```python
parser = c_parser_only
```

### Step 2: Assign data = 'a,b,c~1,2,3~4,5,6'

```python
data = 'a,b,c~1,2,3~4,5,6'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), lineterminator='~')
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data.replace('~', '\n')))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only

# Workflow
parser = c_parser_only
data = 'a,b,c~1,2,3~4,5,6'
result = parser.read_csv(StringIO(data), lineterminator='~')
expected = parser.read_csv(StringIO(data.replace('~', '\n')))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_c_parser_only.py:236 | Complexity: Intermediate | Last updated: 2026-06-02*