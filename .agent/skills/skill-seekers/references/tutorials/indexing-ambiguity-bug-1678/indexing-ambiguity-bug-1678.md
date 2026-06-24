# How To: Indexing Ambiguity Bug 1678

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indexing ambiguity bug 1678

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('Ohio', 'Green'), ('Ohio', 'Red'), ('Colorado', 'Green')])
```

### Step 2: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(12).reshape((4, 3)), index=index, columns=columns)
```

### Step 4: Assign result = value

```python
result = df.iloc[:, 1]
```

### Step 5: Assign expected = value

```python
expected = df.loc[:, ('Ohio', 'Red')]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
columns = MultiIndex.from_tuples([('Ohio', 'Green'), ('Ohio', 'Red'), ('Colorado', 'Green')])
index = MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
df = DataFrame(np.arange(12).reshape((4, 3)), index=index, columns=columns)
result = df.iloc[:, 1]
expected = df.loc[:, ('Ohio', 'Red')]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*