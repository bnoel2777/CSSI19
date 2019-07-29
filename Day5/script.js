







let result = prompt("Enter your name");
console.log("Hello, " ,result);

let num = prompt("Enter a number");
num = Number(num);

if(isNaN(num))
{
    num = 10;
} 
    num=num +10;
    console.log(num);

let num2 = prompt("Enter your grade");
num2 = Number(num2);

if(num2>=70 && Number){
    console.log("You passed with a",num2);
}
else{
    console.log("YOU FAILED! TRY AGAIN");
}