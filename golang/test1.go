package main

import "fmt"

func main(){
    var x [5]int
    x[0] = 10
    x[1] = 14
    x[2] = 11
    x[3] = 16
    x[4] = 13
    
    m := 0
    for i := 0; i < 5; i++ {
        if x[i] > m {
            m = x[i]
        }
    }

    fmt.Println(m)
}
