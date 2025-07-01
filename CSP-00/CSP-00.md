# CSP-00: Directory Layout Convention

**Status**: Proposed  
**Review Window**: 7 days after publication

## Summary
We need a standard layout for snippets and metadata. Two options:

### Option A: Slug-first
```
snippets/
└── structured-logger/
    ├─ CSP-00.md
    ├─ metadata.yaml
    ├─ structured_logger.py
    ├─ tests/
    └─ README.md
```

### Option B: CSP-first
```
CSP-00/
├─ metadata.yaml
├─ code.py
├─ tests/
└─ README.md
```

## Evaluation
Option A maps to real-world tool names; Option B allows simpler versioning per CSP.

### Vote
👍 Option A — slug-first  
👎 Option B — CSP-number-first
