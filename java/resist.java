class Resist {
    public static void main(String[] args) {
        float S = 0;
        for (String r : args) {
            S += 1/Float.parseFloat(r);
        }
        float R = 1/S;
        System.out.println("Общее сопротивление равно: " + Math.round(R*100.0)/100.0 + " Ом");
           
    }
}

