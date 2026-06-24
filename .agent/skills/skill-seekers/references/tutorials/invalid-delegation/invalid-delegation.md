# How To: Invalid Delegation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invalid delegation

## Prerequisites

**Required Modules:**
- `datetime`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.accessor`
- `pandas.core.base`


## Step-by-Step Guide

### Step 1: Call self.Delegate._add_delegate_accessors()

```python
self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._properties, typ='property')
```

### Step 2: Call self.Delegate._add_delegate_accessors()

```python
self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._methods, typ='method')
```

### Step 3: Assign delegate = self.Delegate(...)

```python
delegate = self.Delegate(self.Delegator())
```

### Step 4: Assign msg = 'You cannot access the property prop'

```python
msg = 'You cannot access the property prop'
```

### Step 5: Assign msg = 'The property prop cannot be set'

```python
msg = 'The property prop cannot be set'
```

### Step 6: Assign msg = 'You cannot access the property prop'

```python
msg = 'You cannot access the property prop'
```

### Step 7: delegate.prop

```python
delegate.prop
```

### Step 8: Assign delegate.prop = 5

```python
delegate.prop = 5
```

### Step 9: delegate.prop

```python
delegate.prop
```


## Complete Example

```python
# Workflow
self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._properties, typ='property')
self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._methods, typ='method')
delegate = self.Delegate(self.Delegator())
msg = 'You cannot access the property prop'
with pytest.raises(TypeError, match=msg):
    delegate.prop
msg = 'The property prop cannot be set'
with pytest.raises(TypeError, match=msg):
    delegate.prop = 5
msg = 'You cannot access the property prop'
with pytest.raises(TypeError, match=msg):
    delegate.prop
```

## Next Steps


---

*Source: test_constructors.py:64 | Complexity: Advanced | Last updated: 2026-06-02*