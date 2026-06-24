# How To: Aggregate Api Consistency

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test aggregate api consistency

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.printing`
- `pandas.tests.extension.decimal.array`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': np.random.default_rng(2).standard_normal(8) + 1.0, 'D': np.arange(8)})
```

### Step 2: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(['A', 'B'])
```

### Step 3: Assign c_mean = unknown.mean(...)

```python
c_mean = grouped['C'].mean()
```

### Step 4: Assign c_sum = unknown.sum(...)

```python
c_sum = grouped['C'].sum()
```

### Step 5: Assign d_mean = unknown.mean(...)

```python
d_mean = grouped['D'].mean()
```

### Step 6: Assign d_sum = unknown.sum(...)

```python
d_sum = grouped['D'].sum()
```

### Step 7: Assign result = unknown.agg(...)

```python
result = grouped['D'].agg(['sum', 'mean'])
```

### Step 8: Assign expected = pd.concat(...)

```python
expected = pd.concat([d_sum, d_mean], axis=1)
```

### Step 9: Assign expected.columns = value

```python
expected.columns = ['sum', 'mean']
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```

### Step 11: Assign result = grouped.agg(...)

```python
result = grouped.agg(['sum', 'mean'])
```

### Step 12: Assign expected = pd.concat(...)

```python
expected = pd.concat([c_sum, c_mean, d_sum, d_mean], axis=1)
```

### Step 13: Assign expected.columns = MultiIndex.from_product(...)

```python
expected.columns = MultiIndex.from_product([['C', 'D'], ['sum', 'mean']])
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```

### Step 15: Assign result = unknown.agg(...)

```python
result = grouped[['D', 'C']].agg(['sum', 'mean'])
```

### Step 16: Assign expected = pd.concat(...)

```python
expected = pd.concat([d_sum, d_mean, c_sum, c_mean], axis=1)
```

### Step 17: Assign expected.columns = MultiIndex.from_product(...)

```python
expected.columns = MultiIndex.from_product([['D', 'C'], ['sum', 'mean']])
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```

### Step 19: Assign result = grouped.agg(...)

```python
result = grouped.agg({'C': 'mean', 'D': 'sum'})
```

### Step 20: Assign expected = pd.concat(...)

```python
expected = pd.concat([d_sum, c_mean], axis=1)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```

### Step 22: Assign result = grouped.agg(...)

```python
result = grouped.agg({'C': ['mean', 'sum'], 'D': ['mean', 'sum']})
```

### Step 23: Assign expected = pd.concat(...)

```python
expected = pd.concat([c_mean, c_sum, d_mean, d_sum], axis=1)
```

### Step 24: Assign expected.columns = MultiIndex.from_product(...)

```python
expected.columns = MultiIndex.from_product([['C', 'D'], ['mean', 'sum']])
```

### Step 25: Assign msg = "Column\\(s\\) \\['r', 'r2'\\] do not exist"

```python
msg = "Column\\(s\\) \\['r', 'r2'\\] do not exist"
```

### Step 26: Call unknown.agg()

```python
grouped[['D', 'C']].agg({'r': 'sum', 'r2': 'mean'})
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': np.random.default_rng(2).standard_normal(8) + 1.0, 'D': np.arange(8)})
grouped = df.groupby(['A', 'B'])
c_mean = grouped['C'].mean()
c_sum = grouped['C'].sum()
d_mean = grouped['D'].mean()
d_sum = grouped['D'].sum()
result = grouped['D'].agg(['sum', 'mean'])
expected = pd.concat([d_sum, d_mean], axis=1)
expected.columns = ['sum', 'mean']
tm.assert_frame_equal(result, expected, check_like=True)
result = grouped.agg(['sum', 'mean'])
expected = pd.concat([c_sum, c_mean, d_sum, d_mean], axis=1)
expected.columns = MultiIndex.from_product([['C', 'D'], ['sum', 'mean']])
tm.assert_frame_equal(result, expected, check_like=True)
result = grouped[['D', 'C']].agg(['sum', 'mean'])
expected = pd.concat([d_sum, d_mean, c_sum, c_mean], axis=1)
expected.columns = MultiIndex.from_product([['D', 'C'], ['sum', 'mean']])
tm.assert_frame_equal(result, expected, check_like=True)
result = grouped.agg({'C': 'mean', 'D': 'sum'})
expected = pd.concat([d_sum, c_mean], axis=1)
tm.assert_frame_equal(result, expected, check_like=True)
result = grouped.agg({'C': ['mean', 'sum'], 'D': ['mean', 'sum']})
expected = pd.concat([c_mean, c_sum, d_mean, d_sum], axis=1)
expected.columns = MultiIndex.from_product([['C', 'D'], ['mean', 'sum']])
msg = "Column\\(s\\) \\['r', 'r2'\\] do not exist"
with pytest.raises(KeyError, match=msg):
    grouped[['D', 'C']].agg({'r': 'sum', 'r2': 'mean'})
```

## Next Steps


---

*Source: test_other.py:170 | Complexity: Advanced | Last updated: 2026-06-02*