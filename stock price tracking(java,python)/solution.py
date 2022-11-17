def solution(prices):
    answer = []
    for p in range(0, len(prices)-1):   
        i= 1
        duration = 0   
        while i < len(prices)-p:
            duration += 1   
            if prices[p] > prices[p+i]:   
                break
            i += 1    

        answer.append(duration)   
    answer.append(0)  

    return answer