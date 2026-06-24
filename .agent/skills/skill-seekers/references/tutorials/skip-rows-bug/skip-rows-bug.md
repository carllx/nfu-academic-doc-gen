# How To: Skip Rows Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test skip rows bug

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, skiprows
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign text = '#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n1/1/2000,1.,2.,3.\n1/2/2000,4,5,6\n1/3/2000,7,8,9\n'

```python
text = '#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n1/1/2000,1.,2.,3.\n1/2/2000,4,5,6\n1/3/2000,7,8,9\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(text), skiprows=skiprows, header=None, index_col=0, parse_dates=True)
```

### Step 4: Assign index = Index(...)

```python
index = Index([datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)], name=0)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.arange(1.0, 10.0).reshape((3, 3)), columns=[1, 2, 3], index=index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, skiprows

# Workflow
parser = all_parsers
text = '#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n#foo,a,b,c\n1/1/2000,1.,2.,3.\n1/2/2000,4,5,6\n1/3/2000,7,8,9\n'
result = parser.read_csv(StringIO(text), skiprows=skiprows, header=None, index_col=0, parse_dates=True)
index = Index([datetime(2000, 1, 1), datetime(2000, 1, 2), datetime(2000, 1, 3)], name=0)
expected = DataFrame(np.arange(1.0, 10.0).reshape((3, 3)), columns=[1, 2, 3], index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_skiprows.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*