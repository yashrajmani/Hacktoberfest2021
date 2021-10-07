/*

🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺

*************************************

ENTER FIRST NUMBER ⤵️ hit enter

ENTER OPERATOR (+,-,*,/) ⤵️ hit enter

ENTER SECOND NUMBER ✔️ press submit

🔸🔸NOTE🔸🔸: 

🔹If your choise is +,- or /  

the numbers need to be INTEGERS

🔹Only if you have chosen *  

the numbers can be and DECIMAL

🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺

*************************************

*/

import java.util.Scanner;

public class CalculatorWithotOperators{    

static int reminder=0;

static String res="";

public static void main(String[] args) {

    try{

         Scanner in=new Scanner(System.in);

         double ad=in.nextDouble();

         String operator=in.next();

         double bd=in.nextDouble();

         System.out.printf("First number: %s%nOperator: %s%nSecond number: %s%n", String.valueOf(ad),operator,String.valueOf(bd));

         checkInput(ad,bd,operator.trim());

         in.close();

    }catch(Exception e){

        System.out.println("Your inputs are incorrect.Try again.");

    }

}

    

static void checkInput(double ad, double bd, String operator) {

    // check if the input numbers are integer numbers for operation +, -, / and conversion form double type to int (example 5.0 = 5) for further work

    if(operator.equals("+")||operator.equals("-")||operator.equals("/")) {

        int a=(int)ad;

        int b=(int)bd;

        //if the input numbers are not integers, code ends with execution

        if(ad!=a || bd!=b) {

            System.out.println("Your input is incorrect. Please enter a integers.");

            System.exit(0);

        }

        // find out which operation is being performed (depending on the input operator) and displaying the final result

        switch(operator) {

        case "+": 

            System.out.println("Result: ".concat(String.valueOf(add(a,b))));

            break;

        case "-":

            System.out.println("Result: ".concat(String.valueOf(subtract(a,b))));

            break;

        case "/":

            System.out.println("Result: ".concat(String.valueOf(divide(a,b))));

            break;

        }

    }

    else if(operator.equals("*")) System.out.println(multiple(ad,bd));

    // if the input operator does not respond to any of the +, -, *, /  code ends with execution

    else System.out.println("Your input is incorrect. Operator can be: -, +, * or /");

    

    

}

//sum of two integer can be obtained by XOR bitwise operator and carry can be obtained but AND bitwise operator. We also need to use signed left shift Java operator to add carry into sum.

static int add(int a,int b) { 

    int sum,carry; 

    do{ 

    //sum of two bits is A XOR B

    sum=a^b; 

    //carry is AND of two bits

    carry=a&b; 

    //we are calculating carry and keeping it in a separate variable, than we are storing sum of two numbers into variable a, and shifts carry to 1 bit by using signed left shift operator, in order to add into sum.

    a=sum; 

    //shifts carry to 1 bit to calculate sum

    b=carry<<1; 

    }while(b!=0); 

    return sum;

}

    

static int subtract(int a, int b){ 

// instead subtract we find sum for a+(-b) => a-b

// remeber that -b = (~b)+1

    return add(a,add(~b,1));

}

static int multiply(int a,int b){

    // 0 multiplied with anything gives 0 

    if(b==0) return 0;

    // add "a" one by one 

    // for example: 3*5=3+3+3+3+3

    else if(b>0) return (add(a,multiply(a, subtract(b,1))));

    //the case where "b" is negative

    else return -multiply(a,-b);        

}  

static int division(int a,int b) { 

    //we start by shifting the divisor left until it's greater than the dividend. We then repeatedly shift it right and for each right shift check whether that value is less than the intermediate we got after the last subtraction. If it's less, we subtract again and fill in a for that digit in our result. If it's greater, we "subtract 0" (don't do anything).When we've filled in all the digits, that's our result, and any amount left that we haven't subtracted yet is our remainder.

    int temp = 1;

    int quot = 0;

    while (b <= a) {

        b <<= 1;

        temp <<= 1;

    }

    while (temp > 1) {

        b >>= 1;

        temp >>= 1;

        if (a >= b) {

            a =subtract(a,b);    

            quot=add(quot,temp);          

        }

    }

    reminder=a;

    return  quot;

}   

    

static String multiple(double a, double b){

    //we find the decimal point position for "double a" and the number of digits behind the decimal point

    //after that, we convert the decimal number to the integer ignoring the decimal comma (5.24 => 524)

    int countA=0;

    String s=String.valueOf(a);

    int dot = s.indexOf('.'); 

    countA = subtract(subtract(s. length(),dot),1);

    int ai=Integer.parseInt(s.replace (".",""));   

    //we find the decimal point position for "double b" and the number of digits behind the decimal point

    //after that, we convert the decimal number to the integer ignoring the decimal comma (5.24 => 524)

    int countB=0;

    s=String.valueOf(b);

    dot=s.indexOf('.'); 

    countB = subtract(subtract(s. length(),dot),1);

    int bi=Integer.parseInt(s.replace (".",""));

    //multiplay numbers without decimal comma (integers)

    res=String.valueOf(multiply (ai,bi));

    //calculate total decimal places

    int pos=add(countA,countB);

    // if the inputs are integers return result

    if(pos==0) return res;

    // if the inputs are decimal numbers, need to arrange the result by placing a decimal point at the appropriate location

    return res.substring(0,subtract(res.length(),pos)).concat(".".concat(res.substring(subtract(res.length(),pos))));

}

static String divide(int a, int b) {

    boolean dot=false; //we assume that the result will be an integer(without dot)

    //we check if the number "b" is negative. If is negative, we convert it to positive(-1*b)

    int signB=1;

    if(b<0) {

        signB=-1;

    b=multiply(b,signB);

    }

    //we check if the number "a" is negative. If is negative, we convert it to positive (-1*a)

    int signA=1;

    if(a<0){

        signA=-1;

        a=multiply(a,signA);

    }

   //if the divisor greater than dividend, result will be decimal number

   if(a<b){ a=find(a,b); dot=true;}

   String sign="";

   // if some of inputs are negative number then result will be negative, except if both numbers are negative

   if(signA==-1||signB==-1) sign="-";

   if(signA==-1&&signB==-1) sign=""; res=sign.concat(res.concat(String.valueOf(division(a,b))));

   // if we have remainder, result will be decimal number

    if(reminder!=0&&dot==false) res=res.concat(".");

    //multiplay while has reminder, but result can't be over 10 digits(because of time limit exceed)

    while(reminder!=0) {

        res=res.concat(String.valueOf(division(multiply(reminder,10),b)));

        if(res.length()>10) return res;

    }

    return res;

}

static int find(int a, int b) {

    //this method find how much zero goes behind the decimal point (until divisor multiplied by 10 is greater than dividend)

    res=res.concat("0.");

    int count=0;

    while(a<b){

        count=add(count,1);

        if(count>1) res=res.concat("0");

        a=multiply(a,10);

    }

    return a;

}

}
