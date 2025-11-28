# NLPearl Unified API Implementation Summary

## Overview

Successfully implemented a **unified API approach** where the same class names work for both V1 and V2, with automatic routing based on `pearl.api_version`.

## Implementation Date

November 28, 2025

## What Changed

### Before (Separate Classes)
```python
pearl.api_version = "v2"
pearl.OutboundV2.add_lead(pearl_id, ...)  # Separate class
pearl.Pearl.get_all()
```

### After (Unified API)
```python
pearl.api_version = "v2"
pearl.Outbound.add_lead(pearl_id, ...)  # Same class name!
pearl.Pearl.get_all()
```

## Key Features

### ✅ Same Class Names
- Use `pearl.Outbound`, `pearl.Pearl`, `pearl.Inbound`
- **No** `pearl.OutboundV2` or separate V2 classes

### ✅ Automatic Routing
- Methods automatically route to correct endpoints based on `api_version`
- V1 and V2 share the same interface where applicable

### ✅ Clear Error Messages
When using a method in the wrong version:
```python
pearl.api_version = "v2"
pearl.Inbound.get_all()
# ValueError: Inbound.get_all() is only available in API v1.
# In v2, use Pearl.get_all() instead.
```

### ✅ Version Switching
```python
# Start with V2
pearl.api_version = "v2"
pearl.Pearl.get_all()

# Switch to V1 anytime
pearl.api_version = "v1"
pearl.Inbound.get_all()
```

## How It Works

### Version Checking

Each class has built-in version checking:

```python
class Outbound:
    @classmethod
    def _get_version(cls):
        """Get current API version."""
        return getattr(nlpearl, 'api_version', 'v2')
    
    @classmethod
    def _check_v1_only(cls, method_name):
        """Raise error if method is V1-only but V2 is selected."""
        if cls._get_version() == "v2":
            raise ValueError(f"{method_name}() is only available in API v1...")
```

### Automatic HTTP Method Selection

For methods that exist in both versions but use different HTTP verbs:

```python
@classmethod
def add_lead(cls, id_param, ...):
    version = cls._get_version()
    if version == "v1":
        response = requests.put(url, ...)  # V1 uses PUT
    else:  # v2
        response = requests.post(url, ...)  # V2 uses POST
    return response.json()
```

## Method Routing

| Method | V1 | V2 | Behavior |
|--------|----|----|----------|
| `Outbound.add_lead()` | ✅ | ✅ | Auto-routes, uses `outbound_id` in V1, `pearl_id` in V2 |
| `Outbound.get_all()` | ✅ | ❌ | Raises error in V2, suggests `Pearl.get_all()` |
| `Pearl.get_all()` | ❌ | ✅ | Raises error in V1 |
| `Inbound.get_all()` | ✅ | ❌ | Raises error in V2, suggests `Pearl.get_all()` |

## Usage Examples

### V2 Usage (Default)

```python
import nlpearl as pearl

pearl.api_key = "your_key"
pearl.api_version = "v2"  # Default

# Pearl operations
pearls = pearl.Pearl.get_all()
analytics = pearl.Pearl.get_analytics(pearl_id, from_date, to_date)

# Lead operations (same Outbound class!)
pearl.Outbound.add_lead(pearl_id, phone_number="+123...")
lead = pearl.Outbound.get_lead_by_id(pearl_id, lead_id)
```

### V1 Usage

```python
import nlpearl as pearl

pearl.api_key = "your_key"
pearl.api_version = "v1"

# Inbound/Outbound operations
inbounds = pearl.Inbound.get_all()
outbounds = pearl.Outbound.get_all()

# Lead operations (same Outbound class!)
pearl.Outbound.add_lead(outbound_id, phone_number="+123...")
lead = pearl.Outbound.get_lead_by_id(outbound_id, lead_id)
```

### Switching Versions

```python
# Start with V2
pearl.api_version = "v2"
pearls = pearl.Pearl.get_all()  # Works

# Switch to V1
pearl.api_version = "v1"
inbounds = pearl.Inbound.get_all()  # Works
pearls = pearl.Pearl.get_all()  # Raises clear error

# Switch back to V2
pearl.api_version = "v2"
```

## Files Modified

### Core Implementation
- `nlpearl/__init__.py` - Removed OutboundV2 export
- `nlpearl/outbound.py` - Added version routing logic
- `nlpearl/inbound.py` - Added version checks
- `nlpearl/pearl.py` - Added version checks for V2 methods

### Files Deleted
- `nlpearl/outbound_v2.py` - No longer needed!

### Documentation
- `README.md` - Complete rewrite for unified API
- `example_unified_api.py` - New unified examples
- `test_unified_api.py` - Comprehensive unified API tests

## Testing

### All Tests Pass ✅

1. **Version Selection Test** (`test_version.py`)
   - Default V2 ✅
   - Switch to V1 ✅
   - Switch back to V2 ✅
   - Custom versions ✅

2. **Unified API Test** (`test_unified_api.py`)
   - V2 Pearl methods work ✅
   - V2 Outbound methods work ✅
   - V2 with Inbound raises error ✅
   - V1 Inbound methods work ✅
   - V1 Outbound methods work ✅
   - V1 with Pearl V2 raises error ✅
   - No separate V2 classes ✅

## Benefits

### For Users

1. **Simpler API**
   - One class name regardless of version
   - Less confusion about which class to use

2. **Easy Migration**
   - Change one line: `pearl.api_version = "v2"`
   - Update ID parameters: `outbound_id` → `pearl_id`
   - Same method names where possible

3. **Clear Guidance**
   - Error messages tell you exactly what to do
   - Suggests alternative methods in other versions

### For Maintainers

1. **Single Source of Truth**
   - One `Outbound` class instead of two
   - Easier to maintain and update

2. **Consistent Interface**
   - Same patterns across all classes
   - Version checks in one place

3. **Type Safety**
   - Methods fail fast with clear errors
   - No silent failures or wrong endpoints

## Migration from Previous Implementation

If you were using the previous implementation with `OutboundV2`:

**Before:**
```python
pearl.api_version = "v2"
pearl.OutboundV2.add_lead(pearl_id, ...)
```

**After:**
```python
pearl.api_version = "v2"
pearl.Outbound.add_lead(pearl_id, ...)  # Just use Outbound!
```

## Summary

✅ **Unified API** - Same class names for V1 and V2  
✅ **Automatic Routing** - Methods route based on `api_version`  
✅ **Clear Errors** - Helpful messages when using wrong version  
✅ **No Separate Classes** - No `OutboundV2`, `InboundV2`, etc.  
✅ **Easy Migration** - Change version, update IDs, done!  
✅ **Fully Tested** - All tests pass  
✅ **Complete Documentation** - README, examples, tests  

## Conclusion

The unified API approach provides:
- **Simpler** - One interface, less to remember
- **Clearer** - Obvious errors guide you
- **Flexible** - Easy version switching
- **Maintainable** - Single codebase

Perfect for what you requested! 🎉

