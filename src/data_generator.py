import random
import re
import string


users_ids     = list(range(1,101))
recipient_ids = list(range(1,101))


def generate_message() -> dict:
    random_user_id = random.choice(users_ids)

    # Cópia do array recipients
    recipient_ids_copy = recipient_ids.copy()

    # usuário não pode mandar mensagem para si mesmo
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    # Gera uma mensagem de forma randomica
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id':random_recipient_id,
        'message':message
    }


# Teste

if __name__ == "__main__":

    print(generate_message())

