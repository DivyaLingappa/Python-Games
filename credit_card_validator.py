#The Luhn algorithm is a simple checksum formula used to validate a variety of identification #numbers such as credit card numbers, IMEI numbers 

def luhn_algorithm(num,length):
    checksum=num%10
    card_sum=0
    for i in range(1,length):
        num=int(num/10)
        number=num%10
        if(i%2==0):
            card_sum+=number
        else:
            double_num=number*2
            if(double_num>=10):
                double_num-=9
            card_sum+=double_num
    return (10-(card_sum%10)==checksum)

def main():
    card_str=input('Enter a credit card number ')
    card_str=card_str.replace(' ','')
    length_num=len(card_str)
    card_validator=luhn_algorithm(int(card_str),length_num)
    if(card_validator==True):
        print("This is a valid credit card")
    else:
        print("This is not a valid credit card")

main()

