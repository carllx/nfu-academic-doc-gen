# How To: Comment First Line

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comment first line

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, header
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '# notes\na,b,c\n# more notes\n1,2,3'

```python
data = '# notes\na,b,c\n# more notes\n1,2,3'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), comment='#', header=header)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: ['a', '1'], 1: ['b', '2'], 2: ['c', '3']})
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
```

### Step 7: Assign msg = "The 'comment' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'comment' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), comment='#', header=header)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, header

# Workflow
parser = all_parsers
data = '# notes\na,b,c\n# more notes\n1,2,3'
if header is None:
    expected = DataFrame({0: ['a', '1'], 1: ['b', '2'], 2: ['c', '3']})
else:
    expected = DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
if parser.engine == 'pyarrow':
    msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), comment='#', header=header)
    return
result = parser.read_csv(StringIO(data), comment='#', header=header)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_comment.py:179 | Complexity: Advanced | Last updated: 2026-06-02*