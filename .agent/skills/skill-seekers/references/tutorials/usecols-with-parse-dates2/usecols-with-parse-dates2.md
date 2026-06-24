# How To: Usecols With Parse Dates2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols with parse dates2

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

### Step 2: Assign data = '2008-02-07 09:40,1032.43\n2008-02-07 09:50,1042.54\n2008-02-07 10:00,1051.65'

```python
data = '2008-02-07 09:40,1032.43\n2008-02-07 09:50,1042.54\n2008-02-07 10:00,1051.65'
```

### Step 3: Assign names = value

```python
names = ['date', 'values']
```

### Step 4: Assign usecols = value

```python
usecols = names[:]
```

### Step 5: Assign parse_dates = value

```python
parse_dates = [0]
```

### Step 6: Assign index = Index(...)

```python
index = Index([Timestamp('2008-02-07 09:40'), Timestamp('2008-02-07 09:50'), Timestamp('2008-02-07 10:00')], name='date')
```

### Step 7: Assign cols = value

```python
cols = {'values': [1032.43, 1042.54, 1051.65]}
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(cols, index=index)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), parse_dates=parse_dates, index_col=0, usecols=usecols, header=None, names=names)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '2008-02-07 09:40,1032.43\n2008-02-07 09:50,1042.54\n2008-02-07 10:00,1051.65'
names = ['date', 'values']
usecols = names[:]
parse_dates = [0]
index = Index([Timestamp('2008-02-07 09:40'), Timestamp('2008-02-07 09:50'), Timestamp('2008-02-07 10:00')], name='date')
cols = {'values': [1032.43, 1042.54, 1051.65]}
expected = DataFrame(cols, index=index)
result = parser.read_csv(StringIO(data), parse_dates=parse_dates, index_col=0, usecols=usecols, header=None, names=names)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:65 | Complexity: Advanced | Last updated: 2026-06-02*