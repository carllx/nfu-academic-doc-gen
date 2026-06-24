# How To: Read Excel Parse Dates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read excel parse dates

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `io`
- `os`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat._constants`
- `pandas.compat._optional`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.excel._util`

**Setup Required:**
```python
# Fixtures: ext
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'col': [1, 2, 3], 'date_strings': date_range('2012-01-01', periods=3)})
```

### Step 2: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 3: Assign unknown = unknown.dt.strftime(...)

```python
df2['date_strings'] = df2['date_strings'].dt.strftime('%m/%d/%Y')
```

### Step 4: Call df2.to_excel()

```python
df2.to_excel(pth)
```

### Step 5: Assign res = pd.read_excel(...)

```python
res = pd.read_excel(pth, index_col=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, res)
```

### Step 7: Assign res = pd.read_excel(...)

```python
res = pd.read_excel(pth, parse_dates=['date_strings'], index_col=0)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res)
```

### Step 9: Assign date_parser = value

```python
date_parser = lambda x: datetime.strptime(x, '%m/%d/%Y')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res)
```

### Step 11: Assign res = pd.read_excel(...)

```python
res = pd.read_excel(pth, parse_dates=['date_strings'], date_format='%m/%d/%Y', index_col=0)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, res)
```

### Step 13: Assign res = pd.read_excel(...)

```python
res = pd.read_excel(pth, parse_dates=['date_strings'], date_parser=date_parser, index_col=0)
```


## Complete Example

```python
# Setup
# Fixtures: ext

# Workflow
df = DataFrame({'col': [1, 2, 3], 'date_strings': date_range('2012-01-01', periods=3)})
df2 = df.copy()
df2['date_strings'] = df2['date_strings'].dt.strftime('%m/%d/%Y')
with tm.ensure_clean(ext) as pth:
    df2.to_excel(pth)
    res = pd.read_excel(pth, index_col=0)
    tm.assert_frame_equal(df2, res)
    res = pd.read_excel(pth, parse_dates=['date_strings'], index_col=0)
    tm.assert_frame_equal(df, res)
    date_parser = lambda x: datetime.strptime(x, '%m/%d/%Y')
    with tm.assert_produces_warning(FutureWarning, match="use 'date_format' instead", raise_on_extra_warnings=False):
        res = pd.read_excel(pth, parse_dates=['date_strings'], date_parser=date_parser, index_col=0)
    tm.assert_frame_equal(df, res)
    res = pd.read_excel(pth, parse_dates=['date_strings'], date_format='%m/%d/%Y', index_col=0)
    tm.assert_frame_equal(df, res)
```

## Next Steps


---

*Source: test_writers.py:287 | Complexity: Advanced | Last updated: 2026-06-02*