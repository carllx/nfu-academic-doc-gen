# How To: Replace Out Of Pydatetime Bounds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace out of pydatetime bounds

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.util._test_decorators`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('2016-01-01').as_unit('ns')
```

**Verification:**
```python
assert result.year == 99999
```

### Step 2: Assign msg = "Out of bounds timestamp: 99999-01-01 00:00:00 with frequency 'ns'"

```python
msg = "Out of bounds timestamp: 99999-01-01 00:00:00 with frequency 'ns'"
```

**Verification:**
```python
assert result._value == Timestamp(np.datetime64('99999-01-01', 'ms'))._value
```

### Step 3: Assign ts = ts.as_unit(...)

```python
ts = ts.as_unit('ms')
```

### Step 4: Assign result = ts.replace(...)

```python
result = ts.replace(year=99999)
```

**Verification:**
```python
assert result.year == 99999
```

### Step 5: Call ts.replace()

```python
ts.replace(year=99999)
```


## Complete Example

```python
# Workflow
ts = Timestamp('2016-01-01').as_unit('ns')
msg = "Out of bounds timestamp: 99999-01-01 00:00:00 with frequency 'ns'"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    ts.replace(year=99999)
ts = ts.as_unit('ms')
result = ts.replace(year=99999)
assert result.year == 99999
assert result._value == Timestamp(np.datetime64('99999-01-01', 'ms'))._value
```

## Next Steps


---

*Source: test_replace.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*