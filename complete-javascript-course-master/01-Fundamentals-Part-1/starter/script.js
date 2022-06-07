
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


// Truthy and Falsy Values...........................
// 5 falsy values: 0, '', undefined, null, NaN

console.log(Boolean(0));         // output : false 
console.log(Boolean(undefined));   // output : false
console.log(Boolean('Jonas'));     // output : true
console.log(Boolean({}));         // output : true
console.log(Boolean(''));       // output : false

// so conversion to boolean is always implicit not explicit or in other words it always type coercion 
// when does JS convert to boolean??

// two scenarios :  1) logical operator   2) logical context 
// eg: if else statement



// equality operator 
const age = 18;
if (age === 18 )  console.log('adult ');  // if statement if we have only one line in the block 
// no need of parathesis
// it is strict has it does not perform type coercion

// whereas ==

'18' == 18;    // output : true  as it performs type coercion
// this is called loose equality operator
'18' === 18 ; // output : false as it does not  performs type coercion
18 == 18    // output : true 



// prompt function

const favourite = prompt("what's your favourite number?");
console.log(favourite);
console.log(typeof favourite);


if (favourite == 23)
{
    console.log('23 is a number // type coercion ')
}
if (favourite === 23){
    console.log("23 is a string ");
}


// converted to number 
const favourite = Number(prompt("what's your favourite number?"));
console.log(favourite);
console.log(typeof favourite);


if (favourite == 23)
{
    console.log('23 is a number // type coercion ')
}
if (favourite === 23){
    console.log("23 is a string ");    // it is valid after it  is converted to Number
}
else if (favourite === 7)
{
    console.log('number is 7');
}
else 
{
    console.log('number is different ' );
}


// strict version of operator
if (favourite !== 23) console.log('Why not 23 // strict version');


// loose version of operator

if (favourite != 23) console.log('Why not 23 // loose version');



const hasDriversLicense = true;
const hasGoodVision = false;

console.log(hasDriversLicense && hasGoodVision);
console.log(hasDriversLicense || hasGoodVision);
console.log(!hasDriversLicense);

const isTired = true;

console.log(hasDriversLicense && hasGoodVision || isTired);      // output : false 
//          true                  false           false

console.log(hasDriversLicense && hasGoodVision || isTired); // output : true 
//           true                 false            true 

console.log(hasDriversLicense && hasGoodVision && !isTired); // output : false
//          true                    false           false



// switch case 

const day = 'wednesday';

switch (day) {
    case 'monday':         // day === 'monday'
        console.log('plan course structure');
        break;
    case 'tuesday':
        console.log('tuesday');
        break;
    case 'wednesday':                           //  day = 'wednesday'     output: thrusday 
        // console.log('wednesday');
        // break;                    // herer wednesday and thursday are condition of  'OR' any one of the days 
    case 'thursday':                             //  day ='thursday'      output: thursday 
        console.log('thursday');
        break;
    case 'friday':
        console.log('friday');
        break;
    case 'saturday':
        // console.log('saturday');
        // break;
    case 'sunday':
        console.log('sunday');
        break;
    default:
        console.log('Not valid day');

}

// switch case is nothing but else if statements 

// if don't put break the code simply continues to excute till the end 

// above code in if else statement 


if (day === 'monday')
{
    console.log('monday');
}
else if (day === 'tuesday')
{
    console.log('tuesday');
}
else if (day === 'wednesday' || day === 'thursday')
{
    console.log('wednesday or thursday');
}
else if (day ==='friday')
{
    console.log('friday');
}
else if (day === 'saturday' || day === 'sunday')
{
    console.log('weekend');
}
else 
{
    console.log('Not a valid day');
}



// expressions produce values 
// statements doesnot produce values

// Ternary operator...

const age = 22;
age >= 18 ? console.log('I would like wine 🍷') : console.log('I would like water 💧');
//condition               if/true                     else /false

const drink = age >= 18 ? 'wine 🥂' : 'water💧';
console.log(drink);

console.log(`I would like to drink ${age >= 18 ? 'wine 🍾':'water 💧'}`);
*/

const bill = 275;
const tip = bill <= 300 && bill >= 50 ? bill * 0.15 : bill * 0.2;
//              condition               true             false  
console.log(`the bill is ${bill}, the tip is ${tip} and the total value is ${bill + tip}`); 
