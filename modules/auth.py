import jwt

def verify_token(token, config):
    """from auth0 docs"""
    jwks_url = f'https://{config["DOMAIN"]}/.well-known/jwks.json'
    
    jwks_client = jwt.PyJWKClient(jwks_url)

    # This gets the 'kid' from the passed token
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(
            token
        ).key
    except jwt.exceptions.PyJWKClientError as error:
        return {"status": "error", "msg": error.__str__()}
    except jwt.exceptions.DecodeError as error:
        return {"status": "error", "msg": error.__str__()}

    try:
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=config["ALGORITHMS"],
            audience=config["API_AUDIENCE"],
            issuer=config["ISSUER"],
        )
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return payload