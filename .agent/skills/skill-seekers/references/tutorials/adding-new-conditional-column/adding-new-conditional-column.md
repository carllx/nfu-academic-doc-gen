# How To: Adding New Conditional Column

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test adding new conditional column

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1]})
```

### Step 2: Assign unknown = '1'

```python
df.loc[df['x'] == 1, 'y'] = '1'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [1], 'y': ['1']})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1]})
```

### Step 6: Assign value = value

```python
value = lambda x: x
```

### Step 7: Assign unknown = value

```python
df.loc[df['x'] == 1, 'y'] = value
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'x': [1], 'y': [value]})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'x': [1]})
df.loc[df['x'] == 1, 'y'] = '1'
expected = DataFrame({'x': [1], 'y': ['1']})
tm.assert_frame_equal(df, expected)
df = DataFrame({'x': [1]})
value = lambda x: x
df.loc[df['x'] == 1, 'y'] = value
expected = DataFrame({'x': [1], 'y': [value]})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_indexing.py:1936 | Complexity: Advanced | Last updated: 2026-06-02*