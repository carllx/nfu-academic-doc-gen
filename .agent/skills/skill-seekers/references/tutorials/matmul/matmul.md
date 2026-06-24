# How To: Matmul

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test matmul

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), index=['a', 'b', 'c'], columns=['p', 'q', 'r', 's'])
```

**Verification:**
```python
assert isinstance(result, DataFrame)
```

### Step 2: Assign b = DataFrame(...)

```python
b = DataFrame(np.random.default_rng(2).standard_normal((4, 2)), index=['p', 'q', 'r', 's'], columns=['one', 'two'])
```

**Verification:**
```python
assert result.columns.equals(b.columns)
```

### Step 3: Assign result = operator.matmul(...)

```python
result = operator.matmul(a, b)
```

**Verification:**
```python
assert result.index.equals(Index(range(3)))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = operator.matmul(...)

```python
result = operator.matmul(a, b.one)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(np.dot(a.values, b.one.values), index=['a', 'b', 'c'])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = operator.matmul(...)

```python
result = operator.matmul(a.values, b)
```

**Verification:**
```python
assert isinstance(result, DataFrame)
```

### Step 10: Assign expected = np.dot(...)

```python
expected = np.dot(a.values, b.values)
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.values, expected)
```

### Step 12: Assign result = operator.matmul(...)

```python
result = operator.matmul(a.values.tolist(), b)
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
```

### Step 14: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.values, expected.values)
```

### Step 15: Assign unknown = a.q.round.astype(...)

```python
a['q'] = a.q.round().astype(int)
```

### Step 16: Assign result = operator.matmul(...)

```python
result = operator.matmul(a, b)
```

### Step 17: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 19: Assign a = a.astype(...)

```python
a = a.astype(int)
```

### Step 20: Assign result = operator.matmul(...)

```python
result = operator.matmul(a, b)
```

### Step 21: Assign expected = DataFrame(...)

```python
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 23: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), index=[1, 2, 3], columns=range(4))
```

### Step 24: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), index=range(5), columns=[1, 2, 3])
```

### Step 25: Call operator.matmul()

```python
operator.matmul(df, df2)
```


## Complete Example

```python
# Workflow
a = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), index=['a', 'b', 'c'], columns=['p', 'q', 'r', 's'])
b = DataFrame(np.random.default_rng(2).standard_normal((4, 2)), index=['p', 'q', 'r', 's'], columns=['one', 'two'])
result = operator.matmul(a, b)
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
tm.assert_frame_equal(result, expected)
result = operator.matmul(a, b.one)
expected = Series(np.dot(a.values, b.one.values), index=['a', 'b', 'c'])
tm.assert_series_equal(result, expected)
result = operator.matmul(a.values, b)
assert isinstance(result, DataFrame)
assert result.columns.equals(b.columns)
assert result.index.equals(Index(range(3)))
expected = np.dot(a.values, b.values)
tm.assert_almost_equal(result.values, expected)
result = operator.matmul(a.values.tolist(), b)
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
tm.assert_almost_equal(result.values, expected.values)
a['q'] = a.q.round().astype(int)
result = operator.matmul(a, b)
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
tm.assert_frame_equal(result, expected)
a = a.astype(int)
result = operator.matmul(a, b)
expected = DataFrame(np.dot(a.values, b.values), index=['a', 'b', 'c'], columns=['one', 'two'])
tm.assert_frame_equal(result, expected)
df = DataFrame(np.random.default_rng(2).standard_normal((3, 4)), index=[1, 2, 3], columns=range(4))
df2 = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), index=range(5), columns=[1, 2, 3])
with pytest.raises(ValueError, match='aligned'):
    operator.matmul(df, df2)
```

## Next Steps


---

*Source: test_matmul.py:15 | Complexity: Advanced | Last updated: 2026-06-02*