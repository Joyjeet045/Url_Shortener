import random
import string
from .models import URLShortener

def generate_unique_short_code():
  #domain of code
  characters=string.ascii_letters+string.digits
  code_length=6
  while True:
    middle_part=''.join(random.choice(characters) for _ in range(code_length-2))
    first_letter=random.choice(string.ascii_uppercase)
    last_digit=random.choice(string.digits)
    short_code=first_letter+middle_part+last_digit
    if not URLShortener.objects.filter(short_code=short_code).exists():
      return short_code
    