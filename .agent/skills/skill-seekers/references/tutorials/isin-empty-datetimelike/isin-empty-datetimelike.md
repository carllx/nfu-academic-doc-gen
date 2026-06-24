# How To: Isin Empty Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin empty datetimelike

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1_ts = DataFrame(...)

```python
df1_ts = DataFrame({'date': pd.to_datetime(['2014-01-01', '2014-01-02'])})
```

### Step 2: Assign df1_td = DataFrame(...)

```python
df1_td = DataFrame({'date': [pd.Timedelta(1, 's'), pd.Timedelta(2, 's')]})
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'date': []})
```

### Step 4: Assign df3 = DataFrame(...)

```python
df3 = DataFrame()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'date': [False, False]})
```

### Step 6: Assign result = df1_ts.isin(...)

```python
result = df1_ts.isin(df2)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df1_ts.isin(...)

```python
result = df1_ts.isin(df3)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = df1_td.isin(...)

```python
result = df1_td.isin(df2)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = df1_td.isin(...)

```python
result = df1_td.isin(df3)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1_ts = DataFrame({'date': pd.to_datetime(['2014-01-01', '2014-01-02'])})
df1_td = DataFrame({'date': [pd.Timedelta(1, 's'), pd.Timedelta(2, 's')]})
df2 = DataFrame({'date': []})
df3 = DataFrame()
expected = DataFrame({'date': [False, False]})
result = df1_ts.isin(df2)
tm.assert_frame_equal(result, expected)
result = df1_ts.isin(df3)
tm.assert_frame_equal(result, expected)
result = df1_td.isin(df2)
tm.assert_frame_equal(result, expected)
result = df1_td.isin(df3)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:178 | Complexity: Advanced | Last updated: 2026-06-02*