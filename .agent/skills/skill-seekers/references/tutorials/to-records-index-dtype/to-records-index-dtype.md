# How To: To Records Index Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records index dtype

## Prerequisites

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({1: date_range('2022-01-01', periods=2), 2: date_range('2022-01-01', periods=2), 3: date_range('2022-01-01', periods=2)})
```

### Step 2: Assign expected = np.rec.array(...)

```python
expected = np.rec.array([('2022-01-01', '2022-01-01', '2022-01-01'), ('2022-01-02', '2022-01-02', '2022-01-02')], dtype=[('1', f'{tm.ENDIAN}M8[ns]'), ('2', f'{tm.ENDIAN}M8[ns]'), ('3', f'{tm.ENDIAN}M8[ns]')])
```

### Step 3: Assign result = df.to_records(...)

```python
result = df.to_records(index=False)
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 5: Assign result = df.set_index.to_records(...)

```python
result = df.set_index(1).to_records(index=True)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Assign result = df.set_index.to_records(...)

```python
result = df.set_index([1, 2]).to_records(index=True)
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({1: date_range('2022-01-01', periods=2), 2: date_range('2022-01-01', periods=2), 3: date_range('2022-01-01', periods=2)})
expected = np.rec.array([('2022-01-01', '2022-01-01', '2022-01-01'), ('2022-01-02', '2022-01-02', '2022-01-02')], dtype=[('1', f'{tm.ENDIAN}M8[ns]'), ('2', f'{tm.ENDIAN}M8[ns]'), ('3', f'{tm.ENDIAN}M8[ns]')])
result = df.to_records(index=False)
tm.assert_almost_equal(result, expected)
result = df.set_index(1).to_records(index=True)
tm.assert_almost_equal(result, expected)
result = df.set_index([1, 2]).to_records(index=True)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_to_records.py:120 | Complexity: Advanced | Last updated: 2026-06-02*