# How To: Conversion Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test conversion float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas._config.config`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.plotting`
- `pandas.tseries.offsets`
- `pandas.plotting._matplotlib`

**Setup Required:**
```python
# Fixtures: dtc
```

## Step-by-Step Guide

### Step 1: Assign rtol = value

```python
rtol = 0.5 * 10 ** (-9)
```

### Step 2: Assign rs = dtc.convert(...)

```python
rs = dtc.convert(Timestamp('2012-1-1 01:02:03', tz='UTC'), None, None)
```

### Step 3: Assign xp = converter.mdates.date2num(...)

```python
xp = converter.mdates.date2num(Timestamp('2012-1-1 01:02:03', tz='UTC'))
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(rs, xp, rtol=rtol)
```

### Step 5: Assign rs = dtc.convert(...)

```python
rs = dtc.convert(Timestamp('2012-1-1 09:02:03', tz='Asia/Hong_Kong'), None, None)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(rs, xp, rtol=rtol)
```

### Step 7: Assign rs = dtc.convert(...)

```python
rs = dtc.convert(datetime(2012, 1, 1, 1, 2, 3), None, None)
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(rs, xp, rtol=rtol)
```


## Complete Example

```python
# Setup
# Fixtures: dtc

# Workflow
rtol = 0.5 * 10 ** (-9)
rs = dtc.convert(Timestamp('2012-1-1 01:02:03', tz='UTC'), None, None)
xp = converter.mdates.date2num(Timestamp('2012-1-1 01:02:03', tz='UTC'))
tm.assert_almost_equal(rs, xp, rtol=rtol)
rs = dtc.convert(Timestamp('2012-1-1 09:02:03', tz='Asia/Hong_Kong'), None, None)
tm.assert_almost_equal(rs, xp, rtol=rtol)
rs = dtc.convert(datetime(2012, 1, 1, 1, 2, 3), None, None)
tm.assert_almost_equal(rs, xp, rtol=rtol)
```

## Next Steps


---

*Source: test_converter.py:214 | Complexity: Advanced | Last updated: 2026-06-02*