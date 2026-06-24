# How To: Concat Axis Parameter

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat axis parameter

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [0.1, 0.2]}, index=range(2))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [0.3, 0.4]}, index=range(2))
```

### Step 3: Assign expected_index = DataFrame(...)

```python
expected_index = DataFrame({'A': [0.1, 0.2, 0.3, 0.4]}, index=[0, 1, 0, 1])
```

### Step 4: Assign concatted_index = concat(...)

```python
concatted_index = concat([df1, df2], axis='index')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_index, expected_index)
```

### Step 6: Assign concatted_row = concat(...)

```python
concatted_row = concat([df1, df2], axis='rows')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_row, expected_index)
```

### Step 8: Assign concatted_0 = concat(...)

```python
concatted_0 = concat([df1, df2], axis=0)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_0, expected_index)
```

### Step 10: Assign expected_columns = DataFrame(...)

```python
expected_columns = DataFrame([[0.1, 0.3], [0.2, 0.4]], index=[0, 1], columns=['A', 'A'])
```

### Step 11: Assign concatted_columns = concat(...)

```python
concatted_columns = concat([df1, df2], axis='columns')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_columns, expected_columns)
```

### Step 13: Assign concatted_1 = concat(...)

```python
concatted_1 = concat([df1, df2], axis=1)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_1, expected_columns)
```

### Step 15: Assign series1 = Series(...)

```python
series1 = Series([0.1, 0.2])
```

### Step 16: Assign series2 = Series(...)

```python
series2 = Series([0.3, 0.4])
```

### Step 17: Assign expected_index_series = Series(...)

```python
expected_index_series = Series([0.1, 0.2, 0.3, 0.4], index=[0, 1, 0, 1])
```

### Step 18: Assign concatted_index_series = concat(...)

```python
concatted_index_series = concat([series1, series2], axis='index')
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(concatted_index_series, expected_index_series)
```

### Step 20: Assign concatted_row_series = concat(...)

```python
concatted_row_series = concat([series1, series2], axis='rows')
```

### Step 21: Call tm.assert_series_equal()

```python
tm.assert_series_equal(concatted_row_series, expected_index_series)
```

### Step 22: Assign concatted_0_series = concat(...)

```python
concatted_0_series = concat([series1, series2], axis=0)
```

### Step 23: Call tm.assert_series_equal()

```python
tm.assert_series_equal(concatted_0_series, expected_index_series)
```

### Step 24: Assign expected_columns_series = DataFrame(...)

```python
expected_columns_series = DataFrame([[0.1, 0.3], [0.2, 0.4]], index=[0, 1], columns=[0, 1])
```

### Step 25: Assign concatted_columns_series = concat(...)

```python
concatted_columns_series = concat([series1, series2], axis='columns')
```

### Step 26: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_columns_series, expected_columns_series)
```

### Step 27: Assign concatted_1_series = concat(...)

```python
concatted_1_series = concat([series1, series2], axis=1)
```

### Step 28: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(concatted_1_series, expected_columns_series)
```

### Step 29: Call concat()

```python
concat([series1, series2], axis='something')
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [0.1, 0.2]}, index=range(2))
df2 = DataFrame({'A': [0.3, 0.4]}, index=range(2))
expected_index = DataFrame({'A': [0.1, 0.2, 0.3, 0.4]}, index=[0, 1, 0, 1])
concatted_index = concat([df1, df2], axis='index')
tm.assert_frame_equal(concatted_index, expected_index)
concatted_row = concat([df1, df2], axis='rows')
tm.assert_frame_equal(concatted_row, expected_index)
concatted_0 = concat([df1, df2], axis=0)
tm.assert_frame_equal(concatted_0, expected_index)
expected_columns = DataFrame([[0.1, 0.3], [0.2, 0.4]], index=[0, 1], columns=['A', 'A'])
concatted_columns = concat([df1, df2], axis='columns')
tm.assert_frame_equal(concatted_columns, expected_columns)
concatted_1 = concat([df1, df2], axis=1)
tm.assert_frame_equal(concatted_1, expected_columns)
series1 = Series([0.1, 0.2])
series2 = Series([0.3, 0.4])
expected_index_series = Series([0.1, 0.2, 0.3, 0.4], index=[0, 1, 0, 1])
concatted_index_series = concat([series1, series2], axis='index')
tm.assert_series_equal(concatted_index_series, expected_index_series)
concatted_row_series = concat([series1, series2], axis='rows')
tm.assert_series_equal(concatted_row_series, expected_index_series)
concatted_0_series = concat([series1, series2], axis=0)
tm.assert_series_equal(concatted_0_series, expected_index_series)
expected_columns_series = DataFrame([[0.1, 0.3], [0.2, 0.4]], index=[0, 1], columns=[0, 1])
concatted_columns_series = concat([series1, series2], axis='columns')
tm.assert_frame_equal(concatted_columns_series, expected_columns_series)
concatted_1_series = concat([series1, series2], axis=1)
tm.assert_frame_equal(concatted_1_series, expected_columns_series)
with pytest.raises(ValueError, match='No axis named'):
    concat([series1, series2], axis='something')
```

## Next Steps


---

*Source: test_dataframe.py:73 | Complexity: Advanced | Last updated: 2026-06-02*