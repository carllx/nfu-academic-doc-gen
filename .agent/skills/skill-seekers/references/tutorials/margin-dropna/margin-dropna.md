# How To: Margin Dropna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test margin dropna

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 2, 2, 2, np.nan], 'b': [3, 3, 4, 4, 4, 4]})
```

### Step 2: Assign actual = crosstab(...)

```python
actual = crosstab(df.a, df.b, margins=True, dropna=True)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 0, 1], [1, 3, 4], [2, 3, 5]])
```

### Step 4: Assign expected.index = Index(...)

```python
expected.index = Index([1.0, 2.0, 'All'], name='a')
```

### Step 5: Assign expected.columns = Index(...)

```python
expected.columns = Index([3, 4, 'All'], name='b')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 2, 2, 2, np.nan], 'b': [3, 3, 4, 4, 4, 4]})
actual = crosstab(df.a, df.b, margins=True, dropna=True)
expected = DataFrame([[1, 0, 1], [1, 3, 4], [2, 3, 5]])
expected.index = Index([1.0, 2.0, 'All'], name='a')
expected.columns = Index([3, 4, 'All'], name='b')
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_crosstab.py:253 | Complexity: Intermediate | Last updated: 2026-06-02*