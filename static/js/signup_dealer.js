let from_state1 = document.getElementById('from_state');
let to_state1 = document.getElementById('to_state');

let defaultOption1 = document.createElement('option');
let defaultOption2 = document.createElement('option');

defaultOption1.text = 'Select State';
defaultOption2.text = 'Select State';

from_state1.add(defaultOption1);
to_state1.add(defaultOption2);

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
                option1.text = data.details.regionalBlocs[i].state_name;
                option2.text = data.details.regionalBlocs[i].state_name;
                from_state1.add(option1);
                to_state1.add(option2);
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
    let from_city1 = document.getElementById('from_city');
    let defaultOption1 = document.createElement('option');
    defaultOption1.text = 'Select City';
    from_city1.add(defaultOption1);
    update_city(from_city1, from_state1)
})

to_state1.addEventListener('change', () => {
    let to_city1 = document.getElementById('to_city');
    let defaultOption4 = document.createElement('option');
    defaultOption4.text = 'Select City';
    to_city1.add(defaultOption4);
    update_city(to_city1, to_state1)
})

