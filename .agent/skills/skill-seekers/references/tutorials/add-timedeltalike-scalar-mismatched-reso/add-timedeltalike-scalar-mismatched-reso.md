# How To: Add Timedeltalike Scalar Mismatched Reso

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test add timedeltalike scalar mismatched reso

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: dta_dti, scalar
```

## Step-by-Step Guide

### Step 1: Assign unknown = dta_dti

```python
dta, dti = dta_dti
```

### Step 2: Assign td = pd.Timedelta(...)

```python
td = pd.Timedelta(scalar)
```

### Step 3: Assign exp_unit = tm.get_finest_unit(...)

```python
exp_unit = tm.get_finest_unit(dta.unit, td.unit)
```

### Step 4: Assign expected = unknown._data.as_unit(...)

```python
expected = (dti + td)._data.as_unit(exp_unit)
```

### Step 5: Assign result = value

```python
result = dta + scalar
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = scalar + dta
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 9: Assign expected = unknown._data.as_unit(...)

```python
expected = (dti - td)._data.as_unit(exp_unit)
```

### Step 10: Assign result = value

```python
result = dta - scalar
```

### Step 11: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dta_dti, scalar

# Workflow
dta, dti = dta_dti
td = pd.Timedelta(scalar)
exp_unit = tm.get_finest_unit(dta.unit, td.unit)
expected = (dti + td)._data.as_unit(exp_unit)
result = dta + scalar
tm.assert_extension_array_equal(result, expected)
result = scalar + dta
tm.assert_extension_array_equal(result, expected)
expected = (dti - td)._data.as_unit(exp_unit)
result = dta - scalar
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:231 | Complexity: Advanced | Last updated: 2026-06-02*