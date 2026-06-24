# How To: Multiindex Interval Datetimes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex interval datetimes

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

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([range(4), pd.interval_range(start=pd.Timestamp('2020-01-01'), periods=4, freq='6ME')])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(range(4), index=midx)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(range(4), MultiIndex.from_arrays([range(4), ['(2020-01-31 00:00:00, 2020-07-31 00:00:00]', '(2020-07-31 00:00:00, 2021-01-31 00:00:00]', '(2021-01-31 00:00:00, 2021-07-31 00:00:00]', '(2021-07-31 00:00:00, 2022-01-31 00:00:00]']]))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Call df.to_excel()

```python
df.to_excel(pth)
```

### Step 6: Assign result = pd.read_excel(...)

```python
result = pd.read_excel(pth, index_col=[0, 1])
```


## Complete Example

```python
# Setup
# Fixtures: ext

# Workflow
midx = MultiIndex.from_arrays([range(4), pd.interval_range(start=pd.Timestamp('2020-01-01'), periods=4, freq='6ME')])
df = DataFrame(range(4), index=midx)
with tm.ensure_clean(ext) as pth:
    df.to_excel(pth)
    result = pd.read_excel(pth, index_col=[0, 1])
expected = DataFrame(range(4), MultiIndex.from_arrays([range(4), ['(2020-01-31 00:00:00, 2020-07-31 00:00:00]', '(2020-07-31 00:00:00, 2021-01-31 00:00:00]', '(2021-01-31 00:00:00, 2021-07-31 00:00:00]', '(2021-07-31 00:00:00, 2022-01-31 00:00:00]']]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_writers.py:322 | Complexity: Intermediate | Last updated: 2026-06-02*