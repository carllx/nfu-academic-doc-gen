# How To: Frame Non Unique Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame non unique columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `decimal`
- `io`
- `json`
- `os`
- `sys`
- `time`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.json`
- `pandas.arrays`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: orient, data
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data, index=[1, 2], columns=['x', 'x'])
```

### Step 2: Assign result = read_json(...)

```python
result = read_json(StringIO(df.to_json(orient=orient)), orient=orient, convert_dates=['x'])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(data)
```

### Step 5: Call expected.isetitem()

```python
expected.isetitem(0, expected.iloc[:, 0].astype(np.int64) // 1000000)
```

### Step 6: Assign expected = df

```python
expected = df
```

### Step 7: Assign expected.columns = value

```python
expected.columns = ['x', 'x.1']
```


## Complete Example

```python
# Setup
# Fixtures: orient, data

# Workflow
df = DataFrame(data, index=[1, 2], columns=['x', 'x'])
result = read_json(StringIO(df.to_json(orient=orient)), orient=orient, convert_dates=['x'])
if orient == 'values':
    expected = DataFrame(data)
    if expected.iloc[:, 0].dtype == 'datetime64[ns]':
        expected.isetitem(0, expected.iloc[:, 0].astype(np.int64) // 1000000)
elif orient == 'split':
    expected = df
    expected.columns = ['x', 'x.1']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pandas.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*