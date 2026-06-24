# How To: Describe Datetime Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe datetime columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign columns = pd.DatetimeIndex(...)

```python
columns = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'], freq='MS', tz='US/Eastern', name='XXX')
```

**Verification:**
```python
assert result.columns.freq == 'MS'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({0: [10, 20, 30, 40, 50], 1: [10, 20, 30, 40, 50], 2: ['A', 0, None, 'X', 1]})
```

**Verification:**
```python
assert result.columns.tz == expected.columns.tz
```

### Step 3: Assign df.columns = columns

```python
df.columns = columns
```

### Step 4: Assign result = df.describe(...)

```python
result = df.describe()
```

### Step 5: Assign exp_columns = pd.DatetimeIndex(...)

```python
exp_columns = pd.DatetimeIndex(['2011-01-01', '2011-02-01'], freq='MS', tz='US/Eastern', name='XXX')
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [5, 30, df.iloc[:, 0].std(), 10, 20, 30, 40, 50], 1: [5, 30, df.iloc[:, 1].std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
```

### Step 7: Assign expected.columns = exp_columns

```python
expected.columns = exp_columns
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result.columns.freq == 'MS'
```


## Complete Example

```python
# Workflow
columns = pd.DatetimeIndex(['2011-01-01', '2011-02-01', '2011-03-01'], freq='MS', tz='US/Eastern', name='XXX')
df = DataFrame({0: [10, 20, 30, 40, 50], 1: [10, 20, 30, 40, 50], 2: ['A', 0, None, 'X', 1]})
df.columns = columns
result = df.describe()
exp_columns = pd.DatetimeIndex(['2011-01-01', '2011-02-01'], freq='MS', tz='US/Eastern', name='XXX')
expected = DataFrame({0: [5, 30, df.iloc[:, 0].std(), 10, 20, 30, 40, 50], 1: [5, 30, df.iloc[:, 1].std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
expected.columns = exp_columns
tm.assert_frame_equal(result, expected)
assert result.columns.freq == 'MS'
assert result.columns.tz == expected.columns.tz
```

## Next Steps


---

*Source: test_describe.py:172 | Complexity: Advanced | Last updated: 2026-06-02*