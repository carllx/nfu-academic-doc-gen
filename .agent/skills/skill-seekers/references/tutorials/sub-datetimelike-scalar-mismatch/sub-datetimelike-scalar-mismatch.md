# How To: Sub Datetimelike Scalar Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub datetimelike scalar mismatch

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3)
```

**Verification:**
```python
assert result.dtype == 'm8[us]'
```

### Step 2: Assign dta = dti._data.as_unit(...)

```python
dta = dti._data.as_unit('us')
```

### Step 3: Assign ts = unknown.as_unit(...)

```python
ts = dta[0].as_unit('s')
```

### Step 4: Assign result = value

```python
result = dta - ts
```

### Step 5: Assign expected = unknown._data.as_unit(...)

```python
expected = (dti - dti[0])._data.as_unit('us')
```

**Verification:**
```python
assert result.dtype == 'm8[us]'
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3)
dta = dti._data.as_unit('us')
ts = dta[0].as_unit('s')
result = dta - ts
expected = (dti - dti[0])._data.as_unit('us')
assert result.dtype == 'm8[us]'
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:248 | Complexity: Intermediate | Last updated: 2026-06-02*