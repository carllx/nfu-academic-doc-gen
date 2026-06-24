# How To: Colspecs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test colspecs

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

### Step 1: Assign data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'

```python
data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'
```

### Step 2: Assign colspecs = value

```python
colspecs = [(0, 4), (4, 8), (8, 20), (21, 33), (34, 43)]
```

### Step 3: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), colspecs=colspecs)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2011, 58, 360.24294, 149.910199, 11950.7], [2011, 59, 444.953632, 166.985655, 11788.4], [2011, 60, 364.136849, 183.628767, 11806.2], [2011, 61, 413.836124, 184.375703, 11916.8], [2011, 62, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D', 'E'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'
colspecs = [(0, 4), (4, 8), (8, 20), (21, 33), (34, 43)]
result = read_fwf(StringIO(data), colspecs=colspecs)
expected = DataFrame([[2011, 58, 360.24294, 149.910199, 11950.7], [2011, 59, 444.953632, 166.985655, 11788.4], [2011, 60, 364.136849, 183.628767, 11806.2], [2011, 61, 413.836124, 184.375703, 11916.8], [2011, 62, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D', 'E'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*