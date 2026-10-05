from datetime import UTC, datetime, timedelta

from jose import jwt

SECRET_KEY = "f7Kp2Lm9Qx4Vn8Rt3Yw6Za1Bc5De7GhJ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(user_id: str, email: str, roles: list[str]) -> str:
    expire = datetime.now(UTC) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )

    payload = {"sub": user_id, "email": email, "exp": expire, "roles": roles}

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> dict | None:
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )
