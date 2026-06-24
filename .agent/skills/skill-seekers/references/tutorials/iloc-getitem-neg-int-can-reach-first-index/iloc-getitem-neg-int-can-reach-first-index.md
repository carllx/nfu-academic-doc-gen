# How To: Iloc Getitem Neg Int Can Reach First Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem neg int can reach first index

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [2, 3, 5], 'B': [7, 11, 13]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign s = value

```python
s = df['A']
```

### Step 3: Assign expected = value

```python
expected = df.iloc[0]
```

### Step 4: Assign result = value

```python
result = df.iloc[-3]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = df.iloc[[0]]
```

### Step 7: Assign result = value

```python
result = df.iloc[[-3]]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected = value

```python
expected = s.iloc[0]
```

### Step 10: Assign result = value

```python
result = s.iloc[-3]
```

**Verification:**
```python
assert result == expected
```

### Step 11: Assign expected = value

```python
expected = s.iloc[[0]]
```

### Step 12: Assign result = value

```python
result = s.iloc[[-3]]
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(['a'], index=['A'])
```

### Step 15: Assign result = value

```python
result = expected.iloc[[-1]]
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [2, 3, 5], 'B': [7, 11, 13]})
s = df['A']
expected = df.iloc[0]
result = df.iloc[-3]
tm.assert_series_equal(result, expected)
expected = df.iloc[[0]]
result = df.iloc[[-3]]
tm.assert_frame_equal(result, expected)
expected = s.iloc[0]
result = s.iloc[-3]
assert result == expected
expected = s.iloc[[0]]
result = s.iloc[[-3]]
tm.assert_series_equal(result, expected)
expected = Series(['a'], index=['A'])
result = expected.iloc[[-1]]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:297 | Complexity: Advanced | Last updated: 2026-06-02*