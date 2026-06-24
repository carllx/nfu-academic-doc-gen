# How To: All Modules Are Expected 2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Method checking all objects. The pkgutil-based method in
`test_all_modules_are_expected` does not catch imports into a namespace,
only filenames.  So this test is more thorough, and checks this like:

    import .lib.scimath as emath

To check if something in a module is (effectively) public, one can check if
there's anything in that namespace that's a public function/object but is
not exposed in a higher-level namespace.  For example for a `numpy.lib`
submodule::

    mod = np.lib.mixins
    for obj in mod.__all__:
        if obj in np.__all__:
            continue
        elif obj in np.lib.__all__:
            continue

        else:
            print(obj)

## Prerequisites

**Required Modules:**
- `functools`
- `importlib`
- `inspect`
- `pkgutil`
- `subprocess`
- `sys`
- `sysconfig`
- `types`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `ctypes`
- `numpy.core`
- `collections.abc`
- `typing`
- `numpy._core._multiarray_umath`


## Step-by-Step Guide

### Step 1: "\n    Method checking all objects. The pkgutil-based method in\n    `test_all_modules_are_expected` does not catch imports into a namespace,\n    only filenames.  So this test is more thorough, and checks this like:\n\n        import .lib.scimath as emath\n\n    To check if something in a module is (effectively) public, one can check if\n    there's anything in that namespace that's a public function/object but is\n    not exposed in a higher-level namespace.  For example for a `numpy.lib`\n    submodule::\n\n        mod = np.lib.mixins\n        for obj in mod.__all__:\n            if obj in np.__all__:\n                continue\n            elif obj in np.lib.__all__:\n                continue\n\n            else:\n                print(obj)\n\n    "

```python
"\n    Method checking all objects. The pkgutil-based method in\n    `test_all_modules_are_expected` does not catch imports into a namespace,\n    only filenames.  So this test is more thorough, and checks this like:\n\n        import .lib.scimath as emath\n\n    To check if something in a module is (effectively) public, one can check if\n    there's anything in that namespace that's a public function/object but is\n    not exposed in a higher-level namespace.  For example for a `numpy.lib`\n    submodule::\n\n        mod = np.lib.mixins\n        for obj in mod.__all__:\n            if obj in np.__all__:\n                continue\n            elif obj in np.lib.__all__:\n                continue\n\n            else:\n                print(obj)\n\n    "
```

### Step 2: Assign unexpected_members = find_unexpected_members(...)

```python
unexpected_members = find_unexpected_members('numpy')
```

### Step 3: Assign members = value

```python
members = []
```

### Step 4: Assign module = importlib.import_module(...)

```python
module = importlib.import_module(mod_name)
```

### Step 5: Call unexpected_members.extend()

```python
unexpected_members.extend(find_unexpected_members(modname))
```

### Step 6: Assign objnames = value

```python
objnames = module.__all__
```

### Step 7: Assign objnames = dir(...)

```python
objnames = dir(module)
```

### Step 8: Assign fullobjname = value

```python
fullobjname = mod_name + '.' + objname
```

### Step 9: Call members.append()

```python
members.append(fullobjname)
```


## Complete Example

```python
# Workflow
"\n    Method checking all objects. The pkgutil-based method in\n    `test_all_modules_are_expected` does not catch imports into a namespace,\n    only filenames.  So this test is more thorough, and checks this like:\n\n        import .lib.scimath as emath\n\n    To check if something in a module is (effectively) public, one can check if\n    there's anything in that namespace that's a public function/object but is\n    not exposed in a higher-level namespace.  For example for a `numpy.lib`\n    submodule::\n\n        mod = np.lib.mixins\n        for obj in mod.__all__:\n            if obj in np.__all__:\n                continue\n            elif obj in np.lib.__all__:\n                continue\n\n            else:\n                print(obj)\n\n    "

def find_unexpected_members(mod_name):
    members = []
    module = importlib.import_module(mod_name)
    if hasattr(module, '__all__'):
        objnames = module.__all__
    else:
        objnames = dir(module)
    for objname in objnames:
        if not objname.startswith('_'):
            fullobjname = mod_name + '.' + objname
            if isinstance(getattr(module, objname), types.ModuleType):
                if is_unexpected(fullobjname):
                    if fullobjname not in SKIP_LIST_2:
                        members.append(fullobjname)
    return members
unexpected_members = find_unexpected_members('numpy')
for modname in PUBLIC_MODULES:
    unexpected_members.extend(find_unexpected_members(modname))
if unexpected_members:
    raise AssertionError(f'Found unexpected object(s) that look like modules: {unexpected_members}')
```

## Next Steps


---

*Source: test_public_api.py:326 | Complexity: Advanced | Last updated: 2026-06-02*