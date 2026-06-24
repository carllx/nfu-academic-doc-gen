# How To: Grouping By Key Is In Axis

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test grouping by key is in axis

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'a': [1, 1, 2], 'b': [1, 1, 2], 'c': [3, 4, 5]}).set_index('a')
```

**Verification:**
```python
assert not gb._grouper.groupings[0].in_axis
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby([Grouper(level='a'), Grouper(key='b')], as_index=False)
```

**Verification:**
```python
assert gb._grouper.groupings[1].in_axis
```

### Step 3: Assign msg = 'A grouping .* was excluded from the result'

```python
msg = 'A grouping .* was excluded from the result'
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [1, 2], 'c': [7, 5]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = gb.sum(...)

```python
result = gb.sum()
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, 2], 'b': [1, 1, 2], 'c': [3, 4, 5]}).set_index('a')
gb = df.groupby([Grouper(level='a'), Grouper(key='b')], as_index=False)
assert not gb._grouper.groupings[0].in_axis
assert gb._grouper.groupings[1].in_axis
msg = 'A grouping .* was excluded from the result'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = gb.sum()
expected = DataFrame({'b': [1, 2], 'c': [7, 5]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:1185 | Complexity: Intermediate | Last updated: 2026-06-02*