using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace exec
{
    internal class Pessoa
    {
        string name;
        string cpf;
        int idade;


        public string Name { get => name; set => name = value; }
        public string Cpf { get => cpf; set => cpf = value; }
        public int Idade { get => idade; set => idade = value; }







        public Pessoa(string name, string cpf, int idade)
        {
            this.name = name;
            this.cpf = cpf;
            this.idade = idade;




        }



        public override string ToString()
        {
            return "Name:"+name+", Cpf:"+cpf+", Idade:"+idade;
        }
        








    }
    



}
