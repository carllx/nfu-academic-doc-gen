# How To: Corr Rank

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corr rank

## Prerequisites

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign stats = pytest.importorskip(...)

```python
stats = pytest.importorskip('scipy.stats')
```

### Step 2: Assign A = Series(...)

```python
A = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
```

### Step 3: Assign B = A.copy(...)

```python
B = A.copy()
```

### Step 4: Assign unknown = unknown.copy(...)

```python
A[-5:] = A[:5].copy()
```

### Step 5: Assign result = A.corr(...)

```python
result = A.corr(B, method='kendall')
```

### Step 6: Assign expected = value

```python
expected = stats.kendalltau(A, B)[0]
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 8: Assign result = A.corr(...)

```python
result = A.corr(B, method='spearman')
```

### Step 9: Assign expected = value

```python
expected = stats.spearmanr(A, B)[0]
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 11: Assign A = Series(...)

```python
A = Series([-0.89926396, 0.94209606, -1.03289164, -0.95445587, 0.7691031, -0.06430576, -2.09704447, 0.40660407, -0.89926396, 0.94209606])
```

### Step 12: Assign B = Series(...)

```python
B = Series([-1.01270225, -0.62210117, -1.56895827, 0.59592943, -0.01680292, 1.17258718, -1.06009347, -0.1022206, -0.89076239, 0.89372375])
```

### Step 13: Assign kexp = 0.4319297

```python
kexp = 0.4319297
```

### Step 14: Assign sexp = 0.5853767

```python
sexp = 0.5853767
```

### Step 15: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(A.corr(B, method='kendall'), kexp)
```

### Step 16: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(A.corr(B, method='spearman'), sexp)
```


## Complete Example

```python
# Workflow
stats = pytest.importorskip('scipy.stats')
A = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
B = A.copy()
A[-5:] = A[:5].copy()
result = A.corr(B, method='kendall')
expected = stats.kendalltau(A, B)[0]
tm.assert_almost_equal(result, expected)
result = A.corr(B, method='spearman')
expected = stats.spearmanr(A, B)[0]
tm.assert_almost_equal(result, expected)
A = Series([-0.89926396, 0.94209606, -1.03289164, -0.95445587, 0.7691031, -0.06430576, -2.09704447, 0.40660407, -0.89926396, 0.94209606])
B = Series([-1.01270225, -0.62210117, -1.56895827, 0.59592943, -0.01680292, 1.17258718, -1.06009347, -0.1022206, -0.89076239, 0.89372375])
kexp = 0.4319297
sexp = 0.5853767
tm.assert_almost_equal(A.corr(B, method='kendall'), kexp)
tm.assert_almost_equal(A.corr(B, method='spearman'), sexp)
```

## Next Steps


---

*Source: test_cov_corr.py:95 | Complexity: Advanced | Last updated: 2026-06-02*