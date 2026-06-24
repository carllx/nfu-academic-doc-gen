# How To: Asfreq With Unsorted Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq with unsorted index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = to_datetime(...)

```python
index = to_datetime(['2021-01-04', '2021-01-02', '2021-01-03', '2021-01-01'])
```

### Step 2: Assign result = frame_or_series(...)

```python
result = frame_or_series(range(4), index=index)
```

### Step 3: Assign expected = result.reindex(...)

```python
expected = result.reindex(sorted(index))
```

### Step 4: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq('infer')
```

### Step 5: Assign result = result.asfreq(...)

```python
result = result.asfreq('D')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
index = to_datetime(['2021-01-04', '2021-01-02', '2021-01-03', '2021-01-01'])
result = frame_or_series(range(4), index=index)
expected = result.reindex(sorted(index))
expected.index = expected.index._with_freq('infer')
result = result.asfreq('D')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_asfreq.py:202 | Complexity: Intermediate | Last updated: 2026-06-02*