# How To: Isin Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin multiIndex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([(0, 'a', 'foo'), (0, 'a', 'bar'), (0, 'b', 'bar'), (0, 'b', 'baz'), (2, 'a', 'foo'), (2, 'a', 'bar'), (2, 'c', 'bar'), (2, 'c', 'baz'), (1, 'b', 'foo'), (1, 'b', 'bar'), (1, 'c', 'bar'), (1, 'c', 'baz')])
```

### Step 2: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': np.ones(12), 'B': np.zeros(12)}, index=idx)
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 'B': [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]})
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(False, index=df1.index, columns=df1.columns)
```

### Step 5: Assign result = df1.isin(...)

```python
result = df1.isin(df2)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df2.index = idx

```python
df2.index = idx
```

### Step 8: Assign expected = df2.values.astype(...)

```python
expected = df2.values.astype(bool)
```

### Step 9: Assign unknown = value

```python
expected[:, 1] = ~expected[:, 1]
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected, columns=['A', 'B'], index=idx)
```

### Step 11: Assign result = df1.isin(...)

```python
result = df1.isin(df2)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_tuples([(0, 'a', 'foo'), (0, 'a', 'bar'), (0, 'b', 'bar'), (0, 'b', 'baz'), (2, 'a', 'foo'), (2, 'a', 'bar'), (2, 'c', 'bar'), (2, 'c', 'baz'), (1, 'b', 'foo'), (1, 'b', 'bar'), (1, 'c', 'bar'), (1, 'c', 'baz')])
df1 = DataFrame({'A': np.ones(12), 'B': np.zeros(12)}, index=idx)
df2 = DataFrame({'A': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 'B': [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]})
expected = DataFrame(False, index=df1.index, columns=df1.columns)
result = df1.isin(df2)
tm.assert_frame_equal(result, expected)
df2.index = idx
expected = df2.values.astype(bool)
expected[:, 1] = ~expected[:, 1]
expected = DataFrame(expected, columns=['A', 'B'], index=idx)
result = df1.isin(df2)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:141 | Complexity: Advanced | Last updated: 2026-06-02*