# How To: Edge Paths

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edge paths

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign edge_test1 = self.build_operands(...)

```python
edge_test1 = self.build_operands('eb,cb,fb->cef')
```

### Step 2: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test1, optimize='greedy')
```

### Step 3: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
```

### Step 4: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test1, optimize='optimal')
```

### Step 5: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
```

### Step 6: Assign edge_test2 = self.build_operands(...)

```python
edge_test2 = self.build_operands('dd,fb,be,cdb->cef')
```

### Step 7: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test2, optimize='greedy')
```

### Step 8: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
```

### Step 9: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test2, optimize='optimal')
```

### Step 10: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
```

### Step 11: Assign edge_test3 = self.build_operands(...)

```python
edge_test3 = self.build_operands('bca,cdb,dbf,afc->')
```

### Step 12: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test3, optimize='greedy')
```

### Step 13: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
```

### Step 14: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test3, optimize='optimal')
```

### Step 15: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
```

### Step 16: Assign edge_test4 = self.build_operands(...)

```python
edge_test4 = self.build_operands('dcc,fce,ea,dbf->ab')
```

### Step 17: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
```

### Step 18: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 1), (0, 1)])
```

### Step 19: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
```

### Step 20: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
```

### Step 21: Assign edge_test4 = self.build_operands(...)

```python
edge_test4 = self.build_operands('a,ac,ab,ad,cd,bd,bc->', size_dict={'a': 20, 'b': 20, 'c': 20, 'd': 20})
```

### Step 22: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
```

### Step 23: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
```

### Step 24: Assign unknown = np.einsum_path(...)

```python
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
```

### Step 25: Call self.assert_path_equal()

```python
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
```


## Complete Example

```python
# Workflow
edge_test1 = self.build_operands('eb,cb,fb->cef')
path, path_str = np.einsum_path(*edge_test1, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
path, path_str = np.einsum_path(*edge_test1, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 2), (0, 1)])
edge_test2 = self.build_operands('dd,fb,be,cdb->cef')
path, path_str = np.einsum_path(*edge_test2, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
path, path_str = np.einsum_path(*edge_test2, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 3), (0, 1), (0, 1)])
edge_test3 = self.build_operands('bca,cdb,dbf,afc->')
path, path_str = np.einsum_path(*edge_test3, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
path, path_str = np.einsum_path(*edge_test3, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
edge_test4 = self.build_operands('dcc,fce,ea,dbf->ab')
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 1), (0, 1)])
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (1, 2), (0, 2), (0, 1)])
edge_test4 = self.build_operands('a,ac,ab,ad,cd,bd,bc->', size_dict={'a': 20, 'b': 20, 'c': 20, 'd': 20})
path, path_str = np.einsum_path(*edge_test4, optimize='greedy')
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
path, path_str = np.einsum_path(*edge_test4, optimize='optimal')
self.assert_path_equal(path, ['einsum_path', (0, 1), (0, 1, 2, 3, 4, 5)])
```

## Next Steps


---

*Source: test_einsum.py:1219 | Complexity: Advanced | Last updated: 2026-06-02*