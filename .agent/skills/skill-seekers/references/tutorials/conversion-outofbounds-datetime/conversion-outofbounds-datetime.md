# How To: Conversion Outofbounds Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test conversion outofbounds datetime

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
# Fixtures: dtc, values
```

## Step-by-Step Guide

### Step 1: Assign rs = dtc.convert(...)

```python
rs = dtc.convert(values, None, None)
```

**Verification:**
```python
assert rs == xp
```

### Step 2: Assign xp = converter.mdates.date2num(...)

```python
xp = converter.mdates.date2num(values)
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(rs, xp)
```

### Step 4: Assign rs = dtc.convert(...)

```python
rs = dtc.convert(values[0], None, None)
```

### Step 5: Assign xp = converter.mdates.date2num(...)

```python
xp = converter.mdates.date2num(values[0])
```

**Verification:**
```python
assert rs == xp
```


## Complete Example

```python
# Setup
# Fixtures: dtc, values

# Workflow
rs = dtc.convert(values, None, None)
xp = converter.mdates.date2num(values)
tm.assert_numpy_array_equal(rs, xp)
rs = dtc.convert(values[0], None, None)
xp = converter.mdates.date2num(values[0])
assert rs == xp
```

## Next Steps


---

*Source: test_converter.py:236 | Complexity: Intermediate | Last updated: 2026-06-02*