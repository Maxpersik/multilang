//usr/local/bin/go run $0 $@; exit $?

package main

import "fmt"
import "os"
import "strconv"
import "math"

func main(){
    rA := os.Args[1:]
    S := 0.0
    for r := 0; r < len(rA); r++ {
        rI, err := strconv.ParseFloat(rA[r], 64)
        if err == nil {
            S += 1.0/rI
        }
    }
    R := 1.0/S
    fmt.Println("Общее сопротивление равно:", math.Round(R*100)/100,"Ом")
    





}
