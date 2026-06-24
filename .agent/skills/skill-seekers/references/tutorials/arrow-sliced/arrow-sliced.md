# How To: Arrow Sliced

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arrow sliced

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.arrow._arrow_utils`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': data})
```

### Step 2: Assign table = pa.table(...)

```python
table = pa.table(df)
```

### Step 3: Assign result = table.slice.to_pandas(...)

```python
result = table.slice(2, None).to_pandas()
```

### Step 4: Assign expected = unknown.reset_index(...)

```python
expected = df.iloc[2:].reset_index(drop=True)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df2 = df.fillna(...)

```python
df2 = df.fillna(data[0])
```

### Step 7: Assign table = pa.table(...)

```python
table = pa.table(df2)
```

### Step 8: Assign result = table.slice.to_pandas(...)

```python
result = table.slice(2, None).to_pandas()
```

### Step 9: Assign expected = unknown.reset_index(...)

```python
expected = df2.iloc[2:].reset_index(drop=True)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
df = pd.DataFrame({'a': data})
table = pa.table(df)
result = table.slice(2, None).to_pandas()
expected = df.iloc[2:].reset_index(drop=True)
tm.assert_frame_equal(result, expected)
df2 = df.fillna(data[0])
table = pa.table(df2)
result = table.slice(2, None).to_pandas()
expected = df2.iloc[2:].reset_index(drop=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow_compat.py:95 | Complexity: Advanced | Last updated: 2026-06-02*