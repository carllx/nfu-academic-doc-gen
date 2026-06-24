# How To: Excel Table

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test excel table

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `io`
- `os`
- `pathlib`
- `platform`
- `re`
- `urllib.error`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `s3fs`
- `py.path`
- `pyarrow`
- `pandas.arrays`
- `xlrd`
- `xlrd`
- `python_calamine`
- `python_calamine`

**Setup Required:**
```python
# Fixtures: request, engine, read_ext, df_ref
```

## Step-by-Step Guide

### Step 1: Call xfail_datetimes_with_pyxlsb()

```python
xfail_datetimes_with_pyxlsb(engine, request)
```

### Step 2: Assign expected = df_ref

```python
expected = df_ref
```

### Step 3: Call adjust_expected()

```python
adjust_expected(expected, read_ext, engine)
```

### Step 4: Assign df1 = pd.read_excel(...)

```python
df1 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0)
```

### Step 5: Assign df2 = pd.read_excel(...)

```python
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 8: Assign df3 = pd.read_excel(...)

```python
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, skipfooter=1)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, df1.iloc[:-1])
```


## Complete Example

```python
# Setup
# Fixtures: request, engine, read_ext, df_ref

# Workflow
xfail_datetimes_with_pyxlsb(engine, request)
expected = df_ref
adjust_expected(expected, read_ext, engine)
df1 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0)
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0)
tm.assert_frame_equal(df1, expected)
tm.assert_frame_equal(df2, expected)
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, skipfooter=1)
tm.assert_frame_equal(df3, df1.iloc[:-1])
```

## Next Steps


---

*Source: test_readers.py:434 | Complexity: Advanced | Last updated: 2026-06-02*