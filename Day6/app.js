const CountToN= (x)=>
{

var absX=Math.abs(x);
let index=1;
while(index<=absX)
{
    console.log(index);
    index=index+1; //index++;index+=1
}

}

const numberPrompt = () => {
        while(true){

            let response = Number(prompt('Enter a Number'))
        }if (!isNaN(response)){
            return response;
        }


 


}