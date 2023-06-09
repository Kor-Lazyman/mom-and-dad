import pandas as pd
import numpy as np
import random 

class Table:
    def __init__(self):
        self.Inventory=0#현재재고
        self.incoming_delivery=0#도착한 물건
        self.available=0#판매 가능량
        self.backorder=0#배송 미달량
        self.total_order=0#전체 배송 요청
        self.delivery=0#배송량
        self.incoming_order= 0#요청된 배송
        self.cost=0#현재 지출 비용
        self.order=0#발주량
        self.on_delivery=0#나에게 배송중인양
        
    def Incoming_delivery(self,deliver):
        self.incoming_delivery=deliver
        
    def inventory(self,past_inventory):
        self.Inventory=past_inventory
        
    def Available_update(self):#현재 판매 가능량 업데이트
        self.available=self.incoming_delivery+self.Inventory
        
    def Incoming_order(self,order):
        self.incoming_order=order
        
    def Backorder(self,past_backorder):#부족한 재고
        self.backorder=past_backorder

    def Total_order(self):#총 주문량
        self.total_order= self.backorder+self.incoming_order

    def Delivery(self):#총 배송량
        self.delivery= min(self.available,self.total_order)
        self.backorder=abs(min(self.available-self.incoming_order,0))
        
    def Cost(self,cost):
        if self.backorder>0:
            
            self.cost=self.cost-(2)*self.backorder

        else:
            self.cost=self.cost-self.Inventory
            
    def Order(self):#발주 입력  
        print("정규 발주")  
        self.order=int(input())
        
    def On_delivery(self,on_delivery):
        self.on_delivery=on_delivery
    
             
