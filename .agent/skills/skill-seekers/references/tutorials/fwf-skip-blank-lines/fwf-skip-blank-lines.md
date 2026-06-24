# How To: Fwf Skip Blank Lines

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fwf skip blank lines

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

### Step 1: Assign data = '\n\nA         B            C            D\n\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n\n'

```python
data = '\n\nA         B            C            D\n\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n\n'
```

### Step 2: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), skip_blank_lines=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[201158, 360.24294, 149.910199, 11950.7], [201159, 444.953632, 166.985655, 11788.4], [201162, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign data = 'A         B            C            D\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n'

```python
data = 'A         B            C            D\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n'
```

### Step 6: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(data), skip_blank_lines=False)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[201158, 360.24294, 149.910199, 11950.7], [201159, 444.953632, 166.985655, 11788.4], [np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan], [201162, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = '\n\nA         B            C            D\n\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n\n'
result = read_fwf(StringIO(data), skip_blank_lines=True)
expected = DataFrame([[201158, 360.24294, 149.910199, 11950.7], [201159, 444.953632, 166.985655, 11788.4], [201162, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D'])
tm.assert_frame_equal(result, expected)
data = 'A         B            C            D\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n\n\n201162    502.953953   173.237159   12468.3\n'
result = read_fwf(StringIO(data), skip_blank_lines=False)
expected = DataFrame([[201158, 360.24294, 149.910199, 11950.7], [201159, 444.953632, 166.985655, 11788.4], [np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan], [201162, 502.953953, 173.237159, 12468.3]], columns=['A', 'B', 'C', 'D'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:367 | Complexity: Advanced | Last updated: 2026-06-02*