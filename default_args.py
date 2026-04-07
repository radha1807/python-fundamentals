def  call_llm(prompt, model='gpt-4o-mini', temperature=0, max_tokens=500):
    print(f"prompt={prompt}, model={model}, temp={temperature}, tokens={max_tokens}")
    
call_llm('Hello',  temperature=0.9)  


def order(item, quantity = 1, payment= 'cod'):
    print(f"item={item},qty={quantity}, payment= {payment}")
order("Laptop", 2, "Card")



def order(item, quantity=1, payment='COD'):
    print(f"\n--- Order Summary ---")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Payment: {payment}")

# 1. Ask the user for details
user_item = input("What do you want to buy? ")
user_qty = input("How many do you want? ")
user_pay = input("Payment method (Card/COD): ")

# 2. Pass those 'user' variables into the function
order(user_item, user_qty, user_pay)