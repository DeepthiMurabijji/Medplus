
/*
let js = "amazing";
// if (js === 'amazing') alert("javascript");

console.log(40 + 8 + 23 - 10);
console.log("jonas");

let firstname = "jonas";

// 
//#we cannot use numbers in decalration of variabls like 
// they cannot star with numbers
// they can only contain numbers ,letters, underscores and dollar signs 

// FIXME:  let 3years =3;

// eg: let function =27;  =>> let $function = 27; or let _function = 27; 
//       let new = 27;   because these are reserved keywords

// eg: let Person ='jonas';  don't start variable with capital letters
//#region


let jonas_matilda = 'JM';
let $function = 27;

let person = 'jonas';
let PI = 3.1415;

let myFirstJob = 'Programmer';
let myCurrentJob = 'Bussiness';


let job1 = 'programmer';
let job2 = 'teacher';

true;
console.log(true);
console.log(typeof true);

let javascript = true;        //we asigined a new  variable using let and type boolean
console.log(javascript);
console.log(typeof javascript);

console.log(typeof 23);
console.log(typeof 'jons');

javascript = 'YES';             //  example for Dynamic Typing we are reassigning the variable to another type string
console.log(typeof javascript);      // so there is no need of let this time as we reassigning variable 

let year;
console.log(year);              // example for Undefined datatype 
console.log(typeof year);

year = 1991;                      // reassigning again
console.log(typeof year);

//  hence this is regarded as a bug or error it is not an object ,it is just as type of  undefined returns undefined 
console.log(typeof null);        // it gives output as "object"

// where as let is  a mutable so that we can change it later 
const birthYear = 1991;   // const is an immutable variable 
//  birthYear = 1990;

// whereas var is a mutable so that we can change it later
var job = 'progarmmer';
job = 'doctor';

// * without using let Here ....... it still works 
lastName = 'schmedtmann';
console.log(lastName);

const now = 2037;
const agejonas = now - 1991;
const agesarah = now - 2018;
console.log(agejonas, agesarah);

console.log(agejonas * 2, agejonas / 10 , 2**3);

const firstName = 'Jonas';
const lastName = 'Schmedtmann';
console.log(firstName+ ''+ lastName);

let x = 10+ 5;
x += 10; // x = x + 10
x += 4;  // x = x + 4 
x++;     // x = x + 1
x--;     // x = x - 1 
console.log(x);      // output: 99


console.log(agejonas > agesarah);  // output: true 
console.log(agesarah >= 18);       // output: true

const isFullAge = agesarah >= 18;

console.log(now - 1991 > now - 2018);

console.log(25 - 10 - 5);        // output: 10    left to right operation 


let X, Y;

X = Y = 25 - 10 - 5;  // output:  x = y = 10  ,x = 10
// right to left operation 
console.log(X,Y);

//const averageAge = agejonas + agesarah / 2    // output: 46 19 55.5 
const averageAge = (agejonas + agesarah) / 2    // output: 46 19 32.5 
console.log(agejonas , agesarah, averageAge);




const firstName = 'John';
const job = 'teacher';
const birthYear = 1991;
const year = 2037;

const jonas = "I'm" + firstName + ', a' + (year - birthYear) + 'years old' + job + '!';
console.log(jonas);


const jonasNew = `I'm ${firstName}, a ${year - birthYear} year old ${job} !`;
console.log(jonasNew);

console.log(`just a regular string.....`);      // Template Literals


console.log('String with  \n\
    multiple \n\
           lines ');

console.log(` String 
   with a 
        new line `);



const age = 19;
const isOldEnough = age >= 18;

if (isOldEnough)
{
    console.log('Sarah can start driving 🚗')
}

if else statement.

if {
    ...
} else {
    .... 
}



const age = 15;
 

if (age >= 18)
{
    console.log('Sarah can start driving 🚗')
}
else 
{
    const yearsLeft = 18 - age;
    console.log(`Sarah is too young to start driving
    Please wait for another ${yearsLeft} year 🚳`)
}

const birthYear = 1991;
if (birthYear <= 2000)
{
    let century =20;
}
else 
{
    let century = 21;
}

console.log(century);           // if century is defined inside the block then you will get an error
                                     Thus see the below code


const birthYear = 2012;               //const birthYear = 1991;
let century ;
if (birthYear <= 2000)
{
     century =20;
}
else 
{
     century = 21;
}

console.log(century);


Type conversion is when we manually convert from one type to another
Type coercion is when JavaScript automatically converts types behind the scenes for us 


// Type conversions
const inputYear = '1991';
console.log(inputYear + 18);
console.log(Number(inputYear), inputYear);
console.log(Number(inputYear) + 18);
console.log(Number('jonas'));    // output : NaN        as it is trying to convert a string to a number
console.log(typeof NaN);         // NaN  means an invalid number 
console.log(String(23) , 23 );       

// Type coercion
console.log(`I'am `+ 23 + 'Years old');       // here + actually converted number to a string
console.log('23' - '10' - 3);           // output : 10   and - converted string to a number
console.log('23' + '10' + 3);           // output : 23103
console.log('23' * '2');               // output : 46        now they are converted to numbers


let n = '1' + 1;
n = n - 1;
console.log(n);      // output :10

console.log(2+3+4+ '5');     // output :"95"
console.log('10' - '4'-'3'-2+'5');  // output : "1
*/



