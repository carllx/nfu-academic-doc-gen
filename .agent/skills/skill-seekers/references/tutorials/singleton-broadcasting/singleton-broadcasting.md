# How To: Singleton Broadcasting

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test singleton broadcasting

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign eq = 'ijp,ipq,ikq->ijk'

```python
eq = 'ijp,ipq,ikq->ijk'
```

### Step 2: Assign shapes = value

```python
shapes = ((3, 1, 1), (3, 1, 3), (1, 3, 3))
```

### Step 3: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 4: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```

### Step 5: Assign eq = 'jhcabhijaci,dfijejgh->fgje'

```python
eq = 'jhcabhijaci,dfijejgh->fgje'
```

### Step 6: Assign shapes = value

```python
shapes = ((1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1), (3, 1, 3, 1, 1, 1, 1, 2))
```

### Step 7: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 8: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```

### Step 9: Assign eq = 'baegffahgc,hdggeff->dhg'

```python
eq = 'baegffahgc,hdggeff->dhg'
```

### Step 10: Assign shapes = value

```python
shapes = ((2, 1, 4, 1, 1, 1, 1, 2, 1, 1), (1, 1, 1, 1, 4, 1, 1))
```

### Step 11: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 12: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```

### Step 13: Assign eq = 'cehgbaifff,fhhdegih->cdghbi'

```python
eq = 'cehgbaifff,fhhdegih->cdghbi'
```

### Step 14: Assign shapes = value

```python
shapes = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 1, 1, 2, 4, 1, 1, 1))
```

### Step 15: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 16: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```

### Step 17: Assign eq = 'gah,cdbcghefg->ef'

```python
eq = 'gah,cdbcghefg->ef'
```

### Step 18: Assign shapes = value

```python
shapes = ((2, 3, 1), (1, 3, 1, 1, 1, 2, 1, 4, 1))
```

### Step 19: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 20: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```

### Step 21: Assign eq = 'cacc,bcb->'

```python
eq = 'cacc,bcb->'
```

### Step 22: Assign shapes = value

```python
shapes = ((1, 1, 1, 1), (1, 4, 1))
```

### Step 23: Assign arrays = value

```python
arrays = [np.random.rand(*shape) for shape in shapes]
```

### Step 24: Call self.optimize_compare()

```python
self.optimize_compare(eq, operands=arrays)
```


## Complete Example

```python
# Workflow
eq = 'ijp,ipq,ikq->ijk'
shapes = ((3, 1, 1), (3, 1, 3), (1, 3, 3))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'jhcabhijaci,dfijejgh->fgje'
shapes = ((1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1), (3, 1, 3, 1, 1, 1, 1, 2))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'baegffahgc,hdggeff->dhg'
shapes = ((2, 1, 4, 1, 1, 1, 1, 2, 1, 1), (1, 1, 1, 1, 4, 1, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'cehgbaifff,fhhdegih->cdghbi'
shapes = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 1, 1, 2, 4, 1, 1, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'gah,cdbcghefg->ef'
shapes = ((2, 3, 1), (1, 3, 1, 1, 1, 2, 1, 4, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
eq = 'cacc,bcb->'
shapes = ((1, 1, 1, 1), (1, 4, 1))
arrays = [np.random.rand(*shape) for shape in shapes]
self.optimize_compare(eq, operands=arrays)
```

## Next Steps


---

*Source: test_einsum.py:1122 | Complexity: Advanced | Last updated: 2026-06-02*