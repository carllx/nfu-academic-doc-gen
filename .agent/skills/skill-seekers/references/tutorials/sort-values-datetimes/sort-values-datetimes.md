# How To: Sort Values Datetimes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values datetimes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(['a', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g'], columns=['A'], index=date_range('20130101', periods=9))
```

### Step 2: Assign dts = value

```python
dts = [Timestamp(x) for x in ['2004-02-11', '2004-01-21', '2004-01-26', '2005-09-20', '2010-10-04', '2009-05-12', '2008-11-12', '2010-09-28', '2010-09-28']]
```

### Step 3: Assign unknown = value

```python
df['B'] = dts[::2] + dts[1::2]
```

### Step 4: Assign unknown = 2.0

```python
df['C'] = 2.0
```

### Step 5: Assign unknown = 3.0

```python
df['A1'] = 3.0
```

### Step 6: Assign df1 = df.sort_values(...)

```python
df1 = df.sort_values(by='A')
```

### Step 7: Assign df2 = df.sort_values(...)

```python
df2 = df.sort_values(by=['A'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2)
```

### Step 9: Assign df1 = df.sort_values(...)

```python
df1 = df.sort_values(by='B')
```

### Step 10: Assign df2 = df.sort_values(...)

```python
df2 = df.sort_values(by=['B'])
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2)
```

### Step 12: Assign df1 = df.sort_values(...)

```python
df1 = df.sort_values(by='B')
```

### Step 13: Assign df2 = df.sort_values(...)

```python
df2 = df.sort_values(by=['C', 'B'])
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df2)
```


## Complete Example

```python
# Workflow
df = DataFrame(['a', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g'], columns=['A'], index=date_range('20130101', periods=9))
dts = [Timestamp(x) for x in ['2004-02-11', '2004-01-21', '2004-01-26', '2005-09-20', '2010-10-04', '2009-05-12', '2008-11-12', '2010-09-28', '2010-09-28']]
df['B'] = dts[::2] + dts[1::2]
df['C'] = 2.0
df['A1'] = 3.0
df1 = df.sort_values(by='A')
df2 = df.sort_values(by=['A'])
tm.assert_frame_equal(df1, df2)
df1 = df.sort_values(by='B')
df2 = df.sort_values(by=['B'])
tm.assert_frame_equal(df1, df2)
df1 = df.sort_values(by='B')
df2 = df.sort_values(by=['C', 'B'])
tm.assert_frame_equal(df1, df2)
```

## Next Steps


---

*Source: test_sort_values.py:296 | Complexity: Advanced | Last updated: 2026-06-02*