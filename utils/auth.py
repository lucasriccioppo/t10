import jwt
import bcrypt

key = 'NfHfP9Fd8K-_-bqdMf2LUm0rdnh2-enbC6Qm1h26xVWVUMTxadMsK3_KAoMLq5GoI0DG9ICB68otobgDz3tdhajEP_3n7CfXjWnAyE819R3LydyNWebx07DiujV9aTSD_hY1i99Nstp5m-57gC1QOltTo9j2vkcfqKF5guDW4lyMdIcFYfyr00aTcf9bFhY2cmyydzHMfaJi_BveuYHqJw30bOnpAr-9HlDrTgqmU7HaH9bhK1pZ3fT_1yIgGjyp7lQFHIdQfJxeG4G8GkOwAhnMFnDdoroEIZ03PWjHuX0Xlr3UES1_cDA1jx2vaHKke7fEo25zy39CZ9aLE3iIIQ'

def hash_password(password):
    return bcrypt.hashpw(bytes(password, encoding='utf-8'), bcrypt.gensalt())

def check_password(password):
    return bcrypt.checkpw(password, hash_password(password))

def get_token(usuario, acesso):
    return jwt.encode({'usuario': usuario, 'acesso': acesso}, key, algorithm='HS256')

def decode(encrypted):
    return jwt.decode(encrypted, key, algorithms='HS256')



