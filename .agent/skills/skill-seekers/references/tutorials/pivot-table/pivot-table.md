# How To: Pivot Table

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: observed, data
```

## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = ['A', 'B']
```

**Verification:**
```python
assert table.index.names == tuple(index)
```

### Step 2: Assign columns = 'C'

```python
columns = 'C'
```

**Verification:**
```python
assert table.index.name == index[0]
```

### Step 3: Assign table = pivot_table(...)

```python
table = pivot_table(data, values='D', index=index, columns=columns, observed=observed)
```

**Verification:**
```python
assert table.columns.names == columns
```

### Step 4: Assign table2 = data.pivot_table(...)

```python
table2 = data.pivot_table(values='D', index=index, columns=columns, observed=observed)
```

**Verification:**
```python
assert table.columns.name == columns[0]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(table, table2)
```

### Step 6: Call pivot_table()

```python
pivot_table(data, values='D', index=index, observed=observed)
```

### Step 7: Assign expected = unknown.agg.unstack(...)

```python
expected = data.groupby(index + [columns])['D'].agg('mean').unstack()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(table, expected)
```

**Verification:**
```python
assert table.index.names == tuple(index)
```


## Complete Example

```python
# Setup
# Fixtures: observed, data

# Workflow
index = ['A', 'B']
columns = 'C'
table = pivot_table(data, values='D', index=index, columns=columns, observed=observed)
table2 = data.pivot_table(values='D', index=index, columns=columns, observed=observed)
tm.assert_frame_equal(table, table2)
pivot_table(data, values='D', index=index, observed=observed)
if len(index) > 1:
    assert table.index.names == tuple(index)
else:
    assert table.index.name == index[0]
if len(columns) > 1:
    assert table.columns.names == columns
else:
    assert table.columns.name == columns[0]
expected = data.groupby(index + [columns])['D'].agg('mean').unstack()
tm.assert_frame_equal(table, expected)
```

## Next Steps


---

*Source: test_pivot.py:94 | Complexity: Advanced | Last updated: 2026-06-02*