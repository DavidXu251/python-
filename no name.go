
package main
import "fmt"
var print=fmt.Println

func main(){
    for count:=0; count<=30; count++{
        go func(){
            for i:=0; i<=30; i++{
            }
            print("hello",count)
        }()
    }
    for{}
}










































