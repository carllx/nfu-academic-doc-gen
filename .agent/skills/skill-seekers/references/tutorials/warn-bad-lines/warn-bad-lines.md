# How To: Warn Bad Lines

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test warn bad lines

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

### Step 4: Assign match_msg = 'Skipping line'

```python
match_msg = 'Skipping line'
```

### Step 5: Assign expected_warning = ParserWarning

```python
expected_warning = ParserWarning
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign match_msg = 'Expected 1 columns, but found 3: 1,2,3'

```python
match_msg = 'Expected 1 columns, but found 3: 1,2,3'
```

### Step 8: Assign expected_warning = value

```python
expected_warning = (ParserWarning, DeprecationWarning)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), on_bad_lines='warn')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a\n1\n1,2,3\n4\n5,6,7'
expected = DataFrame({'a': [1, 4]})
match_msg = 'Skipping line'
expected_warning = ParserWarning
if parser.engine == 'pyarrow':
    match_msg = 'Expected 1 columns, but found 3: 1,2,3'
    expected_warning = (ParserWarning, DeprecationWarning)
with tm.assert_produces_warning(expected_warning, match=match_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), on_bad_lines='warn')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_errors.py:185 | Complexity: Advanced | Last updated: 2026-06-02*