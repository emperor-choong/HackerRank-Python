X = int(input())
stock = list(map(int, input().split()))
N = int(input())

customer_order = []
for _ in range(N):
    shoe_size, x = map(int, input().split())
    pair = (shoe_size, x)
    customer_order.append(pair)

sum = 0         
for pair in customer_order:
    if pair[0] in stock:
        sum = sum + pair[1]
        stock.remove(pair[0])

print(sum)



                

    
