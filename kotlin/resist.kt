import kotlin.math.round

fun main(args: Array<String>){
    var S = 0.0
    for (r in args) {
        S += 1/r.toFloat()
    }
    var R = 1.0 / S
    println("Общее сопроотивление равно: " + "%.2f".format(R).toString() + " Ом")
    
}
