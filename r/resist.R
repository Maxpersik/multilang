rA = commandArgs(trailingOnly=TRUE)

S <- 0
for (r in rA){
    S <- S + 1/strtoi(r)
}
R <- 1/S 

message("Общее сопротивление равно: ",round(R, digits = 2), ' Ом')

