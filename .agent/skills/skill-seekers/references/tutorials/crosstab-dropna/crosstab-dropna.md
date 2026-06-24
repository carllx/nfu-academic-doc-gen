# How To: Crosstab Dropna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab dropna

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array(['foo', 'foo', 'foo', 'bar', 'bar', 'foo', 'foo'], dtype=object)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array(['one', 'one', 'two', 'one', 'two', 'two', 'two'], dtype=object)
```

### Step 3: Assign c = np.array(...)

```python
c = np.array(['dull', 'dull', 'dull', 'dull', 'dull', 'shiny', 'shiny'], dtype=object)
```

### Step 4: Assign res = crosstab(...)

```python
res = crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'], dropna=False)
```

### Step 5: Assign m = MultiIndex.from_tuples(...)

```python
m = MultiIndex.from_tuples([('one', 'dull'), ('one', 'shiny'), ('two', 'dull'), ('two', 'shiny')], names=['b', 'c'])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res.columns, m)
```


## Complete Example

```python
# Workflow
a = np.array(['foo', 'foo', 'foo', 'bar', 'bar', 'foo', 'foo'], dtype=object)
b = np.array(['one', 'one', 'two', 'one', 'two', 'two', 'two'], dtype=object)
c = np.array(['dull', 'dull', 'dull', 'dull', 'dull', 'shiny', 'shiny'], dtype=object)
res = crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'], dropna=False)
m = MultiIndex.from_tuples([('one', 'dull'), ('one', 'shiny'), ('two', 'dull'), ('two', 'shiny')], names=['b', 'c'])
tm.assert_index_equal(res.columns, m)
```

## Next Steps


---

*Source: test_crosstab.py:225 | Complexity: Intermediate | Last updated: 2026-06-02*