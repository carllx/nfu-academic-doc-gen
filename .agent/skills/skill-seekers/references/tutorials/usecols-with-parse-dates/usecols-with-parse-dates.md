# How To: Usecols With Parse Dates

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test usecols with parse dates

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, usecols
```

## Step-by-Step Guide

### Step 1: Assign data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'

```python
data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign parse_dates = value

```python
parse_dates = [[1, 2]]
```

### Step 4: Assign depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"

```python
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
```

### Step 5: Assign cols = value

```python
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, columns=['c_d', 'a'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
```

### Step 9: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, usecols

# Workflow
data = 'a,b,c,d,e\n0,1,2014-01-01,09:00,4\n0,1,2014-01-02,10:00,4'
parser = all_parsers
parse_dates = [[1, 2]]
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
cols = {'a': [0, 0], 'c_d': [Timestamp('2014-01-01 09:00:00'), Timestamp('2014-01-02 10:00:00')]}
expected = DataFrame(cols, columns=['c_d', 'a'])
if parser.engine == 'pyarrow':
    with pytest.raises(ValueError, match=_msg_pyarrow_requires_names):
        with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
            parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
    return
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:29 | Complexity: Advanced | Last updated: 2026-06-02*