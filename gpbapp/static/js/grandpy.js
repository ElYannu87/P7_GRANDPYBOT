var form = document.querySelector("form");
var mapNumber = 0;

document.getElementById('submit_form').addEventListener('submit', (e) => {
  e.preventDefault();
  var userQuestion = document.getElementById('userQuestion').value;
  requestQuestionMap(userQuestion);
});

// Request the user question to the server and show item
function requestQuestionMap(userQuestion) {
    var reqQuestion = new XMLHttpRequest();
    var encodeVar = encodeURIComponent(userQuestion);
    reqQuestion.open("GET", "/question/" + encodeVar);
    reqQuestion.onreadystatechange = function () {
        if (reqQuestion.readyState == 4 && (reqQuestion.status >= 200 || reqQuestion.status == 0)) {
            var readData = JSON.parse(reqQuestion.responseText);
            console.log(reqQuestion.responseText)

            // Add a full result
            document.querySelector(".results").innerHTML += `
                <div id="result" class="block_result">
                  <div id="map` + mapNumber + `"></div>
                  <div id="wikiText">
                      <h3>Saviez vous que :</h3>
                      <div class="text">` + readData.story + `</div>
                      <a class="linkWiki" href="` + 'https://fr.wikipedia.org/wiki/' + readData.title + `">Cliquez ici pour en savoir plus</a>                
                  </div>
                </div>
            `;

            var map = new google.maps.Map(document.getElementById('map' + mapNumber), {
                zoom: 10,
                center: { lat: 48.856614, lng: 2.3522219 }
              });


           // Show the map
            var location = new google.maps.LatLng(readData.lat, readData.lng);
            map.setCenter(location);
            	var marker = new google.maps.Marker({
            	map: map,
            	position: (location),
            });
        } else {
            wrongQuestion = "Je n'ai pas compris votre question";
            document.querySelector(".text").innerHTML = wrongQuestion;
        }
    };
    reqQuestion.send(null);
}