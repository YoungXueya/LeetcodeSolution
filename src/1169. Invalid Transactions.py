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
    # Use dict to collect same user together.
    def invalidTransactions2(self, transactions: List[str]) -> List[str]:
        invalid=[]
        persons={}
        for i in range(len(transactions)):
            name,time,price,city=transactions[i].split(',')
            if name not in persons:
                persons[name]=[[time,price,city]]
            else:
                persons[name].append([time,price,city])
       
        
        for person in persons:
            detail=persons[person]
            for i in range(len(detail)):
                time,price,city=detail[i][0],detail[i][1],detail[i][2]
                if int(price)>1000:
                    invalid.append(",".join([person,detail[i][0],detail[i][1],detail[i][2]]))
                for j in range(i+1,len(detail)):
                    time1,price1,city1=detail[j][0],detail[j][1],detail[j][2]
                    if abs(int(time1)-int(time))<=60 and city1!=city:
                        invalid.append(",".join([person,detail[i][0],detail[i][1],detail[i][2]]))
                        invalid.append(",".join([person,detail[j][0],detail[j][1],detail[j][2]]))
        return list(set(invalid))
                    
        # return None    
                
                
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
                
