# How To: To Csv Date Format

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv date format

## Prerequisites

**Required Modules:**
- `io`
- `os`
- `sys`
- `zipfile`
- `_csv`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_sec = DataFrame(...)

```python
df_sec = DataFrame({'A': pd.date_range('20130101', periods=5, freq='s')})
```

**Verification:**
```python
assert df_sec.to_csv() == expected_default_sec
```

### Step 2: Assign df_day = DataFrame(...)

```python
df_day = DataFrame({'A': pd.date_range('20130101', periods=5, freq='d')})
```

**Verification:**
```python
assert df_day.to_csv(date_format='%Y-%m-%d %H:%M:%S') == expected_ymdhms_day
```

### Step 3: Assign expected_rows = value

```python
expected_rows = [',A', '0,2013-01-01 00:00:00', '1,2013-01-01 00:00:01', '2,2013-01-01 00:00:02', '3,2013-01-01 00:00:03', '4,2013-01-01 00:00:04']
```

**Verification:**
```python
assert df_sec.to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
```

### Step 4: Assign expected_default_sec = tm.convert_rows_list_to_csv_str(...)

```python
expected_default_sec = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df_day.to_csv() == expected_default_day
```

### Step 5: Assign expected_rows = value

```python
expected_rows = [',A', '0,2013-01-01 00:00:00', '1,2013-01-02 00:00:00', '2,2013-01-03 00:00:00', '3,2013-01-04 00:00:00', '4,2013-01-05 00:00:00']
```

**Verification:**
```python
assert df_day.to_csv(date_format='%Y-%m-%d') == expected_default_day
```

### Step 6: Assign expected_ymdhms_day = tm.convert_rows_list_to_csv_str(...)

```python
expected_ymdhms_day = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df_sec_grouped.mean().to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
```

### Step 7: Assign expected_rows = value

```python
expected_rows = [',A', '0,2013-01-01', '1,2013-01-01', '2,2013-01-01', '3,2013-01-01', '4,2013-01-01']
```

### Step 8: Assign expected_ymd_sec = tm.convert_rows_list_to_csv_str(...)

```python
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df_sec.to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
```

### Step 9: Assign expected_rows = value

```python
expected_rows = [',A', '0,2013-01-01', '1,2013-01-02', '2,2013-01-03', '3,2013-01-04', '4,2013-01-05']
```

### Step 10: Assign expected_default_day = tm.convert_rows_list_to_csv_str(...)

```python
expected_default_day = tm.convert_rows_list_to_csv_str(expected_rows)
```

**Verification:**
```python
assert df_day.to_csv() == expected_default_day
```

### Step 11: Assign unknown = 0

```python
df_sec['B'] = 0
```

### Step 12: Assign unknown = 1

```python
df_sec['C'] = 1
```

### Step 13: Assign expected_rows = value

```python
expected_rows = ['A,B,C', '2013-01-01,0,1.0']
```

### Step 14: Assign expected_ymd_sec = tm.convert_rows_list_to_csv_str(...)

```python
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)
```

### Step 15: Assign df_sec_grouped = df_sec.groupby(...)

```python
df_sec_grouped = df_sec.groupby([pd.Grouper(key='A', freq='1h'), 'B'])
```

**Verification:**
```python
assert df_sec_grouped.mean().to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
```


## Complete Example

```python
# Workflow
df_sec = DataFrame({'A': pd.date_range('20130101', periods=5, freq='s')})
df_day = DataFrame({'A': pd.date_range('20130101', periods=5, freq='d')})
expected_rows = [',A', '0,2013-01-01 00:00:00', '1,2013-01-01 00:00:01', '2,2013-01-01 00:00:02', '3,2013-01-01 00:00:03', '4,2013-01-01 00:00:04']
expected_default_sec = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_sec.to_csv() == expected_default_sec
expected_rows = [',A', '0,2013-01-01 00:00:00', '1,2013-01-02 00:00:00', '2,2013-01-03 00:00:00', '3,2013-01-04 00:00:00', '4,2013-01-05 00:00:00']
expected_ymdhms_day = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_day.to_csv(date_format='%Y-%m-%d %H:%M:%S') == expected_ymdhms_day
expected_rows = [',A', '0,2013-01-01', '1,2013-01-01', '2,2013-01-01', '3,2013-01-01', '4,2013-01-01']
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_sec.to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
expected_rows = [',A', '0,2013-01-01', '1,2013-01-02', '2,2013-01-03', '3,2013-01-04', '4,2013-01-05']
expected_default_day = tm.convert_rows_list_to_csv_str(expected_rows)
assert df_day.to_csv() == expected_default_day
assert df_day.to_csv(date_format='%Y-%m-%d') == expected_default_day
df_sec['B'] = 0
df_sec['C'] = 1
expected_rows = ['A,B,C', '2013-01-01,0,1.0']
expected_ymd_sec = tm.convert_rows_list_to_csv_str(expected_rows)
df_sec_grouped = df_sec.groupby([pd.Grouper(key='A', freq='1h'), 'B'])
assert df_sec_grouped.mean().to_csv(date_format='%Y-%m-%d') == expected_ymd_sec
```

## Next Steps


---

*Source: test_to_csv.py:221 | Complexity: Advanced | Last updated: 2026-06-02*