def Retailer_Env(x,Retailer,Retailer_df,Present_inventory,Wholesaler_df,action):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        Retailer.Inventory=(20)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
    
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        #발주 해야하는 양
        Retailer.order=action
        
        
        
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.inventory=Present_inventory
        Retailer.Available_update()
        
        Retailer.Incoming_order(random.randint(0,50))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

        #발주 해야하는 양
        Retailer.order=action
        
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order((random.randint(0,50)))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
                

        #발주 해야하는 양
        Retailer.order=action
        
        
    else:
        Retailer.Incoming_delivery(Wholesaler_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(random.randint(0,50))
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        

        #발주 해야하는 양
        Retailer.order=action
        
        
        #업데이트
    
    temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
    #DataFrame에 추가
    
    Retailer_df.loc[x]=temp
 
    return Retailer_df,Present_inventory,Retailer.cost,Retailer.incoming_order

def Wholesaler_Env(x,Retailer,Retailer_df,Present_inventory,df,Distributer_df,action):
    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        Retailer.Inventory=(20)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=action
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #업데이트
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        #DataFrame에 추가
        Retailer_df.loc[x]=temp
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        
        Retailer_df.loc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Distributer_df.loc[x-2][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.loc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        
    else:
        Retailer.Incoming_delivery(Distributer_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.loc[x]=temp
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

    return Retailer_df,Present_inventory,Retailer.cost


def Distributer_Env(x,Retailer,Retailer_df,Present_inventory,Wholesaler_df,Manufacture_df,action):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        Retailer.inventory(20)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=action
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==1:
        Retailer.Incoming_delivery(0)

        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Retailer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        
    elif x==2:
        Retailer.Incoming_delivery(0)

        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Manufacture_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

        
    else:
        Retailer.Incoming_delivery(Manufacture_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Wholesaler_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Manufacture_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    Retailer_df.loc[x]=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                   Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                   abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]


    return Retailer_df,Present_inventory,Retailer.cost

def Manufacturer_Env(x,Retailer,Retailer_df,Present_inventory,Distributer_df,action):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        Retailer.Inventory=(20)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        Retailer.Incoming_order(0)
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
        
        #발주 해야하는 양
        Retailer.order=action
        
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
        
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        #업데이트
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        #DataFrame에 추가
        Retailer_df.loc[x]=temp
        
        #Inventory 업데이트
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
    
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.loc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    elif x==2:
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.loc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    else:
        Retailer.Incoming_delivery(random.randint(0,50))
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(Distributer_df.loc[x-1][-1])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.order=action
        
        Retailer.On_delivery(Distributer_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
        Retailer_df.loc[x]=temp
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
    return Retailer_df,Present_inventory,Retailer.cost

             
def Retailer_Env_test (x,Retailer,Retailer_df,Present_inventory,Wholesaler_df,action,dataset):

    if x==0:
        #현재 도착한 재고
        Retailer.Incoming_delivery(0)

        #초기 재고 설정
        Retailer.Inventory=(20)
        
        #판매재고 업데이트
        Retailer.Available_update()
        
        #주문받은 재고
        
        Retailer.Incoming_order(dataset[x])
        
        #부족한 재고
        Retailer.Backorder(0)
        
        #전체 처리가 필요한 주문량
        Retailer.Total_order()
          
        #현재 배송이 오고있는 재고
        Retailer.On_delivery(0)
          
        #배송을 할 양
        Retailer.Delivery()
        
        #현재 비용
        Retailer.Cost(0)
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        
        #발주 해야하는 양
        Retailer.order=action
        
        
        
    
    elif x==1:
        Retailer.Incoming_delivery(0)
        
        Retailer.inventory=Present_inventory
        
        Retailer.Available_update()
        
        Retailer.Incoming_order(dataset[x])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(0)
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[0][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)

        #발주 해야하는 양
        Retailer.order=action
        
        
    elif x==2:
        
        Retailer.Incoming_delivery(0)
        
        Retailer.Inventory=(Present_inventory)
        
        Retailer.Available_update()
        
        Retailer.Incoming_order(dataset[x])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
                

        #발주 해야하는 양
        Retailer.order=action
        
    else:
        
        Retailer.Incoming_delivery(Wholesaler_df.loc[x-2][-3])
        
        Retailer.Inventory=(Present_inventory)
        Retailer.Available_update()
        
        Retailer.Incoming_order(dataset[x])
        
        Retailer.Backorder(Retailer_df.loc[x-1][4])
        
        Retailer.Total_order()
        
        Retailer.On_delivery(Wholesaler_df.loc[x-1][-3])
        
        Retailer.Delivery()
        
        Retailer.backorder=max(Retailer.total_order-Retailer.available,0)
        
        Retailer.Cost(-Retailer_df.loc[x-1][6])
        
        Present_inventory=max(Retailer.available-Retailer.total_order,0)
        

        #발주 해야하는 양
        Retailer.order=action
        
        
        #업데이트
    
    temp=[Retailer.incoming_delivery,Retailer.Inventory,Retailer.available,
                       Retailer.incoming_order,Retailer.backorder,Retailer.total_order,
                       abs(Retailer.cost),Retailer.delivery,Retailer.on_delivery,Retailer.order]
        
    #DataFrame에 추가
    
    Retailer_df.loc[x]=temp
 
    return Retailer_df,Present_inventory,Retailer.cost

class Agent ():
    def __init__ (self):
        pass
    
    def select_action(self):
        action=random.randint(0,50)
       
        return action
    
def reset(Total_Weeks):
    Retailer_df=np.zeros((Total_Weeks,10))
    Retailer_df=pd.DataFrame(Retailer_df)
    Retailer_df.columns=['Incoming_delivery','Inventory','available',
                             'Incoming_order','Backorder','Total_order',
                             'Cost','Delivery','Your_delivery','Your_order']

    Wholesaler_df=np.zeros((Total_Weeks,10))
    Wholesaler_df=pd.DataFrame(Wholesaler_df)
    Wholesaler_df.columns=['Incoming_delivery','Inventory','available',
                             'Incoming_order','Backorder','Total_order',
                             'Cost','Delivery','Your_delivery','Your_order']

    Distributer_df=np.zeros((Total_Weeks,10))
    Distributer_df=pd.DataFrame(Distributer_df)
    Distributer_df.columns=['Incoming_delivery','Inventory','available',
                             'Incoming_order','Backorder','Total_order',
                             'Cost','Delivery','Your_delivery','Your_order']

    Manufacture_df=np.zeros((Total_Weeks,10))
    Manufacture_df=pd.DataFrame(Manufacture_df)
    Manufacture_df.columns=['Incoming_delivery','Inventory','available',
                             'Incoming_order','Backorder','Total_order',
                             'Cost','Delivery','Your_delivery','Your_order']


    Present_Retailer_Inventory=0
    Present_Wholesaler_Inventory=0
    Present_Distributer_Inventory=0
    Present_Manufacturer_Inventory=0
    
    return Retailer_df,Present_Retailer_Inventory,Wholesaler_df,Present_Wholesaler_Inventory,Distributer_df,Present_Distributer_Inventory,Manufacture_df,Present_Manufacturer_Inventory


def training(x_prime,y_prime,x,y,df,data,totalweek):
    alpha=0.0015
    

    reward=(-1)*abs(df.loc[x][2]-df.loc[x][5])-df.loc[x][6]
    for i in range(len(df)):
        for j in range(len(df.loc[0])):
            if i != x and j != y:
                if x==totalweek-1:
                    data[i][j]+=data[x][y]+alpha*(reward-data[x][y])-15
                    
                elif x==totalweek-2:
                    data[i][j]+=data[x][y]+alpha*(reward
                                                 +np.argmax(data[x_prime])
                                                 -data[x][y])-15
                    
                elif x==totalweek-3:
                    data[i][j]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                                 -data[x][y])-15
                                
                elif x==totalweek-4:
                    data[i][j]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                                 +np.argmax(data[x_prime+1])
                                                 +np.argmax(data[x_prime+2])
                                                 -data[x][y])-15
                elif x==totalweek-5:
                    data[i][j]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                                 +np.argmax(data[x_prime+1])
                                                 +np.argmax(data[x_prime+2])
                                                 +np.argmax(data[x_prime+3])
                                                 -data[x][y])-15
                else:
                    data[i][j]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                                 +np.argmax(data[x_prime+1])
                                                 +np.argmax(data[x_prime+2])
                                                 +np.argmax(data[x_prime+3])
                                                 +np.argmax(data[x_prime+4])
                                                 -data[x][y])-15
            
    if x==totalweek-1:
        data[x][y]+=data[x][y]+alpha*(reward-data[x][y])
        
    elif x==totalweek-2:
        data[x][y]+=data[x][y]+alpha*(reward
                                     +np.argmax(data[x_prime])
                                     -data[x][y])
        
    elif x==totalweek-3:
        data[x][y]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                     -data[x][y])
                    
    elif x==totalweek-4:
        data[x][y]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
                                     +np.argmax(data[x_prime+1])
                                     +np.argmax(data[x_prime+2])
                                     -data[x][y])
    elif x==totalweek-5:
        data[x][y]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
          +np.argmax(data[x_prime+1])
          +np.argmax(data[x_prime+2])
          +np.argmax(data[x_prime+3])
          -data[x][y])
    else:
        data[x][y]+=data[x][y]+alpha*(reward+np.argmax(data[x_prime])
        +np.argmax(data[x_prime+1])
        +np.argmax(data[x_prime+2])
        +np.argmax(data[x_prime+3])
        +np.argmax(data[x_prime+4])
        -data[x][y])
        
    return data


