# How To: Slicing Doc Examples

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slicing doc examples

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cats = Categorical(...)

```python
cats = Categorical(['a', 'b', 'b', 'b', 'c', 'c', 'c'], categories=['a', 'b', 'c'])
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
```

### Step 3: Assign values = value

```python
values = [1, 2, 2, 2, 3, 4, 5]
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'cats': cats, 'values': values}, index=idx)
```

### Step 5: Assign result = value

```python
result = df.iloc[2:4, :]
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'cats': Categorical(['b', 'b'], categories=['a', 'b', 'c']), 'values': [2, 2]}, index=['j', 'k'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.iloc[2:4, :].dtypes
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(['category', 'int64'], ['cats', 'values'], dtype=object)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = df.loc['h':'j', 'cats']
```

### Step 12: Assign expected = Series(...)

```python
expected = Series(Categorical(['a', 'b', 'b'], categories=['a', 'b', 'c']), index=['h', 'i', 'j'], name='cats')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign result = value

```python
result = df.loc['h':'j', df.columns[0:1]]
```

### Step 15: Assign expected = DataFrame(...)

```python
expected = DataFrame({'cats': Categorical(['a', 'b', 'b'], categories=['a', 'b', 'c'])}, index=['h', 'i', 'j'])
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
cats = Categorical(['a', 'b', 'b', 'b', 'c', 'c', 'c'], categories=['a', 'b', 'c'])
idx = Index(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
values = [1, 2, 2, 2, 3, 4, 5]
df = DataFrame({'cats': cats, 'values': values}, index=idx)
result = df.iloc[2:4, :]
expected = DataFrame({'cats': Categorical(['b', 'b'], categories=['a', 'b', 'c']), 'values': [2, 2]}, index=['j', 'k'])
tm.assert_frame_equal(result, expected)
result = df.iloc[2:4, :].dtypes
expected = Series(['category', 'int64'], ['cats', 'values'], dtype=object)
tm.assert_series_equal(result, expected)
result = df.loc['h':'j', 'cats']
expected = Series(Categorical(['a', 'b', 'b'], categories=['a', 'b', 'c']), index=['h', 'i', 'j'], name='cats')
tm.assert_series_equal(result, expected)
result = df.loc['h':'j', df.columns[0:1]]
expected = DataFrame({'cats': Categorical(['a', 'b', 'b'], categories=['a', 'b', 'c'])}, index=['h', 'i', 'j'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:259 | Complexity: Advanced | Last updated: 2026-06-02*