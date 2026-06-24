# How To: Exotic Weights

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exotic weights

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([1.3, 2.5, 2.3])
```

**Verification:**
```python
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
```

### Step 2: Assign weights = value

```python
weights = np.array([1, -1, 2]) + 1j * np.array([2, 1, 2])
```

**Verification:**
```python
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
```

### Step 3: Assign unknown = histogram(...)

```python
wa, wb = histogram(values, bins=[0, 2, 3], weights=weights)
```

**Verification:**
```python
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
```

### Step 4: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
```

**Verification:**
```python
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
```

### Step 5: Assign unknown = histogram(...)

```python
wa, wb = histogram(values, bins=2, range=[1, 3], weights=weights)
```

### Step 6: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
```

### Step 7: Assign values = np.array(...)

```python
values = np.array([1.3, 2.5, 2.3])
```

### Step 8: Assign weights = np.array(...)

```python
weights = np.array([Decimal(1), Decimal(2), Decimal(3)])
```

### Step 9: Assign unknown = histogram(...)

```python
wa, wb = histogram(values, bins=[0, 2, 3], weights=weights)
```

### Step 10: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
```

### Step 11: Assign unknown = histogram(...)

```python
wa, wb = histogram(values, bins=2, range=[1, 3], weights=weights)
```

### Step 12: Call assert_array_almost_equal()

```python
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
```


## Complete Example

```python
# Workflow
values = np.array([1.3, 2.5, 2.3])
weights = np.array([1, -1, 2]) + 1j * np.array([2, 1, 2])
wa, wb = histogram(values, bins=[0, 2, 3], weights=weights)
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
wa, wb = histogram(values, bins=2, range=[1, 3], weights=weights)
assert_array_almost_equal(wa, np.array([1, 1]) + 1j * np.array([2, 3]))
from decimal import Decimal
values = np.array([1.3, 2.5, 2.3])
weights = np.array([Decimal(1), Decimal(2), Decimal(3)])
wa, wb = histogram(values, bins=[0, 2, 3], weights=weights)
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
wa, wb = histogram(values, bins=2, range=[1, 3], weights=weights)
assert_array_almost_equal(wa, [Decimal(1), Decimal(5)])
```

## Next Steps


---

*Source: test_histograms.py:177 | Complexity: Advanced | Last updated: 2026-06-02*