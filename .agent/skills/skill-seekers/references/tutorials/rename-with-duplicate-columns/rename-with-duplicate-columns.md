# How To: Rename With Duplicate Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename with duplicate columns

## Prerequisites

**Required Modules:**
- `collections`
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df4 = DataFrame(...)

```python
df4 = DataFrame({'RT': [0.0454], 'TClose': [22.02], 'TExg': [0.0422]}, index=MultiIndex.from_tuples([(600809, 20130331)], names=['STK_ID', 'RPT_Date']))
```

### Step 2: Assign df5 = DataFrame(...)

```python
df5 = DataFrame({'RPT_Date': [20120930, 20121231, 20130331], 'STK_ID': [600809] * 3, 'STK_Name': ['饡驦', '饡驦', '饡驦'], 'TClose': [38.05, 41.66, 30.01]}, index=MultiIndex.from_tuples([(600809, 20120930), (600809, 20121231), (600809, 20130331)], names=['STK_ID', 'RPT_Date']))
```

### Step 3: Assign k = merge(...)

```python
k = merge(df4, df5, how='inner', left_index=True, right_index=True)
```

### Step 4: Assign result = k.rename(...)

```python
result = k.rename(columns={'TClose_x': 'TClose', 'TClose_y': 'QT_Close'})
```

### Step 5: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame([[0.0454, 22.02, 0.0422, 20130331, 600809, '饡驦', 30.01]], columns=['RT', 'TClose', 'TExg', 'RPT_Date', 'STK_ID', 'STK_Name', 'QT_Close']).set_index(['STK_ID', 'RPT_Date'], drop=False)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df4 = DataFrame({'RT': [0.0454], 'TClose': [22.02], 'TExg': [0.0422]}, index=MultiIndex.from_tuples([(600809, 20130331)], names=['STK_ID', 'RPT_Date']))
df5 = DataFrame({'RPT_Date': [20120930, 20121231, 20130331], 'STK_ID': [600809] * 3, 'STK_Name': ['饡驦', '饡驦', '饡驦'], 'TClose': [38.05, 41.66, 30.01]}, index=MultiIndex.from_tuples([(600809, 20120930), (600809, 20121231), (600809, 20130331)], names=['STK_ID', 'RPT_Date']))
k = merge(df4, df5, how='inner', left_index=True, right_index=True)
result = k.rename(columns={'TClose_x': 'TClose', 'TClose_y': 'QT_Close'})
expected = DataFrame([[0.0454, 22.02, 0.0422, 20130331, 600809, '饡驦', 30.01]], columns=['RT', 'TClose', 'TExg', 'RPT_Date', 'STK_ID', 'STK_Name', 'QT_Close']).set_index(['STK_ID', 'RPT_Date'], drop=False)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rename.py:367 | Complexity: Intermediate | Last updated: 2026-06-02*