# How To: Valid File Buffer Seems Invalid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test valid file buffer seems invalid

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `platform`
- `urllib.error`
- `uuid`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'a\n1'

```python
data = 'a\n1'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1]})
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(NoSeekTellBuffer(data))
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
class NoSeekTellBuffer(StringIO):

    def tell(self):
        raise AttributeError('No tell method')

    def seek(self, pos, whence=0):
        raise AttributeError('No seek method')
data = 'a\n1'
parser = all_parsers
expected = DataFrame({'a': [1]})
result = parser.read_csv(NoSeekTellBuffer(data))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_file_buffer_url.py:345 | Complexity: Intermediate | Last updated: 2026-06-02*