using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exec
{
    internal class Program
    {
        static void Main(string[] args)

        {
            Pessoa pessoa1 = new Pessoa("Joao","123456",2);
            pessoa1.Name = "Carlos";
            pessoa1.Cpf = "123";
            pessoa1.Idade = 17;
            
            Console.WriteLine("{0}-{1}-{2}",pessoa1.Name,pessoa1.Cpf,pessoa1.Idade);
            




        }
    }
}

