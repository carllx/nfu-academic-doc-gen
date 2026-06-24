# How To: Partial Set

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test partial set

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

**Verification:**
```python
assert df['A'].iloc[14] == exp['A'].iloc[14]
```

### Step 2: Assign df = ymd.copy(...)

```python
df = ymd.copy()
```

**Verification:**
```python
assert df['A'].iloc[14] == 5
```

### Step 3: Assign exp = ymd.copy(...)

```python
exp = ymd.copy()
```

### Step 4: Assign unknown = 0

```python
df.loc[2000, 4] = 0
```

### Step 5: Assign unknown = 0

```python
exp.iloc[65:85] = 0
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```

### Step 7: Assign unknown = 1

```python
exp.iloc[65:85, 0] = 1
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```

### Step 9: Assign unknown = 5

```python
df.loc[2000] = 5
```

### Step 10: Assign unknown = 5

```python
exp.iloc[:100] = 5
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```

### Step 12: Assign unknown = 1

```python
df.loc[(2000, 4), 'A'] = 1
```

### Step 13: Assign unknown = 5

```python
df['A'].iloc[14] = 5
```

**Verification:**
```python
assert df['A'].iloc[14] == exp['A'].iloc[14]
```

### Step 14: Assign unknown = 1

```python
df['A'].loc[2000, 4] = 1
```

### Step 15: Assign unknown = 1

```python
df['A'].loc[2000, 4] = 1
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data, using_copy_on_write, warn_copy_on_write

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
df = ymd.copy()
exp = ymd.copy()
df.loc[2000, 4] = 0
exp.iloc[65:85] = 0
tm.assert_frame_equal(df, exp)
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['A'].loc[2000, 4] = 1
    df.loc[(2000, 4), 'A'] = 1
else:
    with tm.raises_chained_assignment_error():
        df['A'].loc[2000, 4] = 1
exp.iloc[65:85, 0] = 1
tm.assert_frame_equal(df, exp)
df.loc[2000] = 5
exp.iloc[:100] = 5
tm.assert_frame_equal(df, exp)
with tm.raises_chained_assignment_error():
    df['A'].iloc[14] = 5
if using_copy_on_write:
    assert df['A'].iloc[14] == exp['A'].iloc[14]
else:
    assert df['A'].iloc[14] == 5
```

## Next Steps


---

*Source: test_partial.py:124 | Complexity: Advanced | Last updated: 2026-06-02*