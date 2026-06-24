# How To: Rolling Functions Window Non Shrinkage

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling functions window non shrinkage

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: f
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(4))
```

### Step 2: Assign s_expected = Series(...)

```python
s_expected = Series(np.nan, index=s.index)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 5], [3, 2], [3, 9], [-1, 0]], columns=['A', 'B'])
```

### Step 4: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame(np.nan, index=df.index, columns=df.columns)
```

### Step 5: Assign s_result = f(...)

```python
s_result = f(s)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s_result, s_expected)
```

### Step 7: Assign df_result = f(...)

```python
df_result = f(df)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_result, df_expected)
```


## Complete Example

```python
# Setup
# Fixtures: f

# Workflow
s = Series(range(4))
s_expected = Series(np.nan, index=s.index)
df = DataFrame([[1, 5], [3, 2], [3, 9], [-1, 0]], columns=['A', 'B'])
df_expected = DataFrame(np.nan, index=df.index, columns=df.columns)
s_result = f(s)
tm.assert_series_equal(s_result, s_expected)
df_result = f(df)
tm.assert_frame_equal(df_result, df_expected)
```

## Next Steps


---

*Source: test_rolling_functions.py:353 | Complexity: Advanced | Last updated: 2026-06-02*