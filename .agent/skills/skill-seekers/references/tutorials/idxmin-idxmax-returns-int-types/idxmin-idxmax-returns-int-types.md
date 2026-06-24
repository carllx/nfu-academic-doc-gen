# How To: Idxmin Idxmax Returns Int Types

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test idxmin idxmax returns int types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: func, values, numeric_only
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'name': ['A', 'A', 'B', 'B'], 'c_int': [1, 2, 3, 4], 'c_float': [4.02, 3.03, 2.04, 1.05], 'c_date': ['2019', '2018', '2016', '2017']})
```

### Step 2: Assign unknown = pd.to_datetime(...)

```python
df['c_date'] = pd.to_datetime(df['c_date'])
```

### Step 3: Assign unknown = unknown.dt.tz_localize(...)

```python
df['c_date_tz'] = df['c_date'].dt.tz_localize('US/Pacific')
```

### Step 4: Assign unknown = value

```python
df['c_timedelta'] = df['c_date'] - df['c_date'].iloc[0]
```

### Step 5: Assign unknown = unknown.dt.to_period(...)

```python
df['c_period'] = df['c_date'].dt.to_period('W')
```

### Step 6: Assign unknown = unknown.astype(...)

```python
df['c_Integer'] = df['c_int'].astype('Int64')
```

### Step 7: Assign unknown = unknown.astype(...)

```python
df['c_Floating'] = df['c_float'].astype('Float64')
```

### Step 8: Assign result = getattr(...)

```python
result = getattr(df.groupby('name'), func)(numeric_only=numeric_only)
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(values, index=pd.Index(['A', 'B'], name='name'))
```

### Step 10: Assign unknown = value

```python
expected['c_Integer'] = expected['c_int']
```

### Step 11: Assign unknown = value

```python
expected['c_Floating'] = expected['c_float']
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign expected = expected.drop(...)

```python
expected = expected.drop(columns=['c_date'])
```

### Step 14: Assign unknown = value

```python
expected['c_date_tz'] = expected['c_date']
```

### Step 15: Assign unknown = value

```python
expected['c_timedelta'] = expected['c_date']
```

### Step 16: Assign unknown = value

```python
expected['c_period'] = expected['c_date']
```


## Complete Example

```python
# Setup
# Fixtures: func, values, numeric_only

# Workflow
df = DataFrame({'name': ['A', 'A', 'B', 'B'], 'c_int': [1, 2, 3, 4], 'c_float': [4.02, 3.03, 2.04, 1.05], 'c_date': ['2019', '2018', '2016', '2017']})
df['c_date'] = pd.to_datetime(df['c_date'])
df['c_date_tz'] = df['c_date'].dt.tz_localize('US/Pacific')
df['c_timedelta'] = df['c_date'] - df['c_date'].iloc[0]
df['c_period'] = df['c_date'].dt.to_period('W')
df['c_Integer'] = df['c_int'].astype('Int64')
df['c_Floating'] = df['c_float'].astype('Float64')
result = getattr(df.groupby('name'), func)(numeric_only=numeric_only)
expected = DataFrame(values, index=pd.Index(['A', 'B'], name='name'))
if numeric_only:
    expected = expected.drop(columns=['c_date'])
else:
    expected['c_date_tz'] = expected['c_date']
    expected['c_timedelta'] = expected['c_date']
    expected['c_period'] = expected['c_date']
expected['c_Integer'] = expected['c_int']
expected['c_Floating'] = expected['c_float']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:272 | Complexity: Advanced | Last updated: 2026-06-02*