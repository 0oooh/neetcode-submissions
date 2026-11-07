class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #자, 생각해 봅시다. 먼저 첫 번째 숫자를 현재 가격으로 잡아. 현재 가격으로 잡고,
        buyprice_and_day = [prices[0], 0]
        sellprice_and_day = [0, 0]
        max_profit = 0

        for day in range(len(prices)):
            #그럼 이제 두 가지 케이스가 있겠지. 
            #1.먼저 다음 숫자가 현재 가격보다 쌀 때, 그리고 다음 숫자니까 나란 다음이니까 이건 자동인 거고.
            #그럼 쌀 때는 어떻게 대응하냐? 이거 쌀 때는 이 싼 가격으로 사야겠지? 
            if prices[day] <= buyprice_and_day[0]:
                #Buy를 해야겠지, 우리가?
                buyprice_and_day[0] = prices[day]
                #그러고 나서 날짜도 Buy 날짜를 업데이트해야겠지? 
                buyprice_and_day[1] = day
                #그러면 Sell 날짜는 어떻게 되냐? Sell 날짜는 초기화가 돼야지. 그러니까 현재 Buy 가격과
                sellprice_and_day[0] = prices[day]
                #Buy 날짜로 초기화가 된다.
                sellprice_and_day[1] = day
            #2. 그럼 반대로 가격이 올랐을 때는 어떻게 하냐? 그러면 이때는 올랐어. 그러면 Buy는 냅둬.
            elif prices[day] > buyprice_and_day[0] and prices[day] > sellprice_and_day[0]:
                #대신 팔 수 있는 후보 가격이 되겠지? 팔 수 있는 후보 가격이 되면 가격을 업데이트하고, 
                sellprice_and_day[0] = prices[day]
                sellprice_and_day[1] = day

            max_profit = max(max_profit, sellprice_and_day[0] - buyprice_and_day[0])

        return max_profit

        