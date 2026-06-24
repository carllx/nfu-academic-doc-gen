# How To: Usecols With Single Byte Unicode Strings

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols with single byte unicode strings

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'A,B,C,D\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'

```python
data = 'A,B,C,D\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign exp_data = value

```python
exp_data = {'A': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'B': {0: 8, 1: 2, 2: 7}}
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(exp_data)
```

### Step 5: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=['A', 'B'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'A,B,C,D\n0.056674973,8,True,a\n2.613230982,2,False,b\n3.568935038,7,False,a'
parser = all_parsers
exp_data = {'A': {0: 0.056674973, 1: 2.6132309819999997, 2: 3.5689350380000002}, 'B': {0: 8, 1: 2, 2: 7}}
expected = DataFrame(exp_data)
result = parser.read_csv(StringIO(data), usecols=['A', 'B'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_strings.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*