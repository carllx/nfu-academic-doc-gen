# How To: Multiple Date Cols With Header

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple date cols with header

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'ID,date,NominalTime,ActualTime,TDew,TAir,Windspeed,Precip,WindDir\nKORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000'

```python
data = 'ID,date,NominalTime,ActualTime,TDew,TAir,Windspeed,Precip,WindDir\nKORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000'
```

### Step 3: Assign depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"

```python
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), 'KORD', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], [datetime(1999, 1, 27, 20, 0), 'KORD', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], [datetime(1999, 1, 27, 21, 0), 'KORD', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], [datetime(1999, 1, 27, 21, 0), 'KORD', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], [datetime(1999, 1, 27, 22, 0), 'KORD', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0], [datetime(1999, 1, 27, 23, 0), 'KORD', ' 22:56:00', -0.59, 1.71, 4.6, 0.0, 280.0]], columns=['nominal', 'ID', 'ActualTime', 'TDew', 'TAir', 'Windspeed', 'Precip', 'WindDir'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), parse_dates={'nominal': [1, 2]})
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'ID,date,NominalTime,ActualTime,TDew,TAir,Windspeed,Precip,WindDir\nKORD,19990127, 19:00:00, 18:56:00, 0.8100, 2.8100, 7.2000, 0.0000, 280.0000\nKORD,19990127, 20:00:00, 19:56:00, 0.0100, 2.2100, 7.2000, 0.0000, 260.0000\nKORD,19990127, 21:00:00, 20:56:00, -0.5900, 2.2100, 5.7000, 0.0000, 280.0000\nKORD,19990127, 21:00:00, 21:18:00, -0.9900, 2.0100, 3.6000, 0.0000, 270.0000\nKORD,19990127, 22:00:00, 21:56:00, -0.5900, 1.7100, 5.1000, 0.0000, 290.0000\nKORD,19990127, 23:00:00, 22:56:00, -0.5900, 1.7100, 4.6000, 0.0000, 280.0000'
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    result = parser.read_csv(StringIO(data), parse_dates={'nominal': [1, 2]})
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), 'KORD', ' 18:56:00', 0.81, 2.81, 7.2, 0.0, 280.0], [datetime(1999, 1, 27, 20, 0), 'KORD', ' 19:56:00', 0.01, 2.21, 7.2, 0.0, 260.0], [datetime(1999, 1, 27, 21, 0), 'KORD', ' 20:56:00', -0.59, 2.21, 5.7, 0.0, 280.0], [datetime(1999, 1, 27, 21, 0), 'KORD', ' 21:18:00', -0.99, 2.01, 3.6, 0.0, 270.0], [datetime(1999, 1, 27, 22, 0), 'KORD', ' 21:56:00', -0.59, 1.71, 5.1, 0.0, 290.0], [datetime(1999, 1, 27, 23, 0), 'KORD', ' 22:56:00', -0.59, 1.71, 4.6, 0.0, 280.0]], columns=['nominal', 'ID', 'ActualTime', 'TDew', 'TAir', 'Windspeed', 'Precip', 'WindDir'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:603 | Complexity: Intermediate | Last updated: 2026-06-02*