# How To: Sort Values Nat Values In Int Column

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values nat values in int column

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign int_values = value

```python
int_values = (2, int(NaT._value))
```

### Step 2: Assign float_values = value

```python
float_values = (2.0, -1.797693e+308)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'int': int_values, 'float': float_values}, columns=['int', 'float'])
```

### Step 4: Assign df_reversed = DataFrame(...)

```python
df_reversed = DataFrame({'int': int_values[::-1], 'float': float_values[::-1]}, columns=['int', 'float'], index=[1, 0])
```

### Step 5: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['int', 'float'], na_position='last')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df_reversed)
```

### Step 7: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['int', 'float'], na_position='first')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df_reversed)
```

### Step 9: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['int', 'float'], ascending=False)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df)
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame({'datetime': [Timestamp('2016-01-01'), NaT], 'float': float_values}, columns=['datetime', 'float'])
```

### Step 12: Assign df_reversed = DataFrame(...)

```python
df_reversed = DataFrame({'datetime': [NaT, Timestamp('2016-01-01')], 'float': float_values[::-1]}, columns=['datetime', 'float'], index=[1, 0])
```

### Step 13: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['datetime', 'float'], na_position='first')
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df_reversed)
```

### Step 15: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['datetime', 'float'], na_position='last')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df)
```

### Step 17: Assign df_sorted = df.sort_values(...)

```python
df_sorted = df.sort_values(['datetime', 'float'], ascending=False)
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_sorted, df)
```


## Complete Example

```python
# Workflow
int_values = (2, int(NaT._value))
float_values = (2.0, -1.797693e+308)
df = DataFrame({'int': int_values, 'float': float_values}, columns=['int', 'float'])
df_reversed = DataFrame({'int': int_values[::-1], 'float': float_values[::-1]}, columns=['int', 'float'], index=[1, 0])
df_sorted = df.sort_values(['int', 'float'], na_position='last')
tm.assert_frame_equal(df_sorted, df_reversed)
df_sorted = df.sort_values(['int', 'float'], na_position='first')
tm.assert_frame_equal(df_sorted, df_reversed)
df_sorted = df.sort_values(['int', 'float'], ascending=False)
tm.assert_frame_equal(df_sorted, df)
df = DataFrame({'datetime': [Timestamp('2016-01-01'), NaT], 'float': float_values}, columns=['datetime', 'float'])
df_reversed = DataFrame({'datetime': [NaT, Timestamp('2016-01-01')], 'float': float_values[::-1]}, columns=['datetime', 'float'], index=[1, 0])
df_sorted = df.sort_values(['datetime', 'float'], na_position='first')
tm.assert_frame_equal(df_sorted, df_reversed)
df_sorted = df.sort_values(['datetime', 'float'], na_position='last')
tm.assert_frame_equal(df_sorted, df)
df_sorted = df.sort_values(['datetime', 'float'], ascending=False)
tm.assert_frame_equal(df_sorted, df)
```

## Next Steps


---

*Source: test_sort_values.py:353 | Complexity: Advanced | Last updated: 2026-06-02*