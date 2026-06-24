# How To: Comment Char In Default Value

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comment char in default value

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
# Fixtures: all_parsers, request
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '# this is a comment\ncol1,col2,col3,col4\n1,2,3,4#inline comment\n4,5#,6,10\n7,8,#N/A,11\n'

```python
data = '# this is a comment\ncol1,col2,col3,col4\n1,2,3,4#inline comment\n4,5#,6,10\n7,8,#N/A,11\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), comment='#', na_values='#N/A')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col1': [1, 4, 7], 'col2': [2, 5, 8], 'col3': [3.0, np.nan, np.nan], 'col4': [4.0, np.nan, 11.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign reason = 'see gh-34002: works on the python engine but not the c engine'

```python
reason = 'see gh-34002: works on the python engine but not the c engine'
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason=reason, raises=AssertionError))
```

### Step 8: Assign msg = "The 'comment' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'comment' option is not supported with the 'pyarrow' engine"
```

### Step 9: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), comment='#', na_values='#N/A')
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, request

# Workflow
if all_parsers.engine == 'c':
    reason = 'see gh-34002: works on the python engine but not the c engine'
    request.applymarker(pytest.mark.xfail(reason=reason, raises=AssertionError))
parser = all_parsers
data = '# this is a comment\ncol1,col2,col3,col4\n1,2,3,4#inline comment\n4,5#,6,10\n7,8,#N/A,11\n'
if parser.engine == 'pyarrow':
    msg = "The 'comment' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), comment='#', na_values='#N/A')
    return
result = parser.read_csv(StringIO(data), comment='#', na_values='#N/A')
expected = DataFrame({'col1': [1, 4, 7], 'col2': [2, 5, 8], 'col3': [3.0, np.nan, np.nan], 'col4': [4.0, np.nan, 11.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_comment.py:198 | Complexity: Advanced | Last updated: 2026-06-02*