def Test(Total_Weeks,result_r,result_w,result_d,result_m,dataset):
    RL=0
    Sample=0
    RL_group=0
    Sample_group=0
    
    week=0
    
    print('start_test')
    
    for y in range(100):
        
        agent=Agent()
        Test_cost_R=0
        Test_cost_W=0
        Test_cost_D=0
        Test_cost_M=0
        
        RL_cost_R=0
        RL_cost_W=0
        RL_cost_D=0
        RL_cost_M=0
        
        Retailer_df,Present_Retailer_Inventory,Wholesaler_df,Present_Wholesaler_Inventory,Distributer_df,Present_Distributer_Inventory,Manufacture_df,Present_Manufacturer_Inventory=reset(Total_Weeks)
        week=0
        temp=0
        
        action_r=agent.select_action()
        action_w=agent.select_action()
        action_d=agent.select_action()
        action_m=agent.select_action()
        
        cost_m,cost_d,cost_w,cost_m=0,0,0,0
        
        Retailer=Table()
        Wholesaler=Table()
        Distributer=Table()
        Manufacture=Table()
        
        for x in range(Total_Weeks):
        
            Manufacture_df,Present_Manufacturer_Inventory,cost_m=Manufacturer_Env(week,Manufacture,Manufacture_df,Present_Manufacturer_Inventory,Distributer_df,action_m)
            Distributer_df,Present_Distributer_Inventory,cost_d=Distributer_Env(week,Distributer,Distributer_df,Present_Distributer_Inventory,Wholesaler_df,Manufacture_df,action_d)
            Wholesaler_df,Present_Wholesaler_Inventory,cost_w=Wholesaler_Env(week,Wholesaler,Wholesaler_df,Present_Wholesaler_Inventory,Retailer_df,Distributer_df,action_w)
            Retailer_df,Present_Retailer_Inventory,cost_r,temp=Retailer_Env(week,Retailer,Retailer_df,Present_Retailer_Inventory,Wholesaler_df,action_r)
        
            week+=1
            
        Test_cost_R=(Retailer_df.loc[Total_Weeks-1][6])
        Test_cost_W=(Wholesaler_df.loc[Total_Weeks-1][6])
        Test_cost_D=(Distributer_df.loc[Total_Weeks-1][6])
        Test_cost_M=(Manufacture_df.loc[Total_Weeks-1][6])
            
        Retailer_df,Present_Retailer_Inventory,Wholesaler_df,Present_Wholesaler_Inventory,Distributer_df,Present_Distributer_Inventory,Manufacture_df,Present_Manufacturer_Inventory=reset(Total_Weeks)
        week=0
        
        cost_m,cost_d,cost_w,cost_m=0,0,0,0
        
        Retailer=Table()
        Wholesaler=Table()
        Distributer=Table()
        Manufacture=Table()

        for x in range(Total_Weeks):
            
            action_r=result_r[x] 
            action_w=result_w[x]
            action_d=result_d[x]
            action_m=result_m[x]
            Manufacture_df,Present_Manufacturer_Inventory,cost_m=Manufacturer_Env(week,Manufacture,Manufacture_df,Present_Manufacturer_Inventory,Distributer_df,action_m)
            Distributer_df,Present_Distributer_Inventory,cost_d=Distributer_Env(week,Distributer,Distributer_df,Present_Distributer_Inventory,Wholesaler_df,Manufacture_df,action_d)
            Wholesaler_df,Present_Wholesaler_Inventory,cost_w=Wholesaler_Env(week,Wholesaler,Wholesaler_df,Present_Wholesaler_Inventory,Retailer_df,Distributer_df,action_w)
            Retailer_df,Present_Retailer_Inventory,cost_r=Retailer_Env_test(week,Retailer,Retailer_df,Present_Retailer_Inventory,Wholesaler_df,action_r,dataset)
            
            week+=1
            
        RL_cost_R=(Retailer_df.loc[Total_Weeks-1][6])
        RL_cost_W=(Wholesaler_df.loc[Total_Weeks-1][6])
        RL_cost_D=(Distributer_df.loc[Total_Weeks-1][6])
        RL_cost_M=(Manufacture_df.loc[Total_Weeks-1][6])
        
        if y%10==0:
            print(RL_cost_R,Test_cost_R)
            print(RL_cost_W,Test_cost_W)
            print(RL_cost_D,Test_cost_D)
            print(RL_cost_M,Test_cost_M)
            print("Now:",y)
        
        if(RL_cost_R+RL_cost_W+RL_cost_D+RL_cost_M<=Test_cost_R+Test_cost_W+Test_cost_D+Test_cost_M):
   
            RL+=1
            
        elif(RL_cost_R>Test_cost_R):
            Sample+=1
            
        if(RL_cost_W<=Test_cost_W):
            RL+=1
            
        elif(RL_cost_W>Test_cost_W):
            Sample+=1
        
        if(RL_cost_D<=Test_cost_D):
            RL+=1
            
        elif(RL_cost_D>Test_cost_D):
            Sample+=1
        
        if(RL_cost_M<=Test_cost_M):
            RL+=1
            
        elif(RL_cost_M>Test_cost_M):
            Sample+=1
            
        if(RL_cost_R+RL_cost_W+RL_cost_D+RL_cost_M<=Test_cost_R+Test_cost_W+Test_cost_D+Test_cost_M):
   
            RL_group+=1
            
        else:
            Sample_group+=1
           
    return RL,Sample,RL_group,Sample_group
    
    
