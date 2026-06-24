# How To: Agg Namedtuple

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test agg namedtuple

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': [0, 1], 'B': [1, 2]})
```

### Step 2: Assign result = df.agg(...)

```python
result = df.agg(foo=pd.NamedAgg('B', 'sum'), bar=pd.NamedAgg('B', 'min'), cat=pd.NamedAgg(column='B', aggfunc='count'), fft=pd.NamedAgg('B', aggfunc='max'))
```

### Step 3: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'B': [3, 1, 2, 2]}, index=pd.Index(['foo', 'bar', 'cat', 'fft']))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.agg(...)

```python
result = df.agg(foo=pd.NamedAgg('A', 'min'), bar=pd.NamedAgg(column='B', aggfunc='max'), cat=pd.NamedAgg(column='A', aggfunc='max'))
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': [0.0, np.nan, 1.0], 'B': [np.nan, 2.0, np.nan]}, index=pd.Index(['foo', 'bar', 'cat']))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': [0, 1], 'B': [1, 2]})
result = df.agg(foo=pd.NamedAgg('B', 'sum'), bar=pd.NamedAgg('B', 'min'), cat=pd.NamedAgg(column='B', aggfunc='count'), fft=pd.NamedAgg('B', aggfunc='max'))
expected = pd.DataFrame({'B': [3, 1, 2, 2]}, index=pd.Index(['foo', 'bar', 'cat', 'fft']))
tm.assert_frame_equal(result, expected)
result = df.agg(foo=pd.NamedAgg('A', 'min'), bar=pd.NamedAgg(column='B', aggfunc='max'), cat=pd.NamedAgg(column='A', aggfunc='max'))
expected = pd.DataFrame({'A': [0.0, np.nan, 1.0], 'B': [np.nan, 2.0, np.nan]}, index=pd.Index(['foo', 'bar', 'cat']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply_relabeling.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*