# How To: Numpy Reduction With Tz Aware Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numpy reduction with tz aware dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture, func
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign arg = pd.to_datetime.tz_localize(...)

```python
arg = pd.to_datetime(['2019']).tz_localize(tz)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(arg)
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(np, func)(expected, expected)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture, func

# Workflow
tz = tz_aware_fixture
arg = pd.to_datetime(['2019']).tz_localize(tz)
expected = Series(arg)
result = getattr(np, func)(expected, expected)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:225 | Complexity: Intermediate | Last updated: 2026-06-02*