def main():
    Retailer=Table()
    Wholesaler=Table()
    Distributer=Table()
    Manufacture=Table()
    print("진행시킬 게임의 총 주를 입력하시오:")
    
    Total_Weeks=int(input())
    done=False
    
    week=0
    
    while(done==False):
        
        agent=Agent()
        data_r=[]
        data_w=[]
        data_d=[]
        data_m=[]
        
        data_r=np.zeros((Total_Weeks,51))
        data_w=np.zeros((Total_Weeks,51))
        data_d=np.zeros((Total_Weeks,51))
        data_m=np.zeros((Total_Weeks,51))

        for k in range(5000):
            Retailer_df,Present_Retailer_Inventory,Wholesaler_df,Present_Wholesaler_Inventory,Distributer_df,Present_Distributer_Inventory,Manufacture_df,Present_Manufacturer_Inventory=reset(Total_Weeks)
            
            done=False
            
            week=0
            dataset=[]
            action_r=agent.select_action()
            action_w=agent.select_action()
            action_d=agent.select_action()
            action_m=agent.select_action()
            
            Retailer=Table()
            Wholesaler=Table()
            Distributer=Table()
            Manufacture=Table()
            agent=Agent()
            
            while not done:
    
                Manufacture_df,Present_Manufacturer_Inventory,cost_m=Manufacturer_Env(week,Manufacture,Manufacture_df,Present_Manufacturer_Inventory,Distributer_df,action_m)
                Distributer_df,Present_Distributer_Inventory,cost_d=Distributer_Env(week,Distributer,Distributer_df,Present_Distributer_Inventory,Wholesaler_df,Manufacture_df,action_d)
                Wholesaler_df,Present_Wholesaler_Inventory,cost_w=Wholesaler_Env(week,Wholesaler,Wholesaler_df,Present_Wholesaler_Inventory,Retailer_df,Distributer_df,action_w)
                Retailer_df,Present_Retailer_Inventory,cost_r,temp=Retailer_Env(week,Retailer,Retailer_df,Present_Retailer_Inventory,Wholesaler_df,action_r)
                
                dataset.append(temp)

                
                
                if week+1==Total_Weeks:
                    done=True
                
                else:
                    data_r=training(week+1,agent.select_action(),week,np.argmax(data_r[week]),Retailer_df,data_r,Total_Weeks)
                    data_w=training(week+1,agent.select_action(),week,np.argmax(data_w[week]),Wholesaler_df,data_w,Total_Weeks)
                    data_d=training(week+1,agent.select_action(),week,np.argmax(data_d[week]),Distributer_df,data_d,Total_Weeks)
                    data_m=training(week+1,agent.select_action(),week,np.argmax(data_m[week]),Manufacture_df,data_m,Total_Weeks)
                
                week+=1
                
            if k%10==0:
                print(k)
   
    df_r=pd.DataFrame(data_m)
    df_w=pd.DataFrame(data_w)
    df_d=pd.DataFrame(data_d)
    df_m=pd.DataFrame(data_r)

    result_r=[]
    result_w=[]
    result_d=[]
    result_m=[]
    
    for x in range(len(df_r)):
        result_r.append(np.argmax((df_r.loc[x])))
        result_w.append(np.argmax((df_w.loc[x])))
        result_d.append(np.argmax((df_d.loc[x])))
        result_m.append(np.argmax((df_m.loc[x])))
    
 
    #df_r.to_csv("RESULT_r.csv")
    #df_w.to_csv("RESULT_w.csv")
    #df_d.to_csv("RESULT_d.csv")
    #df_m.to_csv("RESULT_m.csv")
    
    print('\n')
    print("Retailer Policy:",result_r,"\nWholesaler Policy:",result_w,"\nDistribution Policy:",result_d,"\nManufacture Policy:",result_m)
    list_=[result_r,result_w,result_d,result_m]
    df=pd.DataFrame(list_,index=['Retailer','Wholesaler','Distribution','Manufacture'])
    
    print('\n')
    df.to_csv("Policy.csv")
    
    RL,Sample,RL_group,Sample_group=Test(Total_Weeks,result_r,result_w,result_d,result_m,dataset)
    
    print("Solo_Accuracy:",(RL/400)*100,"%\t","Group_Accuracy:",(RL_group),'%')


main()





