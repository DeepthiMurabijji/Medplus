
from time import sleep


OHS = {

    'Interns': {

     'Ramchand': { 
         'slept': 'Done'
      },
     'Deepthi': {
         'slept': 'Not Done'
     },
     'Prashanth': {
         'slept': 'Yes'
     }

    }

}


# Keys, Values => Items

for keys, values in OHS.items():
    for a, b in values.items():
        for x, y in b.items():
            print(x,y)
