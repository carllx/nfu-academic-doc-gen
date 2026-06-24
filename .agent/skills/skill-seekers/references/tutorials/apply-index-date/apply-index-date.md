# How To: Apply Index Date

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply index date

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = ['2011-05-16 00:00', '2011-05-16 01:00', '2011-05-16 02:00', '2011-05-16 03:00', '2011-05-17 02:00', '2011-05-17 03:00', '2011-05-17 04:00', '2011-05-17 05:00', '2011-05-18 02:00', '2011-05-18 03:00', '2011-05-18 04:00', '2011-05-18 05:00']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649]}, index=Index(pd.to_datetime(ts), name='date_time'))
```

### Step 3: Assign expected = df.groupby.idxmax(...)

```python
expected = df.groupby(df.index.date).idxmax()
```

### Step 4: Assign result = df.groupby.apply(...)

```python
result = df.groupby(df.index.date).apply(lambda x: x.idxmax())
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
ts = ['2011-05-16 00:00', '2011-05-16 01:00', '2011-05-16 02:00', '2011-05-16 03:00', '2011-05-17 02:00', '2011-05-17 03:00', '2011-05-17 04:00', '2011-05-17 05:00', '2011-05-18 02:00', '2011-05-18 03:00', '2011-05-18 04:00', '2011-05-18 05:00']
df = DataFrame({'value': [1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649, 1.40893, 1.4076, 1.4075, 1.40649]}, index=Index(pd.to_datetime(ts), name='date_time'))
expected = df.groupby(df.index.date).idxmax()
result = df.groupby(df.index.date).apply(lambda x: x.idxmax())
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*