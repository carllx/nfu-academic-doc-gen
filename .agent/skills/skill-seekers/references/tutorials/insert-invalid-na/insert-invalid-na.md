# How To: Insert Invalid Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert invalid na

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['4day', '1day', '2day'], name='idx')
```

### Step 2: Assign item = np.datetime64(...)

```python
item = np.datetime64('NaT')
```

### Step 3: Assign result = idx.insert(...)

```python
result = idx.insert(0, item)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([item] + list(idx), dtype=object, name='idx')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign item2 = np.datetime64(...)

```python
item2 = np.datetime64('NaT')
```

### Step 7: Assign result = idx.insert(...)

```python
result = idx.insert(0, item2)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['4day', '1day', '2day'], name='idx')
item = np.datetime64('NaT')
result = idx.insert(0, item)
expected = Index([item] + list(idx), dtype=object, name='idx')
tm.assert_index_equal(result, expected)
item2 = np.datetime64('NaT')
result = idx.insert(0, item2)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_insert.py:86 | Complexity: Advanced | Last updated: 2026-06-02*