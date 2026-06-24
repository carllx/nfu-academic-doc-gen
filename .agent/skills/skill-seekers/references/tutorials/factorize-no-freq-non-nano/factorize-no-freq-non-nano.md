# How To: Factorize No Freq Non Nano

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test factorize no freq non nano

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture, sort
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign idx = value

```python
idx = date_range('2016-11-06', freq='h', periods=5, tz=tz)[[0, 4, 1, 3, 2]]
```

### Step 3: Assign unknown = idx.factorize(...)

```python
exp_codes, exp_uniques = idx.factorize(sort=sort)
```

### Step 4: Assign unknown = idx.as_unit.factorize(...)

```python
res_codes, res_uniques = idx.as_unit('s').factorize(sort=sort)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res_codes, exp_codes)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_uniques, exp_uniques.as_unit('s'))
```

### Step 7: Assign unknown = idx.as_unit.to_series.factorize(...)

```python
res_codes, res_uniques = idx.as_unit('s').to_series().factorize(sort=sort)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res_codes, exp_codes)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_uniques, exp_uniques.as_unit('s'))
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, sort

# Workflow
tz = tz_naive_fixture
idx = date_range('2016-11-06', freq='h', periods=5, tz=tz)[[0, 4, 1, 3, 2]]
exp_codes, exp_uniques = idx.factorize(sort=sort)
res_codes, res_uniques = idx.as_unit('s').factorize(sort=sort)
tm.assert_numpy_array_equal(res_codes, exp_codes)
tm.assert_index_equal(res_uniques, exp_uniques.as_unit('s'))
res_codes, res_uniques = idx.as_unit('s').to_series().factorize(sort=sort)
tm.assert_numpy_array_equal(res_codes, exp_codes)
tm.assert_index_equal(res_uniques, exp_uniques.as_unit('s'))
```

## Next Steps


---

*Source: test_factorize.py:111 | Complexity: Advanced | Last updated: 2026-06-02*