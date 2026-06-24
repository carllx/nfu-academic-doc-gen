# How To: Ignore Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ignore multiindex

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = pd.MultiIndex.from_tuples(...)

```python
index = pd.MultiIndex.from_tuples([('first', 'second'), ('first', 'third')], names=['baz', 'foobar'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'foo': [0, 1], 'bar': [2, 3]}, index=index)
```

### Step 3: Assign result = melt(...)

```python
result = melt(df, ignore_index=False)
```

### Step 4: Assign expected_index = pd.MultiIndex.from_tuples(...)

```python
expected_index = pd.MultiIndex.from_tuples([('first', 'second'), ('first', 'third')] * 2, names=['baz', 'foobar'])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'variable': ['foo'] * 2 + ['bar'] * 2, 'value': [0, 1, 2, 3]}, index=expected_index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = pd.MultiIndex.from_tuples([('first', 'second'), ('first', 'third')], names=['baz', 'foobar'])
df = DataFrame({'foo': [0, 1], 'bar': [2, 3]}, index=index)
result = melt(df, ignore_index=False)
expected_index = pd.MultiIndex.from_tuples([('first', 'second'), ('first', 'third')] * 2, names=['baz', 'foobar'])
expected = DataFrame({'variable': ['foo'] * 2 + ['bar'] * 2, 'value': [0, 1, 2, 3]}, index=expected_index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_melt.py:387 | Complexity: Intermediate | Last updated: 2026-06-02*