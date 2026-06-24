# How To: Frame On

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame on

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'B': range(5), 'C': date_range('20130101 09:00:00', periods=5, freq='3s')})
```

### Step 2: Assign unknown = value

```python
df['A'] = [Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]
```

### Step 3: Assign expected = df.set_index.rolling.B.sum.reset_index(...)

```python
expected = df.set_index('A').rolling('2s').B.sum().reset_index(drop=True)
```

### Step 4: Assign result = df.rolling.B.sum(...)

```python
result = df.rolling('2s', on='A').B.sum()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = df.set_index('A').rolling('2s')[['B']].sum().reset_index()[['B', 'A']]
```

### Step 7: Assign result = unknown.sum(...)

```python
result = df.rolling('2s', on='A')[['B']].sum()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'B': range(5), 'C': date_range('20130101 09:00:00', periods=5, freq='3s')})
df['A'] = [Timestamp('20130101 09:00:00'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:05'), Timestamp('20130101 09:00:06')]
expected = df.set_index('A').rolling('2s').B.sum().reset_index(drop=True)
result = df.rolling('2s', on='A').B.sum()
tm.assert_series_equal(result, expected)
expected = df.set_index('A').rolling('2s')[['B']].sum().reset_index()[['B', 'A']]
result = df.rolling('2s', on='A')[['B']].sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timeseries_window.py:152 | Complexity: Advanced | Last updated: 2026-06-02*