# How To: Join Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign f = value

```python
f = float_frame.loc[float_frame.index[:10], ['A', 'B']]
```

### Step 2: Assign f2 = value

```python
f2 = float_frame.loc[float_frame.index[5:], ['C', 'D']].iloc[::-1]
```

### Step 3: Assign joined = f.join(...)

```python
joined = f.join(f2)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(f.index, joined.index)
```

### Step 5: Assign expected_columns = Index(...)

```python
expected_columns = Index(['A', 'B', 'C', 'D'])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.columns, expected_columns)
```

### Step 7: Assign joined = f.join(...)

```python
joined = f.join(f2, how='left')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.index, f.index)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.columns, expected_columns)
```

### Step 10: Assign joined = f.join(...)

```python
joined = f.join(f2, how='right')
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.index, f2.index)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.columns, expected_columns)
```

### Step 13: Assign joined = f.join(...)

```python
joined = f.join(f2, how='inner')
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.index, f.index[5:10])
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.columns, expected_columns)
```

### Step 16: Assign joined = f.join(...)

```python
joined = f.join(f2, how='outer')
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.index, float_frame.index.sort_values())
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(joined.columns, expected_columns)
```

### Step 19: Assign msg = 'columns overlap but no suffix'

```python
msg = 'columns overlap but no suffix'
```

### Step 20: Call f.join()

```python
f.join(f2, how='foo')
```

### Step 21: Call float_frame.join()

```python
float_frame.join(float_frame, how=how)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
f = float_frame.loc[float_frame.index[:10], ['A', 'B']]
f2 = float_frame.loc[float_frame.index[5:], ['C', 'D']].iloc[::-1]
joined = f.join(f2)
tm.assert_index_equal(f.index, joined.index)
expected_columns = Index(['A', 'B', 'C', 'D'])
tm.assert_index_equal(joined.columns, expected_columns)
joined = f.join(f2, how='left')
tm.assert_index_equal(joined.index, f.index)
tm.assert_index_equal(joined.columns, expected_columns)
joined = f.join(f2, how='right')
tm.assert_index_equal(joined.index, f2.index)
tm.assert_index_equal(joined.columns, expected_columns)
joined = f.join(f2, how='inner')
tm.assert_index_equal(joined.index, f.index[5:10])
tm.assert_index_equal(joined.columns, expected_columns)
joined = f.join(f2, how='outer')
tm.assert_index_equal(joined.index, float_frame.index.sort_values())
tm.assert_index_equal(joined.columns, expected_columns)
with pytest.raises(ValueError, match='join method'):
    f.join(f2, how='foo')
msg = 'columns overlap but no suffix'
for how in ('outer', 'left', 'inner'):
    with pytest.raises(ValueError, match=msg):
        float_frame.join(float_frame, how=how)
```

## Next Steps


---

*Source: test_join.py:264 | Complexity: Advanced | Last updated: 2026-06-02*