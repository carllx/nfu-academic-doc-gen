# How To: Groupby Fill Duplicate Column Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby fill duplicate column names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'field1': [1, 3, 4], 'field2': [1, 3, 4]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'field1': [1, np.nan, 4]})
```

### Step 3: Assign df_grouped = pd.concat.groupby(...)

```python
df_grouped = pd.concat([df1, df2], axis=1).groupby(by=['field2'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1.0], [3, np.nan], [4, 4.0]], columns=['field1', 'field1'])
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(df_grouped, func)()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
df1 = DataFrame({'field1': [1, 3, 4], 'field2': [1, 3, 4]})
df2 = DataFrame({'field1': [1, np.nan, 4]})
df_grouped = pd.concat([df1, df2], axis=1).groupby(by=['field2'])
expected = DataFrame([[1, 1.0], [3, np.nan], [4, 4.0]], columns=['field1', 'field1'])
result = getattr(df_grouped, func)()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*