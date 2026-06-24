# How To: Einsum Sorting Behavior

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test einsum sorting behavior

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign n1 = 26

```python
n1 = 26
```

**Verification:**
```python
assert all((c.isupper() for c in output_indices1)), f'Output indices for n=26 should use uppercase letters only: {output_indices1}'
```

### Step 2: Assign x1 = np.random.random(...)

```python
x1 = np.random.random((1,) * n1)
```

**Verification:**
```python
assert_equal(output_indices1, ''.join(sorted(output_indices1)), err_msg=f'Output indices for n=26 are not lexicographically sorted: {output_indices1}')
```

### Step 3: Assign path1 = value

```python
path1 = np.einsum_path(x1, range(n1))[1]
```

**Verification:**
```python
assert any((c.islower() for c in output_indices2)), f'Output indices for n=27 should include uppercase letters: {output_indices2}'
```

### Step 4: Assign output_indices1 = unknown.strip(...)

```python
output_indices1 = path1.split('->')[-1].strip()
```

**Verification:**
```python
assert_equal(output_indices2, ''.join(sorted(output_indices2)), err_msg=f'Output indices for n=27 are not lexicographically sorted: {output_indices2}')
```

### Step 5: Call assert_equal()

```python
assert_equal(output_indices1, ''.join(sorted(output_indices1)), err_msg=f'Output indices for n=26 are not lexicographically sorted: {output_indices1}')
```

**Verification:**
```python
assert_equal(output_indices2, ''.join(expected_indices), err_msg=f"Output indices do not map to the correct dimensions. Expected: {''.join(expected_indices)}, Got: {output_indices2}")
```

### Step 6: Assign n2 = 27

```python
n2 = 27
```

### Step 7: Assign x2 = np.random.random(...)

```python
x2 = np.random.random((1,) * n2)
```

### Step 8: Assign path2 = value

```python
path2 = np.einsum_path(x2, range(n2))[1]
```

### Step 9: Assign output_indices2 = unknown.strip(...)

```python
output_indices2 = path2.split('->')[-1].strip()
```

**Verification:**
```python
assert any((c.islower() for c in output_indices2)), f'Output indices for n=27 should include uppercase letters: {output_indices2}'
```

### Step 10: Call assert_equal()

```python
assert_equal(output_indices2, ''.join(sorted(output_indices2)), err_msg=f'Output indices for n=27 are not lexicographically sorted: {output_indices2}')
```

### Step 11: Assign expected_indices = value

```python
expected_indices = [chr(i + ord('A')) if i < 26 else chr(i - 26 + ord('a')) for i in range(n2)]
```

### Step 12: Call assert_equal()

```python
assert_equal(output_indices2, ''.join(expected_indices), err_msg=f"Output indices do not map to the correct dimensions. Expected: {''.join(expected_indices)}, Got: {output_indices2}")
```


## Complete Example

```python
# Workflow
n1 = 26
x1 = np.random.random((1,) * n1)
path1 = np.einsum_path(x1, range(n1))[1]
output_indices1 = path1.split('->')[-1].strip()
assert all((c.isupper() for c in output_indices1)), f'Output indices for n=26 should use uppercase letters only: {output_indices1}'
assert_equal(output_indices1, ''.join(sorted(output_indices1)), err_msg=f'Output indices for n=26 are not lexicographically sorted: {output_indices1}')
n2 = 27
x2 = np.random.random((1,) * n2)
path2 = np.einsum_path(x2, range(n2))[1]
output_indices2 = path2.split('->')[-1].strip()
assert any((c.islower() for c in output_indices2)), f'Output indices for n=27 should include uppercase letters: {output_indices2}'
assert_equal(output_indices2, ''.join(sorted(output_indices2)), err_msg=f'Output indices for n=27 are not lexicographically sorted: {output_indices2}')
expected_indices = [chr(i + ord('A')) if i < 26 else chr(i - 26 + ord('a')) for i in range(n2)]
assert_equal(output_indices2, ''.join(expected_indices), err_msg=f"Output indices do not map to the correct dimensions. Expected: {''.join(expected_indices)}, Got: {output_indices2}")
```

## Next Steps


---

*Source: test_einsum.py:87 | Complexity: Advanced | Last updated: 2026-06-02*