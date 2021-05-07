var aR = process.argv;
var S = 0, R = 0;
for (var i = 2; i < aR.length; i++){
    S += 1/aR[i]; 
}
R = 1.0/S;
console.log("Общее сопротивление равно: " + Math.round(R*100)/100 + " Ом");
