# How To: Unity Not Misidentified As Unreal With Source Dir

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Unity project with a 'Source' subfolder must NOT be identified as Unreal (Issue #365).

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `pathlib`
- `pytest`
- `skill_seekers.cli.architectural_pattern_detector`
- `skill_seekers.cli.architectural_pattern_detector`
- `skill_seekers.cli.architectural_pattern_detector`

**Setup Required:**
```python
# Fixtures: detector, tmp_path
```

## Step-by-Step Guide

### Step 1: "Unity project with a 'Source' subfolder must NOT be identified as Unreal (Issue #365)."

```python
"Unity project with a 'Source' subfolder must NOT be identified as Unreal (Issue #365)."
```

**Verification:**
```python
assert 'Unity' in frameworks, f'Expected Unity, got {frameworks}'
```

### Step 2: Assign root = str(...)

```python
root = str(tmp_path)
```

**Verification:**
```python
assert 'Unreal' not in frameworks, f'Unreal falsely detected: {frameworks}'
```

### Step 3: Call _make_unity_dir()

```python
_make_unity_dir(tmp_path)
```

### Step 4: Assign source_dir = value

```python
source_dir = tmp_path / 'Assets' / 'Scripts' / 'Source'
```

### Step 5: Call source_dir.mkdir()

```python
source_dir.mkdir(parents=True)
```

### Step 6: Assign files = _unity_files(...)

```python
files = _unity_files(root)
```

### Step 7: Call files.append()

```python
files.append({'file': f'{root}/Assets/Scripts/Source/Utilities.cs', 'language': 'C#', 'imports': ['UnityEngine', 'System']})
```

### Step 8: Assign frameworks = detector._detect_frameworks(...)

```python
frameworks = detector._detect_frameworks(tmp_path, files)
```

**Verification:**
```python
assert 'Unity' in frameworks, f'Expected Unity, got {frameworks}'
```


## Complete Example

```python
# Setup
# Fixtures: detector, tmp_path

# Workflow
"Unity project with a 'Source' subfolder must NOT be identified as Unreal (Issue #365)."
root = str(tmp_path)
_make_unity_dir(tmp_path)
source_dir = tmp_path / 'Assets' / 'Scripts' / 'Source'
source_dir.mkdir(parents=True)
files = _unity_files(root)
files.append({'file': f'{root}/Assets/Scripts/Source/Utilities.cs', 'language': 'C#', 'imports': ['UnityEngine', 'System']})
frameworks = detector._detect_frameworks(tmp_path, files)
assert 'Unity' in frameworks, f'Expected Unity, got {frameworks}'
assert 'Unreal' not in frameworks, f'Unreal falsely detected: {frameworks}'
```

## Next Steps


---

*Source: test_architectural_pattern_detector.py:73 | Complexity: Advanced | Last updated: 2026-06-02*