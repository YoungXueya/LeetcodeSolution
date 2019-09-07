class Solution:
	# Sort first and then comapre the same user.
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=[False for i in range(len(transactions))]
        for i in range(len(transactions)):
            name,time,price,city=transactions[i].split(",")
            if int(price)>1000:
                invalid[i]=True
            for j in range(i+1,len(transactions)):
                name1,time1,price1,city1=transactions[j].split(",")
                #print(name==name1 and abs(int(time1)-int(time))<=60 and city!=city)
                if name1==name and abs(int(time1)-int(time))<=60 and city!=city1:
                    invalid[i]=True
                    invalid[j]=True
        result=[]
        for i in range(len(invalid)):
            if invalid[i]:
                result.append(transactions[i])   
        return result
                
    # Totally brute force.
	
    def invalidTransactions1(self, transactions: List[str]) -> List[str]:
        invalid=[False for i in range(len(transactions))]
        for i in range(len(transactions)):
            name,time,price,city=transactions[i].split(",")
            if int(price)>1000:
                invalid[i]=True
            for j in range(i+1,len(transactions)):
                name1,time1,price1,city1=transactions[j].split(",")
                #print(name==name1 and abs(int(time1)-int(time))<=60 and city!=city)
                if name1==name and abs(int(time1)-int(time))<=60 and city!=city1:
                    invalid[i]=True
                    invalid[j]=True
        result=[]
        for i in range(len(invalid)):
            if invalid[i]:
                result.append(transactions[i])
                
        return result
                