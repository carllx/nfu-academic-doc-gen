# How To: Full File

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full file

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.parsers`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign test = 'index                             A    B    C\n2000-01-03T00:00:00  0.980268513777    3  foo\n2000-01-04T00:00:00  1.04791624281    -4  bar\n2000-01-05T00:00:00  0.498580885705   73  baz\n2000-01-06T00:00:00  1.12020151869     1  foo\n2000-01-07T00:00:00  0.487094399463    0  bar\n2000-01-10T00:00:00  0.836648671666    2  baz\n2000-01-11T00:00:00  0.157160753327   34  foo'

```python
test = 'index                             A    B    C\n2000-01-03T00:00:00  0.980268513777    3  foo\n2000-01-04T00:00:00  1.04791624281    -4  bar\n2000-01-05T00:00:00  0.498580885705   73  baz\n2000-01-06T00:00:00  1.12020151869     1  foo\n2000-01-07T00:00:00  0.487094399463    0  bar\n2000-01-10T00:00:00  0.836648671666    2  baz\n2000-01-11T00:00:00  0.157160753327   34  foo'
```

### Step 2: Assign colspecs = value

```python
colspecs = ((0, 19), (21, 35), (38, 40), (42, 45))
```

### Step 3: Assign expected = read_fwf(...)

```python
expected = read_fwf(StringIO(test), colspecs=colspecs)
```

### Step 4: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(test))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
test = 'index                             A    B    C\n2000-01-03T00:00:00  0.980268513777    3  foo\n2000-01-04T00:00:00  1.04791624281    -4  bar\n2000-01-05T00:00:00  0.498580885705   73  baz\n2000-01-06T00:00:00  1.12020151869     1  foo\n2000-01-07T00:00:00  0.487094399463    0  bar\n2000-01-10T00:00:00  0.836648671666    2  baz\n2000-01-11T00:00:00  0.157160753327   34  foo'
colspecs = ((0, 19), (21, 35), (38, 40), (42, 45))
expected = read_fwf(StringIO(test), colspecs=colspecs)
result = read_fwf(StringIO(test))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:444 | Complexity: Intermediate | Last updated: 2026-06-02*