var form = document.querySelector("form");
// Bloque qui va contenir l'ensemble des résultats.
let main = document.getElementById('main');
// Bloc d'une seule réponse.
var result = document.getElementById("result");

document.getElementById('submit_form').addEventListener('submit', (e) => {
    e.preventDefault();
    let userQuestion = document.getElementById('userQuestion').value;
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
            // Init map
            let map1 = document.querySelector('.map')
            // Je vais réccupérer toutes les classes map
            let lesMaps = document.getElementsByClassName('map');
            console.log(lesMaps);
            //Je prends la dernière classe map
            let lastMap = lesMaps.item((lesMaps.length)-1);
            console.log(lastMap);
            let map = new google.maps.Map(lastMap, {
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
            // Show the Wiki Media text
            document.querySelector(".text").innerHTML += readData.story;
            var link = document.querySelector(".linkWiki");
            link.setAttribute('href', 'https://fr.wikipedia.org/wiki/' + readData.title);
            // Affichage dans le HTML
            let reponse = document.createElement('div');
            reponse.innerHTML = "<div class='map'></div>";
            reponse.innerHTML += "<div id=\"wikiText\">";
            reponse.innerHTML += "<h3>Saviez vous que :</h3>";
            reponse.innerHTML += "<p class='text'>" + readData.story + "</p>";
            reponse.innerHTML += "<a class='linkWiki' href=''>Cliquez ici pour en savoir plus</a></div>";
            main.appendChild(reponse)
        }
        result.style.display = "inline";
    };
    reqQuestion.send(null);
}