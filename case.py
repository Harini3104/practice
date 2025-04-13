value="one"
match value:
    case "one":
        res=1
    case"two":
        res=2
    case"three|four": 
        res=(3,4)
    case _:
        res=-1
print(res)
