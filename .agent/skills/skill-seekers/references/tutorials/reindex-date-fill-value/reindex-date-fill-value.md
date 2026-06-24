# How To: Reindex Date Fill Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex date fill value

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign arr = date_range.values.reshape(...)

```python
arr = date_range('2016-01-01', periods=6).values.reshape(3, 2)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=['A', 'B'], index=range(3))
```

### Step 3: Assign ts = value

```python
ts = df.iloc[0, 0]
```

### Step 4: Assign fv = ts.date(...)

```python
fv = ts.date()
```

### Step 5: Assign res = df.reindex(...)

```python
res = df.reindex(index=range(4), columns=['A', 'B', 'C'], fill_value=fv)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': df['A'].tolist() + [fv], 'B': df['B'].tolist() + [fv], 'C': [fv] * 4}, dtype=object)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 8: Assign res = df.reindex(...)

```python
res = df.reindex(index=range(4), fill_value=fv)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected[['A', 'B']])
```

### Step 10: Assign res = df.reindex(...)

```python
res = df.reindex(index=range(4), columns=['A', 'B', 'C'], fill_value='2016-01-01')
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': df['A'].tolist() + [ts], 'B': df['B'].tolist() + [ts], 'C': [ts] * 4})
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
arr = date_range('2016-01-01', periods=6).values.reshape(3, 2)
df = DataFrame(arr, columns=['A', 'B'], index=range(3))
ts = df.iloc[0, 0]
fv = ts.date()
res = df.reindex(index=range(4), columns=['A', 'B', 'C'], fill_value=fv)
expected = DataFrame({'A': df['A'].tolist() + [fv], 'B': df['B'].tolist() + [fv], 'C': [fv] * 4}, dtype=object)
tm.assert_frame_equal(res, expected)
res = df.reindex(index=range(4), fill_value=fv)
tm.assert_frame_equal(res, expected[['A', 'B']])
res = df.reindex(index=range(4), columns=['A', 'B', 'C'], fill_value='2016-01-01')
expected = DataFrame({'A': df['A'].tolist() + [ts], 'B': df['B'].tolist() + [ts], 'C': [ts] * 4})
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_reindex.py:202 | Complexity: Advanced | Last updated: 2026-06-02*