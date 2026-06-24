# How To: Multiple Date Col

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiple date col

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.tools.datetimes`
- `pandas.io.parsers`

**Setup Required:**
```python
# Fixtures: all_parsers, keep_date_col, request
```

## Step-by-Step Guide

### Step 1: Assign data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000\n'

```python
data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign depr_msg = "The 'keep_date_col' keyword in pd.read_csv is deprecated"

```python
depr_msg = "The 'keep_date_col' keyword in pd.read_csv is deprecated"
```

### Step 4: Assign kwds = value

```python
kwds = {'header': None, 'parse_dates': [[1, 2], [1, 3]], 'keep_date_col': keep_date_col, 'names': ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']}
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 18, 56), 'KORD', '19990127', ' 19:00:00', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], [datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 19, 56), 'KORD', '19990127', ' 20:00:00', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 20, 56), 'KORD', '19990127', ' 21:00:00', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 18), 'KORD', '19990127', ' 21:00:00', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], [datetime(1999, 1, 27, 22, 0), datetime(1999, 1, 27, 21, 56), 'KORD', '19990127', ' 22:00:00', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0], [datetime(1999, 1, 27, 23, 0), datetime(1999, 1, 27, 22, 56), 'KORD', '19990127', ' 23:00:00', ' 22:56:00', -0.59, 1.71, 4.6, 0.0, 280.0]], columns=['X1_X2', 'X1_X3', 'X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason="pyarrow doesn't support disabling auto-inference on column numbers.")
```

### Step 8: Call request.applymarker()

```python
request.applymarker(mark)
```

### Step 9: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), **kwds)
```

### Step 10: Assign expected = expected.drop(...)

```python
expected = expected.drop(['X1', 'X2', 'X3'], axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, keep_date_col, request

# Workflow
data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000\n'
parser = all_parsers
if keep_date_col and parser.engine == 'pyarrow':
    mark = pytest.mark.xfail(reason="pyarrow doesn't support disabling auto-inference on column numbers.")
    request.applymarker(mark)
depr_msg = "The 'keep_date_col' keyword in pd.read_csv is deprecated"
kwds = {'header': None, 'parse_dates': [[1, 2], [1, 3]], 'keep_date_col': keep_date_col, 'names': ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']}
with tm.assert_produces_warning((DeprecationWarning, FutureWarning), match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), **kwds)
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 18, 56), 'KORD', '19990127', ' 19:00:00', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], [datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 19, 56), 'KORD', '19990127', ' 20:00:00', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 20, 56), 'KORD', '19990127', ' 21:00:00', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 18), 'KORD', '19990127', ' 21:00:00', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], [datetime(1999, 1, 27, 22, 0), datetime(1999, 1, 27, 21, 56), 'KORD', '19990127', ' 22:00:00', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0], [datetime(1999, 1, 27, 23, 0), datetime(1999, 1, 27, 22, 56), 'KORD', '19990127', ' 23:00:00', ' 22:56:00', -0.59, 1.71, 4.6, 0.0, 280.0]], columns=['X1_X2', 'X1_X3', 'X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'])
if not keep_date_col:
    expected = expected.drop(['X1', 'X2', 'X3'], axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:318 | Complexity: Advanced | Last updated: 2026-06-02*