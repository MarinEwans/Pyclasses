#this code takes credit card numbers and returns numbers hidden with asteriks and last four digits
# in this code tuples were used 
card_number=input("enter your credit card number:")
def credit_card_number(card_number):
    if len(card_number) <16:
        return "invalid card number"
    last_digits=card_number[-4:]
    hidden_count=len(card_number)-4
    hidden_charecters=('*',)*hidden_count
    hidden_card_number=hidden_charecters + (last_digits,)
    return ''.join(hidden_card_number)
print("hidden card number is:", credit_card_number(card_number))   