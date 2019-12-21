
'''
Uygur Tepe 105006877
CS Games Team B Application
'''

def solution(stocks):
    low = min(stocks)           #get lowest value
    dayLow = stocks.index(low)  #get index of lowest value
    
    dayHigh = -1                #assume there is no maxProfit              
    
    if(max(stocks[dayLow:]) > low):   #if statement to find max after the index of the lowest value
        high = max(stocks[dayLow+1:])   #get highest value
        dayHigh = stocks.index(high)    #get index of highest value
    
    if(dayHigh == -1):
        print("0 \nNo transaction is done, i.e. max profit = 0.")
    else:
        print(high - low)   #subtract these prices to find the profit
        print("Buy on day " + str(dayLow+1) + ", (price = " + str(low) + "), and sell on day " + str(dayHigh+1) + ", (price = " + str(high) + ")")
  
if __name__ == '__main__':
    #[7, 1, 5, 3, 6, 4] #sample test case #1 from README.md
    stocks = list(map(int, input("Enter the Integer values of the stocks (separate values with spaces): \n").split()))
    solution(stocks)