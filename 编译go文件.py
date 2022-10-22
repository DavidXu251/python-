
data='''
package main
import "fmt"
import "time"

func main(){
    fmt.Println("hello")
    time.Sleep(30*1000_000_000)
}
'''

file=open('go文件.go', 'w')
file.write(data)
file.close()

import os
os.system('cmd /K go run go文件.go')


