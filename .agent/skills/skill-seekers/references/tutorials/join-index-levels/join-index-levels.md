# How To: Join Index Levels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join index levels

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx, midx = MultiIndex.from_tuples(...)

```python
midx = midx = MultiIndex.from_tuples([('a', '2019-02-01'), ('a', '2019-02-01')])
```

### Step 2: Assign midx2 = MultiIndex.from_tuples(...)

```python
midx2 = MultiIndex.from_tuples([('a', '2019-01-31')])
```

### Step 3: Assign result = midx.join(...)

```python
result = midx.join(midx2, how='outer')
```

### Step 4: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([('a', '2019-01-31'), ('a', '2019-02-01'), ('a', '2019-02-01')])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.levels[1], expected.levels[1])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
midx = midx = MultiIndex.from_tuples([('a', '2019-02-01'), ('a', '2019-02-01')])
midx2 = MultiIndex.from_tuples([('a', '2019-01-31')])
result = midx.join(midx2, how='outer')
expected = MultiIndex.from_tuples([('a', '2019-01-31'), ('a', '2019-02-01'), ('a', '2019-02-01')])
tm.assert_index_equal(result.levels[1], expected.levels[1])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*