# How To: Memory Contraints

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memory contraints

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign outer_test = self.build_operands(...)

```python
outer_test = self.build_operands('a,b,c->abc')
```

### Step 2: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*outer_test, optimize=('greedy', 0))
```

### Step 3: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
```

### Step 4: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*outer_test, optimize=('optimal', 0))
```

### Step 5: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
```

### Step 6: Assign long_test = self.build_operands(...)

```python
long_test = self.build_operands('acdf,jbje,gihb,hfac')
```

### Step 7: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test, optimize=('greedy', 0))
```

### Step 8: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
```

### Step 9: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test, optimize=('optimal', 0))
```

### Step 10: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
```


## Complete Example

```python
# Workflow
outer_test = self.build_operands('a,b,c->abc')
path, path_str = np.einsum_path(*outer_test, optimize=('greedy', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
path, path_str = np.einsum_path(*outer_test, optimize=('optimal', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2)])
long_test = self.build_operands('acdf,jbje,gihb,hfac')
path, path_str = np.einsum_path(*long_test, optimize=('greedy', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
path, path_str = np.einsum_path(*long_test, optimize=('optimal', 0))
self.assert_path_equal(path, ['einsum_path', (0, 1, 2, 3)])
```

## Next Steps


---

*Source: test_einsum.py:1178 | Complexity: Advanced | Last updated: 2026-06-02*