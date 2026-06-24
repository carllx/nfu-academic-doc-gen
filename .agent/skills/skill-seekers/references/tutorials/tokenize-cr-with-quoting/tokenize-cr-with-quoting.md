# How To: Tokenize Cr With Quoting

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tokenize CR with quoting

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

### Step 2: Assign data = ' a,b,c\r"a,b","e,d","f,f"'

```python
data = ' a,b,c\r"a,b","e,d","f,f"'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), header=None)
```

### Step 4: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data.replace('\r', '\n')), header=None)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data))
```

### Step 7: Assign expected = parser.read_csv(...)

```python
expected = parser.read_csv(StringIO(data.replace('\r', '\n')))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only

# Workflow
parser = c_parser_only
data = ' a,b,c\r"a,b","e,d","f,f"'
result = parser.read_csv(StringIO(data), header=None)
expected = parser.read_csv(StringIO(data.replace('\r', '\n')), header=None)
tm.assert_frame_equal(result, expected)
result = parser.read_csv(StringIO(data))
expected = parser.read_csv(StringIO(data.replace('\r', '\n')))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_c_parser_only.py:280 | Complexity: Advanced | Last updated: 2026-06-02*