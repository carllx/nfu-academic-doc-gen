# How To: Same Tz Min Max Axis 1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test same tz min max axis 1

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
# Fixtures: op, expected_col
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(date_range('2016-01-01 00:00:00', periods=3, tz='UTC'), columns=['a'])
```

### Step 2: Assign unknown = df.a.subtract(...)

```python
df['b'] = df.a.subtract(Timedelta(seconds=3600))
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(df, op)(axis=1)
```

### Step 4: Assign expected = unknown.rename(...)

```python
expected = df[expected_col].rename(None)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op, expected_col

# Workflow
df = DataFrame(date_range('2016-01-01 00:00:00', periods=3, tz='UTC'), columns=['a'])
df['b'] = df.a.subtract(Timedelta(seconds=3600))
result = getattr(df, op)(axis=1)
expected = df[expected_col].rename(None)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:214 | Complexity: Intermediate | Last updated: 2026-06-02*