# How To: Custom Comment Char

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test custom comment char

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
# Fixtures: all_parsers, comment_char
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c\n1,2,3#ignore this!\n4,5,6#ignorethistoo'

```python
data = 'a,b,c\n1,2,3#ignore this!\n4,5,6#ignorethistoo'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data.replace('#', comment_char)), comment=comment_char)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "The 'comment' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'comment' option is not supported with the 'pyarrow' engine"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data.replace('#', comment_char)), comment=comment_char)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, comment_char

# Workflow
parser = all_parsers
data = 'a,b,c\n1,2,3#ignore this!\n4,5,6#ignorethistoo'
if parser.engine == 'pyarrow':
    msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data.replace('#', comment_char)), comment=comment_char)
    return
result = parser.read_csv(StringIO(data.replace('#', comment_char)), comment=comment_char)
expected = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_comment.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*