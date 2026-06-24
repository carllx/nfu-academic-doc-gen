# How To: Usecols Str

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols str

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

### Step 2: Assign expected = value

```python
expected = df_ref[['A', 'B', 'C']]
```

### Step 3: Call adjust_expected()

```python
adjust_expected(expected, read_ext, engine)
```

### Step 4: Assign df2 = pd.read_excel(...)

```python
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A:D')
```

### Step 5: Assign df3 = pd.read_excel(...)

```python
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A:D')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, expected)
```

### Step 8: Assign expected = value

```python
expected = df_ref[['B', 'C']]
```

### Step 9: Call adjust_expected()

```python
adjust_expected(expected, read_ext, engine)
```

### Step 10: Assign df2 = pd.read_excel(...)

```python
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A,C,D')
```

### Step 11: Assign df3 = pd.read_excel(...)

```python
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A,C,D')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, expected)
```

### Step 14: Assign df2 = pd.read_excel(...)

```python
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A,C:D')
```

### Step 15: Assign df3 = pd.read_excel(...)

```python
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A,C:D')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df3, expected)
```


## Complete Example

```python
# Setup
# Fixtures: request, engine, read_ext, df_ref

# Workflow
xfail_datetimes_with_pyxlsb(engine, request)
expected = df_ref[['A', 'B', 'C']]
adjust_expected(expected, read_ext, engine)
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A:D')
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A:D')
tm.assert_frame_equal(df2, expected)
tm.assert_frame_equal(df3, expected)
expected = df_ref[['B', 'C']]
adjust_expected(expected, read_ext, engine)
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A,C,D')
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A,C,D')
tm.assert_frame_equal(df2, expected)
tm.assert_frame_equal(df3, expected)
df2 = pd.read_excel('test1' + read_ext, sheet_name='Sheet1', index_col=0, usecols='A,C:D')
df3 = pd.read_excel('test1' + read_ext, sheet_name='Sheet2', skiprows=[1], index_col=0, usecols='A,C:D')
tm.assert_frame_equal(df2, expected)
tm.assert_frame_equal(df3, expected)
```

## Next Steps


---

*Source: test_readers.py:252 | Complexity: Advanced | Last updated: 2026-06-02*