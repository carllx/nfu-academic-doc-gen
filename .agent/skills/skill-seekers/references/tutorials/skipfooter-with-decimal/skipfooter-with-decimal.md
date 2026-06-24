# How To: Skipfooter With Decimal

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test skipfooter with decimal

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
# Fixtures: python_parser_only, add_footer
```

## Step-by-Step Guide

### Step 1: Assign data = '1#2\n3#4'

```python
data = '1#2\n3#4'
```

### Step 2: Assign parser = python_parser_only

```python
parser = python_parser_only
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1.2, 3.4]})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), names=['a'], decimal='#', **kwargs)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign kwargs = value

```python
kwargs = {'skipfooter': 1}
```

### Step 7: Assign kwargs = value

```python
kwargs = {}
```


## Complete Example

```python
# Setup
# Fixtures: python_parser_only, add_footer

# Workflow
data = '1#2\n3#4'
parser = python_parser_only
expected = DataFrame({'a': [1.2, 3.4]})
if add_footer:
    kwargs = {'skipfooter': 1}
    data += '\nFooter'
else:
    kwargs = {}
result = parser.read_csv(StringIO(data), names=['a'], decimal='#', **kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_python_parser_only.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*