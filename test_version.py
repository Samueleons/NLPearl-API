"""
Test pour vérifier le système de sélection de version de l'API
"""
import nlpearl as pearl
from nlpearl._helpers import _get_api_url

print("=== Test du système de version de l'API ===\n")

# Test 1: Vérifier la version par défaut
print("Test 1: Version par défaut")
print(f"Version API: {pearl.api_version}")
print(f"URL API: {_get_api_url()}")
assert pearl.api_version == "v2", "La version par défaut devrait être v2"
assert _get_api_url() == "https://api.nlpearl.ai/v2", "L'URL par défaut devrait pointer vers v2"
print("[OK] Test reussi\n")

# Test 2: Basculer vers v1
print("Test 2: Basculer vers v1")
pearl.api_version = "v1"
print(f"Version API: {pearl.api_version}")
print(f"URL API: {_get_api_url()}")
assert pearl.api_version == "v1", "La version devrait être v1"
assert _get_api_url() == "https://api.nlpearl.ai/v1", "L'URL devrait pointer vers v1"
print("[OK] Test reussi\n")

# Test 3: Revenir à v2
print("Test 3: Revenir à v2")
pearl.api_version = "v2"
print(f"Version API: {pearl.api_version}")
print(f"URL API: {_get_api_url()}")
assert pearl.api_version == "v2", "La version devrait être v2"
assert _get_api_url() == "https://api.nlpearl.ai/v2", "L'URL devrait pointer vers v2"
print("[OK] Test reussi\n")

# Test 4: Tester avec une version personnalisée (v3, v4, etc.)
print("Test 4: Version personnalisée (v3)")
pearl.api_version = "v3"
print(f"Version API: {pearl.api_version}")
print(f"URL API: {_get_api_url()}")
assert _get_api_url() == "https://api.nlpearl.ai/v3", "L'URL devrait pointer vers v3"
print("[OK] Test reussi\n")

# Test 5: Tester avec None (devrait revenir à v2 par défaut)
print("Test 5: Version None (devrait revenir à v2)")
pearl.api_version = None
print(f"Version API: {pearl.api_version}")
print(f"URL API: {_get_api_url()}")
assert _get_api_url() == "https://api.nlpearl.ai/v2", "L'URL devrait revenir à v2 par défaut"
print("[OK] Test reussi\n")

# Réinitialiser à v2 pour les autres tests
pearl.api_version = "v2"

print("=== Tous les tests ont réussi! ===")

