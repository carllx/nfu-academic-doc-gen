# How To: Rank Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: ser, results
```

## Step-by-Step Guide

### Step 1: Assign unknown = results

```python
method, exp = results
```

### Step 2: Assign s = ser.dropna.astype(...)

```python
s = ser.dropna().astype('i8')
```

### Step 3: Assign result = s.rank(...)

```python
result = s.rank(method=method)
```

### Step 4: Assign expected = Series.dropna(...)

```python
expected = Series(exp).dropna()
```

### Step 5: Assign expected.index = value

```python
expected.index = result.index
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ser, results

# Workflow
method, exp = results
s = ser.dropna().astype('i8')
result = s.rank(method=method)
expected = Series(exp).dropna()
expected.index = result.index
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:403 | Complexity: Intermediate | Last updated: 2026-06-02*