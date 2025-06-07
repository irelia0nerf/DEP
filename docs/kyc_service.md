# KYC Service

`get_identity` provides simulated KYC verification with optional encryption of PII.

## Verification Levels
- **Level 0**: Unverified wallet.
- **Level 1–3**: Increasing levels of verification. The level is derived from the last hex digit of the wallet address.

## PII Encryption
Pass a `cryptography.fernet.Fernet` instance to encrypt the returned email address:

```python
from cryptography.fernet import Fernet
from app.services.kyc import get_identity

fernet = Fernet.generate_key()
identity = await get_identity("0xabc4", fernet=Fernet(fernet))
```
