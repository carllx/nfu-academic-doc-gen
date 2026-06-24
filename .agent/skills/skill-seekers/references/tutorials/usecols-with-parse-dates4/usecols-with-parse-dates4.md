# How To: Usecols With Parse Dates4

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols with parse dates4

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

### Step 1: Assign data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'

```python
data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'
```

### Step 2: Assign usecols = list(...)

```python
usecols = list('abcdefghij')
```

### Step 3: Assign parse_dates = value

```python
parse_dates = [[0, 1]]
```

### Step 4: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 5: Assign cols = value

```python
cols = {'a_b': '2016/09/21 1', 'c': [1], 'd': [2], 'e': [3], 'f': [4], 'g': [5], 'h': [6], 'i': [7], 'j': [8]}
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, columns=['a_b'] + list('cdefghij'))
```

### Step 7: Assign depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"

```python
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'
usecols = list('abcdefghij')
parse_dates = [[0, 1]]
parser = all_parsers
cols = {'a_b': '2016/09/21 1', 'c': [1], 'd': [2], 'e': [3], 'f': [4], 'g': [5], 'h': [6], 'i': [7], 'j': [8]}
expected = DataFrame(cols, columns=['a_b'] + list('cdefghij'))
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
with tm.assert_produces_warning((FutureWarning, DeprecationWarning), match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:125 | Complexity: Advanced | Last updated: 2026-06-02*