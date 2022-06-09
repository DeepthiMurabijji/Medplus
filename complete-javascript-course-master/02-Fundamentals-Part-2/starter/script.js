'use strict';

/*
let hasDriversLicense = false;
const passTest = true;
if (passTest) hasDriversLicense = true;
if (hasDriversLicense) console.log("I can drive 🚕") 

//   without [use strict]   and with error hasDriverLicense
// the output :  _______

// same without [use strict] but correct variable name hasDriversLicense
// the output : I can drive 🚕

// with [use strict] and with error hasDriverLicense
// the output : it show an error  
// Uncaught ReferenceError: hasDriverLicense is not defined at script.js:5:32

// with [use strict] and no error hasDriverLicense
// the output : I can drive 🚕


// const interface = 'Audio';
// const private = 534;
// output: it shows an error message 
// Uncaught SyntaxError: Unexpected strict mode reserved word (at script.js:21:7)



// functions:

function logger()
{
    console.log("My name is Jonas");
}

logger();         // caling  / running / invoking function 
logger();           // you can call any number of times 


function fruitProcessor(apples , oranges)
{
    //console.log(apples , oranges);
    const juice = `juice with ${apples} apples and ${oranges} oranges.`;
    return juice;
}

fruitProcessor(5, 3);     // output : 5 3 
const appleJuice = fruitProcessor(5 ,3);
console.log(appleJuice);           // output : juice with 5 apples and 3 oranges.

console.log(fruitProcessor(5,0));  // output :  juice with 5 apples and 0 oranges.


// function declaration

const age1 = calcAge1(1991);
function calcAge1(birthYeah)
{
    return  2037 - birthYeah;
    
}

//const age1 = calcAge1(1991);         in this case you can call it befor declaring 
console.log(age1);


// function expression 

//const age2 = calcAge2(1991);          Here you can cannot call before declaration 
const calcAge2 = function (birthYeah)
{
    return 2037 - birthYeah;
}
const age2 = calcAge2(1991);
console.log(age2);


// Arrow functions
const calcAge3 = birthYeah => 2037 - birthYeah;
const age3 = calcAge3(1991);
console.log(age3);

const yearsUntiRetirement = (birthYeah, firstName) =>{
    const age = 2037 - birthYeah;
    const retirement = 65 - age;
   // return retirement;
   return `${firstName} retires in ${retirement} years`;
}

console.log(yearsUntiRetirement(1991,'Jonas'));
console.log(yearsUntiRetirement(1980,'Bob')); 


function cutFruitPieces(fruit)
{
    return fruit * 4;
}

function fruitProcessor (apples, oranges)
{
    const applePieces = cutFruitPieces(apples);
    const orangePieces = cutFruitPieces(oranges);
    const juice = `juice with ${applePieces} apples pieces and ${orangePieces} oranges pieces.`
    return juice;
}
console.log(fruitProcessor(2,3)); 


// Arrays : 

const friend1 = 'Michael';
const friend2 = 'Steven';
const friend3 = 'Peter';

const friends = ['Michael' , 'Steven', 'Peter'];
console.log(friends);

const years = new Array(1991, 1984, 2008, 2020);

console.log(friends[0]);
console.log(friends[2]);

console.log(friends.length);
console.log(friends[friends.length - 1]);
friends[2] = 'Jay';
console.log(friends);
// friends = ['Bob', 'Alice'];      output :  error 
// script.js:128 Uncaught TypeError: Assignment to constant variable. at script.js:128:9   

const firstName = "Jonas";
const jonas = [firstName, "Schmedtmann", 2037- 1991, "teacher", friends];
console.log(jonas);

const calcAge = function (birthYeah)
{
    return 2037 - birthYeah;
}
const y = [1990,1967,2002,2010,2018];
console.log(calcAge(y));              // output: NaN

const age1 = calcAge(y[0]);
const age2 = calcAge(y[1]);
const age3 = calcAge(y[y.length - 1]);
console.log(age1, age2, age3);
const ages = [calcAge(y[0]), calcAge(y[1]), calcAge(y[y.length-1])];
console.log(ages);

//  1️⃣ difference in adding a new element to the array (at the end) 
const friends = ['Michael' , 'Steven', 'Peter'];
friends.push('Jay');
console.log(friends);

// 2️⃣ difference in adding a new element to the array (at the end)
const friends = ['Michael' , 'Steven', 'Peter'];
const newfriend = friends.push('Jay');
console.log(friends);                // output: (4) ['Michael', 'Steven', 'Peter', 'Jay']
console.log(newfriend);              // output: 4


// 3️⃣ add element at the beginning


friends.unshift('John');
console.log(friends);                       // output: (4) ['John', 'Michael', 'Steven', 'Peter']

// 4️⃣ to Remove elements 
friends.pop();          // last element
const popped = friends.pop();
console.log(popped);                        // output:  peter 
console.log(friends);                       // output:  (3) ['John', 'Michael', 'Steven']

friends.shift();        // remove first element
console.log(friends);                        // output: (2) ['Michael', 'Steven']

// index of element
console.log(friends.indexOf('steven'));     // output: -1  for element which is not present
console.log(friends.indexOf('Steven'));     // output: 1 

// includes ....
console.log(friends.includes("Steven"));      // output: true 
console.log(friends.includes("Bob"));         // output: false 
friends.push(23);
console.log(friends.includes("23"));          // output: false    
console.log(friends.includes(23));            // output: true 
// AS it follows strict equality   i.e it does not do type coercion



// Objects 🎈🎈

const jonas = {
    firstName: 'Jonas',
    lastName: 'Schmedtmann',
    age: 2037 - 1991,
    job: 'teacher',
    friends: ['Michael', 'Peter', 'Steven']
};

console.log(jonas);
// dot notation  ‟ • ”  (Member Access) 
console.log(jonas.lastName);            // output: Schmedtmann
// bracket notation  ‟ [] ”   (computer member access)
console.log(jonas['lastName']);         // output: Schmedtmann

const nameKey = 'Name';
console.log(jonas['first' + nameKey]);           // output:  Jonas
console.log(jonas['last' + nameKey]);           // output:  Schmedtmann

// same in dot notation
// you will get an error,  as we need to use a real property name here
// 🚫console.log(jonas.'last' + nameKey)            // output: ❌Uncaught SyntaxError: Unexpected string (at script.js:212:19)

const interestedIn = prompt('What do you want to know about Jonas ?');
//  console.log(interestedIn);        // input: job      output: job
// console.log(jonas.interestedIn);    // input: job      output: undefined
//👆 we try to access a property on an object that does not exist  .... as jonas doesnot have a property called  'interestedIn'

// now let's try using bracket notation []
console.log(jonas[interestedIn]);        // input: job       output: teacher  

// if you try to access a property on an object that does not exist it will show undefined even in bracket notation
// eg:    input : location             output: undefined

// 👇to add a property to an object

jonas.location = 'Portugal';
jonas['twitter'] = '@jonasschmedtman';
console.log(jonas);

// challenge
console.log(`${jonas.firstName} has ${jonas.friends.length} friends,and his best friend is ${jonas.friends[0]}`);


// object Methods 
const jonas = {
    firstName: 'Jonas',
    lastName: 'Schmedtmann',
    birthYeah: 1991,
    job: 'teacher',
    friends: ['Michael', 'Peter', 'Steven'],
    hasDriversLicense: true,


    // calcAge: function (birthYeah)
    // {
    //     return 2037 - birthYeah;
    // }
    calcAge: function (){
        //console.log(this);                         // output: {firstName: 'Jonas', lastName: 'Schmedtmann', birthYeah: 1991, job: 'teacher', friends: Array(3), …}
        this.age = 2037 - this.birthYeah;
        return this.age;
    },
    getSummary : function() {
        return `${this.firstName} is a ${this.calcAge()} -years old ${jonas.job}, and he has ${this.hasDriversLicense ? 'a' : 'no'} driver's License.`;

    }
};

console.log(jonas.calcAge());
console.log(jonas.age);
//console.log(jonas.calcAge(1992));               // output : 45
// console.log(jonas['calcAge'](1991));            // output: 46 

console.log(jonas.getSummary());

*/

// iteration : for loop 🔄



for(let rep = 1; rep <=10; rep++) 
{
    console.log(`lifting weight ${rep} 🏋️‍♀️`);
}
