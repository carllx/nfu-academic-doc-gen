# How To: Xs Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign df = multiindex_dataframe_random_data

```python
df = multiindex_dataframe_random_data
```

### Step 2: Assign result = df.xs(...)

```python
result = df.xs('two', level='second')
```

### Step 3: Assign expected = value

```python
expected = df[df.index.get_level_values(1) == 'two']
```

### Step 4: Assign expected.index = Index(...)

```python
expected.index = Index(['foo', 'bar', 'baz', 'qux'], name='first')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
df = multiindex_dataframe_random_data
result = df.xs('two', level='second')
expected = df[df.index.get_level_values(1) == 'two']
expected.index = Index(['foo', 'bar', 'baz', 'qux'], name='first')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*