while True:
    n = input("Enter a number: ")
    if n == "exit":
        break
    try:
        n = int(n)
        if n <= 0:
            print("The number must be larger than 0 and positive")
            continue
    except Exception as e:
        print("Error:", e)
        
    for i in range(1, n+1):
        print(i * '*')