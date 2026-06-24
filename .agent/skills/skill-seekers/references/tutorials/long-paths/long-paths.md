# How To: Long Paths

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test long paths

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign long_test1 = self.build_operands(...)

```python
long_test1 = self.build_operands('acdf,jbje,gihb,hfac,gfac,gifabc,hfac')
```

### Step 2: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test1, optimize='greedy')
```

### Step 3: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
```

### Step 4: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test1, optimize='optimal')
```

### Step 5: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
```

### Step 6: Assign long_test2 = self.build_operands(...)

```python
long_test2 = self.build_operands('chd,bde,agbc,hiad,bdi,cgh,agdb')
```

### Step 7: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test2, optimize='greedy')
```

### Step 8: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (3, 4), (0, 3), (3, 4), (1, 3), (1, 2), (0, 1)])
```

### Step 9: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*long_test2, optimize='optimal')
```

### Step 10: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 5), (1, 4), (3, 4), (1, 3), (1, 2), (0, 1)])
```


## Complete Example

```python
# Workflow
long_test1 = self.build_operands('acdf,jbje,gihb,hfac,gfac,gifabc,hfac')
path, path_str = np.einsum_path(*long_test1, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
path, path_str = np.einsum_path(*long_test1, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (3, 6), (3, 4), (2, 4), (2, 3), (0, 2), (0, 1)])
long_test2 = self.build_operands('chd,bde,agbc,hiad,bdi,cgh,agdb')
path, path_str = np.einsum_path(*long_test2, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (3, 4), (0, 3), (3, 4), (1, 3), (1, 2), (0, 1)])
path, path_str = np.einsum_path(*long_test2, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 5), (1, 4), (3, 4), (1, 3), (1, 2), (0, 1)])
```

## Next Steps


---

*Source: test_einsum.py:1196 | Complexity: Advanced | Last updated: 2026-06-02*