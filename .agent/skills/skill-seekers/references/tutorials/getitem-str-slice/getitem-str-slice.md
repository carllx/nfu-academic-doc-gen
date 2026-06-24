# How To: Getitem Str Slice

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem str slice

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([['20160525 13:30:00.023', 'MSFT', '51.95', '51.95'], ['20160525 13:30:00.048', 'GOOG', '720.50', '720.93'], ['20160525 13:30:00.076', 'AAPL', '98.55', '98.56'], ['20160525 13:30:00.131', 'AAPL', '98.61', '98.62'], ['20160525 13:30:00.135', 'MSFT', '51.92', '51.95'], ['20160525 13:30:00.135', 'AAPL', '98.61', '98.62']], columns='time,ticker,bid,ask'.split(','))
```

### Step 2: Assign df2 = df.set_index.sort_index(...)

```python
df2 = df.set_index(['ticker', 'time']).sort_index()
```

### Step 3: Assign res = unknown.droplevel(...)

```python
res = df2.loc[('AAPL', slice('2016-05-25 13:30:00')), :].droplevel(0)
```

### Step 4: Assign expected = value

```python
expected = df2.loc['AAPL'].loc[slice('2016-05-25 13:30:00'), :]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([['20160525 13:30:00.023', 'MSFT', '51.95', '51.95'], ['20160525 13:30:00.048', 'GOOG', '720.50', '720.93'], ['20160525 13:30:00.076', 'AAPL', '98.55', '98.56'], ['20160525 13:30:00.131', 'AAPL', '98.61', '98.62'], ['20160525 13:30:00.135', 'MSFT', '51.92', '51.95'], ['20160525 13:30:00.135', 'AAPL', '98.61', '98.62']], columns='time,ticker,bid,ask'.split(','))
df2 = df.set_index(['ticker', 'time']).sort_index()
res = df2.loc[('AAPL', slice('2016-05-25 13:30:00')), :].droplevel(0)
expected = df2.loc['AAPL'].loc[slice('2016-05-25 13:30:00'), :]
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_loc.py:713 | Complexity: Intermediate | Last updated: 2026-06-02*