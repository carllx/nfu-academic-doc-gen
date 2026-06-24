# How To: Usecols With Parse Dates And Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols with parse dates and names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, usecols, names, request
```

## Step-by-Step Guide

### Step 1: Assign s = '0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'

```python
s = '0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
```

### Step 2: Assign parse_dates = value

```python
parse_dates = [[1, 2]]
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign cols = value

```python
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, columns=['c_d', 'a'])
```

### Step 6: Assign depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"

```python
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Length mismatch in some cases, UserWarning in other')
```

### Step 9: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 10: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(s), names=names, parse_dates=parse_dates, usecols=usecols)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, usecols, names, request

# Workflow
s = '0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
parse_dates = [[1, 2]]
parser = all_parsers
if parser.engine == 'pyarrow' and (not (len(names) == 3 and usecols[0] == 0)):
    mark = pytest.mark.xfail(reason='Length mismatch in some cases, UserWarning in other')
    request.applymarker(mark)
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
expected = DataFrame(cols, columns=['c_d', 'a'])
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
with tm.assert_produces_warning((FutureWarning, DeprecationWarning), match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(s), names=names, parse_dates=parse_dates, usecols=usecols)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:166 | Complexity: Advanced | Last updated: 2026-06-02*