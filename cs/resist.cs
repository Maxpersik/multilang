using System;

namespace Resist
{
    class Program
    {
        static void Main(string[] args)
        {
            double S = 0;
            double R = 0;
            for (int i = 0; i < args.Length; i++){
                S += 1/Convert.ToDouble(args[i]);
            }
            R = 1 / S;  
            Console.WriteLine(string.Format("Общее сопротивление равно: {0:N2} Ом", R));
            
         }   
    }
}

