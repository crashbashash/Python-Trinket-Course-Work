from random import randint

def GetCheckSum(cNumber: str, check: bool):
    if not check and len(cNumber) < 16:
        cNumber += "0"
    sum: int = 0
    for i, num in enumerate((cNumber[::-1])[1:len(cNumber)]):
        curNum: int
        if i % 2 == 0:
            curNum = int(num) * 2
            if curNum > 9:
                sum += int(str(curNum)[0]) + int(str(curNum)[1])
            else:
                sum += curNum
        else:
            sum += int(num)
    
    newCheck = ((sum*9)%10)

    if check:
        ogCheck = cNumber[-1]    
        return (newCheck == int(ogCheck)), newCheck
    else:
        return str(newCheck)


def GenerateCardNumber():
    cardNum: str = "4"

    for _ in range(0, 14):
        cardNum += str(randint(0, 9))
    
    return cardNum + GetCheckSum(cardNum, False)

print("\nCard Number: " + GenerateCardNumber())
print("\nVerification Site: https://ccardgenerator.com/credit-card-validator.php\n")

input("\nHit ENTER/RETURN to continue....")