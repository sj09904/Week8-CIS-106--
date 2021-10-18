def main():
    userInput, month, sales = getAttributes()
    #the above assigns the threee inputs to the getAttributes() function
    NextMonthSales = userEnter(month, sales, userInput)
    #the dynamic variable NextMonthSales is created from the userEnter function which takes three variables, month(string), sales(int), userInput(yes or no)
def getAttributes():
    userInput = input("Start Forcast? ")
    #This could use some error handling as the runtime will contiune even if the user enters 'no'
    month = input("enter the month: ")
    #month again isn't a regulated input. This relies on the user entering the three letter abbreviation. Anything else will be multiplied by the 1.25 defined in the 'else' clause
    sales = int(input("sales?: "))
    return userInput, month, sales
    #the function getAttributes() returns the three variables
def userEnter (month, sales, userInput):
  #userEnter func takes these three variables and utilises them. Python uses 2 * '=' to symbolise equality 
    while userInput == "yes":
        if month in ["Jan", "Feb", "Mar", "jan", "feb", "mar"]:
          #use of an array of strings (denoted by the '['|']') to tidy it up. the if statement will scan the array to see if the value exists
            NextMonthSales = sales * 1.1
            print(NextMonthSales)
            #break is used as this is a while loop, and without break it would be an indefinite loop (run forever)
            break
        elif month in ["Apr", "May", "Jun", "apr", "may","jun"]:
            NextMonthSales = sales * 1.15
            print(NextMonthSales)
            break
        elif month in ["Jul", "Aug", "Sep", "jul", "aug", "sep"]:
            #each array has a capitalised and non-capitalised version to avert human error
            NextMonthSales = sales * 1.20
            print(NextMonthSales)
            break
        else:
            NextMonthSales = sales * 1.25
            print(NextMonthSales)
            break


main()
#all encased in a main() function
