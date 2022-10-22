import time
import numpy as np
import numba as nb
arr=np.ndarray
@nb.vectorize()
def do(Sstr :arr,Vstr :arr,record :arr,times :int=1000):
    for _ in range(times):
        Sstr+=Vstr
        Vstr=Sstr>>7
        record[:, _%100]=Sstr
        return (Sstr :arr,Vstr :arr,record :arr)
def main():
    Sstr=np.array([2000],dtype='int16')
    Vstr=Sstr*0
    alive=np.array([1],dtype='bool')
    record=np.ndarray((len(Sstr),100),dtype='int16')
    
    game_start_time=time.time()
    printtime=1000
    Sstr,Vstr,record=do(Sstr,Vstr,record,1000)
    game_end_time=time.time()
    game_timeuse=0.00001+game_end_time-game_start_time
    print(Sstr)
    print(f'用时{game_timeuse}秒')
    print(f'显示了{printtime}次')
    print(f'平均帧数{printtime/game_timeuse}')
main()
