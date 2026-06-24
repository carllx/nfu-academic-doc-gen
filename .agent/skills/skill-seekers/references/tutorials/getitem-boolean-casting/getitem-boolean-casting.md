# How To: Getitem Boolean Casting

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem boolean casting

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: datetime_frame
```

## Step-by-Step Guide

### Step 1: Assign df = datetime_frame.copy(...)

```python
df = datetime_frame.copy()
```

### Step 2: Assign unknown = 1

```python
df['E'] = 1
```

### Step 3: Assign unknown = unknown.astype(...)

```python
df['E'] = df['E'].astype('int32')
```

### Step 4: Assign unknown = unknown.copy(...)

```python
df['E1'] = df['E'].copy()
```

### Step 5: Assign unknown = 1

```python
df['F'] = 1
```

### Step 6: Assign unknown = unknown.astype(...)

```python
df['F'] = df['F'].astype('int64')
```

### Step 7: Assign unknown = unknown.copy(...)

```python
df['F1'] = df['F'].copy()
```

### Step 8: Assign casted = value

```python
casted = df[df > 0]
```

### Step 9: Assign result = value

```python
result = casted.dtypes
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] * 2 + [np.dtype('int64')] * 2, index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign unknown = 0

```python
df.loc[df.index[1:3], ['E1', 'F1']] = 0
```

### Step 13: Assign casted = value

```python
casted = df[df > 0]
```

### Step 14: Assign result = value

```python
result = casted.dtypes
```

### Step 15: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] + [np.dtype('float64')] + [np.dtype('int64')] + [np.dtype('float64')], index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame

# Workflow
df = datetime_frame.copy()
df['E'] = 1
df['E'] = df['E'].astype('int32')
df['E1'] = df['E'].copy()
df['F'] = 1
df['F'] = df['F'].astype('int64')
df['F1'] = df['F'].copy()
casted = df[df > 0]
result = casted.dtypes
expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] * 2 + [np.dtype('int64')] * 2, index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
tm.assert_series_equal(result, expected)
df.loc[df.index[1:3], ['E1', 'F1']] = 0
casted = df[df > 0]
result = casted.dtypes
expected = Series([np.dtype('float64')] * 4 + [np.dtype('int32')] + [np.dtype('float64')] + [np.dtype('int64')] + [np.dtype('float64')], index=['A', 'B', 'C', 'D', 'E', 'E1', 'F', 'F1'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:185 | Complexity: Advanced | Last updated: 2026-06-02*