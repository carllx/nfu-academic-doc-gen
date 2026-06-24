# How To: Merge Datetime Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge datetime index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([1, 2, 3], ['2016-01-01', '2017-01-01', '2018-01-01'], columns=['a'])
```

### Step 2: Assign df.index = pd.to_datetime(...)

```python
df.index = pd.to_datetime(df.index)
```

### Step 3: Assign on_vector = value

```python
on_vector = df.index.year
```

### Step 4: Assign exp_years = np.array(...)

```python
exp_years = np.array([2016, 2017, 2018], dtype=np.int32)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'key_1': exp_years})
```

### Step 6: Assign result = df.merge(...)

```python
result = df.merge(df, on=['a', on_vector], how='inner')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key_0': exp_years, 'a_x': [1, 2, 3], 'a_y': [1, 2, 3]})
```

### Step 9: Assign result = df.merge(...)

```python
result = df.merge(df, on=[df.index.year], how='inner')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign on_vector = klass(...)

```python
on_vector = klass(on_vector)
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
df = DataFrame([1, 2, 3], ['2016-01-01', '2017-01-01', '2018-01-01'], columns=['a'])
df.index = pd.to_datetime(df.index)
on_vector = df.index.year
if klass is not None:
    on_vector = klass(on_vector)
exp_years = np.array([2016, 2017, 2018], dtype=np.int32)
expected = DataFrame({'a': [1, 2, 3], 'key_1': exp_years})
result = df.merge(df, on=['a', on_vector], how='inner')
tm.assert_frame_equal(result, expected)
expected = DataFrame({'key_0': exp_years, 'a_x': [1, 2, 3], 'a_y': [1, 2, 3]})
result = df.merge(df, on=[df.index.year], how='inner')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:451 | Complexity: Advanced | Last updated: 2026-06-02*