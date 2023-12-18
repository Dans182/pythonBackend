def user_schema(user) -> dict:
    return{"id": str(user["_id"]),
           "username": user["username"],
           "email": user["email"]}

#Esto tranforma lo que viene de la DB a lo que espera que tiene nuestro objeto de modelo que es User, la clase User.