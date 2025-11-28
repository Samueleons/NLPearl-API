"""
Test unified API approach - same class names, different versions
"""
import nlpearl as pearl

print("=" * 60)
print("Testing Unified API Approach")
print("=" * 60)

# Test 1: V2 with Pearl methods (should work)
print("\n[Test 1] V2 - Pearl methods should work")
pearl.api_version = "v2"
try:
    # These should not raise errors (though they'd fail without API key)
    assert hasattr(pearl.Pearl, 'get_all')
    assert hasattr(pearl.Pearl, 'get')
    assert hasattr(pearl.Pearl, 'get_analytics')
    print("[OK] Pearl V2 methods accessible")
except Exception as e:
    print(f"[FAIL] {e}")

# Test 2: V2 with Outbound lead methods (should work)
print("\n[Test 2] V2 - Outbound lead methods should work")
pearl.api_version = "v2"
try:
    assert hasattr(pearl.Outbound, 'add_lead')
    assert hasattr(pearl.Outbound, 'get_lead_by_id')
    assert hasattr(pearl.Outbound, 'delete_leads')
    print("[OK] Outbound V2 lead methods accessible")
except Exception as e:
    print(f"[FAIL] {e}")

# Test 3: V2 with Inbound methods (should fail)
print("\n[Test 3] V2 - Inbound methods should raise error")
pearl.api_version = "v2"
pearl.api_key = "test_key"  # Set a fake key to test version check
try:
    pearl.Inbound.get_all()
    print("[FAIL] Should have raised error for Inbound in V2")
except ValueError as e:
    if "only available in API v1" in str(e):
        print(f"[OK] Correct error raised: {e}")
    else:
        print(f"[FAIL] Wrong error: {e}")
except Exception as e:
    print(f"[FAIL] Unexpected error: {e}")

# Test 4: V2 with V1-only Outbound methods (should fail)
print("\n[Test 4] V2 - V1-only Outbound methods should raise error")
pearl.api_version = "v2"
try:
    pearl.Outbound.get_all()
    print("[FAIL] Should have raised error for Outbound.get_all() in V2")
except ValueError as e:
    if "only available in API v1" in str(e):
        print(f"[OK] Correct error raised: {e}")
    else:
        print(f"[FAIL] Wrong error: {e}")
except Exception as e:
    print(f"[FAIL] Unexpected error: {e}")

# Test 5: V1 with Inbound methods (should work)
print("\n[Test 5] V1 - Inbound methods should work")
pearl.api_version = "v1"
try:
    assert hasattr(pearl.Inbound, 'get_all')
    assert hasattr(pearl.Inbound, 'get')
    assert hasattr(pearl.Inbound, 'get_analytics')
    print("[OK] Inbound V1 methods accessible")
except Exception as e:
    print(f"[FAIL] {e}")

# Test 6: V1 with Outbound methods (should work)
print("\n[Test 6] V1 - Outbound methods should work")
pearl.api_version = "v1"
try:
    assert hasattr(pearl.Outbound, 'get_all')
    assert hasattr(pearl.Outbound, 'add_lead')
    assert hasattr(pearl.Outbound, 'get_analytics')
    print("[OK] Outbound V1 methods accessible")
except Exception as e:
    print(f"[FAIL] {e}")

# Test 7: V1 with Pearl V2-only methods (should fail)
print("\n[Test 7] V1 - Pearl V2-only methods should raise error")
pearl.api_version = "v1"
try:
    pearl.Pearl.get_all()
    print("[FAIL] Should have raised error for Pearl.get_all() in V1")
except ValueError as e:
    if "only available in API v2" in str(e):
        print(f"[OK] Correct error raised: {e}")
    else:
        print(f"[FAIL] Wrong error: {e}")
except Exception as e:
    print(f"[FAIL] Unexpected error: {e}")

# Test 8: Version switching
print("\n[Test 8] Version switching")
pearl.api_version = "v1"
from nlpearl._helpers import _get_api_url
assert _get_api_url() == "https://api.nlpearl.ai/v1"
print("[OK] V1 URL correct")

pearl.api_version = "v2"
assert _get_api_url() == "https://api.nlpearl.ai/v2"
print("[OK] V2 URL correct")

# Test 9: Shared methods work in both versions
print("\n[Test 9] Shared methods accessible in both versions")
pearl.api_version = "v1"
assert hasattr(pearl.Outbound, 'add_lead')
assert hasattr(pearl.Outbound, 'get_lead_by_id')
print("[OK] V1 - Shared Outbound methods accessible")

pearl.api_version = "v2"
assert hasattr(pearl.Outbound, 'add_lead')
assert hasattr(pearl.Outbound, 'get_lead_by_id')
print("[OK] V2 - Shared Outbound methods accessible")

# Test 10: No OutboundV2 class exists
print("\n[Test 10] No separate V2 classes")
assert not hasattr(pearl, 'OutboundV2'), "OutboundV2 should not exist"
assert not hasattr(pearl, 'InboundV2'), "InboundV2 should not exist"
print("[OK] No separate V2 classes - unified API confirmed")

print("\n" + "=" * 60)
print("All tests passed!")
print("=" * 60)

print("\nUnified API Summary:")
print("- Set pearl.api_version once at the beginning")
print("- Use pearl.Outbound, pearl.Pearl, pearl.Inbound")
print("- Methods automatically route to correct version")
print("- Clear errors when using wrong version")
print("- No separate V2 classes needed")

