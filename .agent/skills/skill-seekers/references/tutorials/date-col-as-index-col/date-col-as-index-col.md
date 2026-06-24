# How To: Date Col As Index Col

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date col as index col

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign data = 'KORD,19990127 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\n'

```python
data = 'KORD,19990127 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\n'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign kwds = value

```python
kwds = {'header': None, 'parse_dates': [1], 'index_col': 1, 'names': ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']}
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), **kwds)
```

### Step 5: Assign index = Index(...)

```python
index = Index([datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 22, 0)], name='X1')
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([['KORD', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], ['KORD', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], ['KORD', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], ['KORD', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], ['KORD', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0]], columns=['X0', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'], index=index)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign unknown = value

```python
expected['X2'] = pd.to_datetime('1970-01-01' + expected['X2']).dt.time
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'KORD,19990127 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\n'
parser = all_parsers
kwds = {'header': None, 'parse_dates': [1], 'index_col': 1, 'names': ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']}
result = parser.read_csv(StringIO(data), **kwds)
index = Index([datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 22, 0)], name='X1')
expected = DataFrame([['KORD', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], ['KORD', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], ['KORD', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], ['KORD', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], ['KORD', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0]], columns=['X0', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'], index=index)
if parser.engine == 'pyarrow':
    expected['X2'] = pd.to_datetime('1970-01-01' + expected['X2']).dt.time
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:452 | Complexity: Advanced | Last updated: 2026-06-02*