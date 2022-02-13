let from_state1 = document.getElementById('from_state1');
let from_state2 = document.getElementById('from_state2');
let from_state3 = document.getElementById('from_state3');
let to_state1 = document.getElementById('to_state1');
let to_state2 = document.getElementById('to_state2');
let to_state3 = document.getElementById('to_state3');

let defaultOption1 = document.createElement('option');
let defaultOption2 = document.createElement('option');
let defaultOption3 = document.createElement('option');
let defaultOption4 = document.createElement('option');
let defaultOption5 = document.createElement('option');
let defaultOption6 = document.createElement('option');

defaultOption1.text = 'Select State';
defaultOption2.text = 'Select State';
defaultOption3.text = 'Select State';
defaultOption4.text = 'Select State';
defaultOption5.text = 'Select State';
defaultOption6.text = 'Select State';

from_state1.add(defaultOption1);
from_state2.add(defaultOption2);
from_state3.add(defaultOption3);
to_state1.add(defaultOption4);
to_state2.add(defaultOption5);
to_state3.add(defaultOption6);

function init(){
    const url = 'https://geodata.solutions/restapi?country=India';
    fetch(url)  
      .then(  
        function(response) {  
          if (response.status !== 200) {  
            console.warn('Looks like there was a problem. Status Code: ' + 
              response.status);  
            return;  
          }
            response.json().then(function(data) {  
            let option1, option2, option3, option4, option5, option6;        
            for (let i = 0; i < data.details.regionalBlocs.length; i++) {
                option1 = document.createElement('option');
                option2 = document.createElement('option');
                option3 = document.createElement('option');
                option4 = document.createElement('option');
                option5 = document.createElement('option');
                option6 = document.createElement('option');
                option1.text = data.details.regionalBlocs[i].state_name;
                option2.text = data.details.regionalBlocs[i].state_name;
                option3.text = data.details.regionalBlocs[i].state_name;
                option4.text = data.details.regionalBlocs[i].state_name;
                option5.text = data.details.regionalBlocs[i].state_name;
                option6.text = data.details.regionalBlocs[i].state_name;
                from_state1.add(option1);
                from_state2.add(option2);
                from_state3.add(option3);
                to_state1.add(option4);
                to_state2.add(option5);
                to_state3.add(option6);
            }    
          });  
        }  
      )  
      .catch(function(err) {  
        console.error('Fetch Error -', err);  
      });
}

init()

function update_city(driver_city, driver_state){
    driver_city.length = 0;
    let loading = document.createElement('option');
    loading.text = "Loading..."
    driver_city.add(loading)
    const url = 'https://geodata.solutions/restapi?country=India&state=' + driver_state.value;
    fetch(url)  
    .then(  
        function(response) {  
            if (response.status !== 200) {  
                console.warn('Looks like there was a problem. Status Code: ' + 
                response.status);  
                return;  
            }
            response.json().then(function(data) {  
            driver_city.length = 0;
            let option;  
            for (let i = 0; i < Object.keys(data).length; i++) {
                option = document.createElement('option');
                option.text = data[i].city_name;
                driver_city.add(option);
              }          
          });  
        }  
      )  
      .catch(function(err) {  
        console.error('Fetch Error -', err);  
      });
}


from_state1.addEventListener('change', () => {
    let from_city1 = document.getElementById('from_city1');
    let defaultOption1 = document.createElement('option');
    defaultOption1.text = 'Select City';
    from_city1.add(defaultOption1);
    update_city(from_city1, from_state1)
})

from_state2.addEventListener('change', () => {
    let from_city2 = document.getElementById('from_city2');
    let defaultOption2 = document.createElement('option');
    defaultOption2.text = 'Select City';
    from_city2.add(defaultOption2);
    update_city(from_city2, from_state2)
})
from_state3.addEventListener('change', () => {
    let from_city3 = document.getElementById('from_city3');
    let defaultOption3 = document.createElement('option');
    defaultOption3.text = 'Select City';
    from_city3.add(defaultOption3);
    update_city(from_city3, from_state3)
})

to_state1.addEventListener('change', () => {
    let to_city1 = document.getElementById('to_city1');
    let defaultOption4 = document.createElement('option');
    defaultOption4.text = 'Select City';
    to_city1.add(defaultOption4);
    update_city(to_city1, to_state1)
})

to_state2.addEventListener('change', () => {
    let to_city2 = document.getElementById('to_city2');
    let defaultOption5 = document.createElement('option');
    defaultOption5.text = 'Select City';
    to_city2.add(defaultOption5);
    update_city(to_city2, to_state2)
})

to_state3.addEventListener('change', () => {
    let to_city3 = document.getElementById('to_city3');
    let defaultOption6 = document.createElement('option');
    defaultOption6.text = 'Select City';
    to_city3.add(defaultOption6);
    update_city(to_city3, to_state3)
})