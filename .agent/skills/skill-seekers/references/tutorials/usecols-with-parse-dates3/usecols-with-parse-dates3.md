# How To: Usecols With Parse Dates3

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols with parse dates3

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'

```python
data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'
```

### Step 3: Assign usecols = list(...)

```python
usecols = list('abcdefghij')
```

### Step 4: Assign parse_dates = value

```python
parse_dates = [0]
```

### Step 5: Assign cols = value

```python
cols = {'a': Timestamp('2016-09-21').as_unit('ns'), 'b': [1], 'c': [1], 'd': [2], 'e': [3], 'f': [4], 'g': [5], 'h': [6], 'i': [7], 'j': [8]}
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, columns=usecols)
```

### Step 7: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8'
usecols = list('abcdefghij')
parse_dates = [0]
cols = {'a': Timestamp('2016-09-21').as_unit('ns'), 'b': [1], 'c': [1], 'd': [2], 'e': [3], 'f': [4], 'g': [5], 'h': [6], 'i': [7], 'j': [8]}
expected = DataFrame(cols, columns=usecols)
result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:98 | Complexity: Advanced | Last updated: 2026-06-02*