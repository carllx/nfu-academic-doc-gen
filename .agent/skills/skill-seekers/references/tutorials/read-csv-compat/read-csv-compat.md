# How To: Read Csv Compat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv compat

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

### Step 1: Assign csv_data = 'A,B,C,D,E\n2011,58,360.242940,149.910199,11950.7\n2011,59,444.953632,166.985655,11788.4\n2011,60,364.136849,183.628767,11806.2\n2011,61,413.836124,184.375703,11916.8\n2011,62,502.953953,173.237159,12468.3\n'

```python
csv_data = 'A,B,C,D,E\n2011,58,360.242940,149.910199,11950.7\n2011,59,444.953632,166.985655,11788.4\n2011,60,364.136849,183.628767,11806.2\n2011,61,413.836124,184.375703,11916.8\n2011,62,502.953953,173.237159,12468.3\n'
```

### Step 2: Assign expected = read_csv(...)

```python
expected = read_csv(StringIO(csv_data), engine='python')
```

### Step 3: Assign fwf_data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'

```python
fwf_data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'
```

### Step 4: Assign colspecs = value

```python
colspecs = [(0, 4), (4, 8), (8, 20), (21, 33), (34, 43)]
```

### Step 5: Assign result = read_fwf(...)

```python
result = read_fwf(StringIO(fwf_data), colspecs=colspecs)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
csv_data = 'A,B,C,D,E\n2011,58,360.242940,149.910199,11950.7\n2011,59,444.953632,166.985655,11788.4\n2011,60,364.136849,183.628767,11806.2\n2011,61,413.836124,184.375703,11916.8\n2011,62,502.953953,173.237159,12468.3\n'
expected = read_csv(StringIO(csv_data), engine='python')
fwf_data = 'A   B     C            D            E\n201158    360.242940   149.910199   11950.7\n201159    444.953632   166.985655   11788.4\n201160    364.136849   183.628767   11806.2\n201161    413.836124   184.375703   11916.8\n201162    502.953953   173.237159   12468.3\n'
colspecs = [(0, 4), (4, 8), (8, 20), (21, 33), (34, 43)]
result = read_fwf(StringIO(fwf_data), colspecs=colspecs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_read_fwf.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*