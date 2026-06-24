# How To: Negative Dates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negative dates

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `time`
- `unicodedata`
- `dateutil.tz`
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.tseries`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('-2000-01-01')
```

### Step 2: Assign msg = " not yet supported on Timestamps which are outside the range of Python's standard library. For now, please call the components you need \\(such as `.year` and `.month`\\) and construct your string from there.$"

```python
msg = " not yet supported on Timestamps which are outside the range of Python's standard library. For now, please call the components you need \\(such as `.year` and `.month`\\) and construct your string from there.$"
```

### Step 3: Assign func = '^strftime'

```python
func = '^strftime'
```

### Step 4: Assign msg = " not yet supported on Timestamps which are outside the range of Python's standard library. "

```python
msg = " not yet supported on Timestamps which are outside the range of Python's standard library. "
```

### Step 5: Assign func = '^date'

```python
func = '^date'
```

### Step 6: Assign func = '^isocalendar'

```python
func = '^isocalendar'
```

### Step 7: Assign func = '^timetuple'

```python
func = '^timetuple'
```

### Step 8: Assign func = '^toordinal'

```python
func = '^toordinal'
```

### Step 9: Call ts.strftime()

```python
ts.strftime('%Y')
```

### Step 10: Call ts.date()

```python
ts.date()
```

### Step 11: Call ts.isocalendar()

```python
ts.isocalendar()
```

### Step 12: Call ts.timetuple()

```python
ts.timetuple()
```

### Step 13: Call ts.toordinal()

```python
ts.toordinal()
```


## Complete Example

```python
# Workflow
ts = Timestamp('-2000-01-01')
msg = " not yet supported on Timestamps which are outside the range of Python's standard library. For now, please call the components you need \\(such as `.year` and `.month`\\) and construct your string from there.$"
func = '^strftime'
with pytest.raises(NotImplementedError, match=func + msg):
    ts.strftime('%Y')
msg = " not yet supported on Timestamps which are outside the range of Python's standard library. "
func = '^date'
with pytest.raises(NotImplementedError, match=func + msg):
    ts.date()
func = '^isocalendar'
with pytest.raises(NotImplementedError, match=func + msg):
    ts.isocalendar()
func = '^timetuple'
with pytest.raises(NotImplementedError, match=func + msg):
    ts.timetuple()
func = '^toordinal'
with pytest.raises(NotImplementedError, match=func + msg):
    ts.toordinal()
```

## Next Steps


---

*Source: test_timestamp.py:901 | Complexity: Advanced | Last updated: 2026-06-02*