
# to find the frequency of maximum height of candles

# user input -> storing in a list
num=int(input( "Happy Birthday!  Please Enter the Age of your neice :" ))
candle = [int(i) for i in input("Please enter the candles height ").split()]

# defining a functn to find the frequency of maximum height candles
def birthdaycandles(num,candle) :

    x=max(candle)
    x=candle.count(x)
    return(x)

#calling the function within a print to show output
print ( "Your Neice Will Be Able to Blow Out ", birthdaycandles(num,candle) , ' candles ' )
