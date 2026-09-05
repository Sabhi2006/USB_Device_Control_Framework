from policy_engine import PolicyEngine


def main():
    policy = PolicyEngine()

    # Test 1: Device present in allowlist
    allowed_device = {
        "vid": "2717",
        "pid": "FF40"
    }

    # Test 2: Device not present in allowlist
    unknown_device = {
        "vid": "1234",
        "pid": "5678"
    }

    print("=" * 50)
    print("USB AUTHORIZATION TEST")
    print("=" * 50)

    print("\nTest 1: Allowlisted device")
    print("VID: 2717 | PID: FF40")
    print("Authorization:", policy.is_authorized(allowed_device))

    print("\nTest 2: Unknown device")
    print("VID: 1234 | PID: 5678")
    print("Authorization:", policy.is_authorized(unknown_device))

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()