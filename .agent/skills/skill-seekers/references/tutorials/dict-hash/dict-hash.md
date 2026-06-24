# How To: Dict Hash

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dict hash

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `gc`
- `hashlib`
- `io`
- `itertools`
- `pickle`
- `random`
- `sys`
- `time`
- `concurrent.futures`
- `decimal`
- `joblib.func_inspect`
- `joblib.hashing`
- `joblib.memory`
- `joblib.test.common`
- `joblib.testing`

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign k = KlassWithCachedMethod(...)

```python
k = KlassWithCachedMethod(tmpdir.strpath)
```

**Verification:**
```python
assert hash(a) == hash(b)
```

### Step 2: Assign d = value

```python
d = {'#s12069__c_maps.nii.gz': [33], '#s12158__c_maps.nii.gz': [33], '#s12258__c_maps.nii.gz': [33], '#s12277__c_maps.nii.gz': [33], '#s12300__c_maps.nii.gz': [33], '#s12401__c_maps.nii.gz': [33], '#s12430__c_maps.nii.gz': [33], '#s13817__c_maps.nii.gz': [33], '#s13903__c_maps.nii.gz': [33], '#s13916__c_maps.nii.gz': [33], '#s13981__c_maps.nii.gz': [33], '#s13982__c_maps.nii.gz': [33], '#s13983__c_maps.nii.gz': [33]}
```

### Step 3: Assign a = k.f(...)

```python
a = k.f(d)
```

### Step 4: Assign b = k.f(...)

```python
b = k.f(a)
```

**Verification:**
```python
assert hash(a) == hash(b)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
k = KlassWithCachedMethod(tmpdir.strpath)
d = {'#s12069__c_maps.nii.gz': [33], '#s12158__c_maps.nii.gz': [33], '#s12258__c_maps.nii.gz': [33], '#s12277__c_maps.nii.gz': [33], '#s12300__c_maps.nii.gz': [33], '#s12401__c_maps.nii.gz': [33], '#s12430__c_maps.nii.gz': [33], '#s13817__c_maps.nii.gz': [33], '#s13903__c_maps.nii.gz': [33], '#s13916__c_maps.nii.gz': [33], '#s13981__c_maps.nii.gz': [33], '#s13982__c_maps.nii.gz': [33], '#s13983__c_maps.nii.gz': [33]}
a = k.f(d)
b = k.f(a)
assert hash(a) == hash(b)
```

## Next Steps


---

*Source: test_hashing.py:280 | Complexity: Intermediate | Last updated: 2026-06-02*