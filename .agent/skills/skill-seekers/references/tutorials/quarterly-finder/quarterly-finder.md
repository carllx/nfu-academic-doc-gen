# How To: Quarterly Finder

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test quarterly finder

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
# Fixtures: year_span
```

## Step-by-Step Guide

### Step 1: Assign vmin = value

```python
vmin = -1000
```

**Verification:**
```python
assert np.all(check_major_years)
```

### Step 2: Assign vmax = value

```python
vmax = vmin + year_span * 4
```

**Verification:**
```python
assert np.all(check_minor_years)
```

### Step 3: Assign span = value

```python
span = vmax - vmin + 1
```

**Verification:**
```python
assert np.all(check_major_quarters)
```

### Step 4: Assign nyears = value

```python
nyears = span / 4
```

**Verification:**
```python
assert np.all(check_minor_quarters)
```

### Step 5: Assign unknown = converter._get_default_annual_spacing(...)

```python
min_anndef, maj_anndef = converter._get_default_annual_spacing(nyears)
```

### Step 6: Assign result = converter._quarterly_finder(...)

```python
result = converter._quarterly_finder(vmin, vmax, to_offset('QE'))
```

### Step 7: Assign quarters = PeriodIndex(...)

```python
quarters = PeriodIndex(arrays.PeriodArray(np.array([x[0] for x in result]), dtype='period[Q]'))
```

### Step 8: Assign majors = np.array(...)

```python
majors = np.array([x[1] for x in result])
```

### Step 9: Assign minors = np.array(...)

```python
minors = np.array([x[2] for x in result])
```

### Step 10: Assign major_quarters = value

```python
major_quarters = quarters[majors]
```

### Step 11: Assign minor_quarters = value

```python
minor_quarters = quarters[minors]
```

### Step 12: Assign check_major_years = value

```python
check_major_years = major_quarters.year % maj_anndef == 0
```

### Step 13: Assign check_minor_years = value

```python
check_minor_years = minor_quarters.year % min_anndef == 0
```

### Step 14: Assign check_major_quarters = value

```python
check_major_quarters = major_quarters.quarter == 1
```

### Step 15: Assign check_minor_quarters = value

```python
check_minor_quarters = minor_quarters.quarter == 1
```

**Verification:**
```python
assert np.all(check_major_years)
```

### Step 16: Call pytest.skip()

```python
pytest.skip('the quarterly finder is only invoked if the span is >= 45')
```


## Complete Example

```python
# Setup
# Fixtures: year_span

# Workflow
vmin = -1000
vmax = vmin + year_span * 4
span = vmax - vmin + 1
if span < 45:
    pytest.skip('the quarterly finder is only invoked if the span is >= 45')
nyears = span / 4
min_anndef, maj_anndef = converter._get_default_annual_spacing(nyears)
result = converter._quarterly_finder(vmin, vmax, to_offset('QE'))
quarters = PeriodIndex(arrays.PeriodArray(np.array([x[0] for x in result]), dtype='period[Q]'))
majors = np.array([x[1] for x in result])
minors = np.array([x[2] for x in result])
major_quarters = quarters[majors]
minor_quarters = quarters[minors]
check_major_years = major_quarters.year % maj_anndef == 0
check_minor_years = minor_quarters.year % min_anndef == 0
check_major_quarters = major_quarters.quarter == 1
check_minor_quarters = minor_quarters.quarter == 1
assert np.all(check_major_years)
assert np.all(check_minor_years)
assert np.all(check_major_quarters)
assert np.all(check_minor_quarters)
```

## Next Steps


---

*Source: test_converter.py:387 | Complexity: Advanced | Last updated: 2026-06-02*