# How To: Comment Header

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comment header

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '# empty\n# second empty line\n1,2,3\nA,B,C\n1,2.,4.\n5.,NaN,10.0\n'

```python
data = '# empty\n# second empty line\n1,2,3\nA,B,C\n1,2.,4.\n5.,NaN,10.0\n'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=['A', 'B', 'C'])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), comment='#', header=1)
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
parser.read_csv(StringIO(data), comment='#', header=1)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '# empty\n# second empty line\n1,2,3\nA,B,C\n1,2.,4.\n5.,NaN,10.0\n'
expected = DataFrame([[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=['A', 'B', 'C'])
if parser.engine == 'pyarrow':
    msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), comment='#', header=1)
    return
result = parser.read_csv(StringIO(data), comment='#', header=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_comment.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*