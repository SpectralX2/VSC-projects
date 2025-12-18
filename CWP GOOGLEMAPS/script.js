function initMap(){
    var collegeSelection = document.getElementById("college");
    var modeSelection = document.getElementById("mode");
    var directionsButton = document.getElementById("get-directions");
    var map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 47.6562, lng: -122.3021},
        zoom: 11,
        fullscreenControl: false
    });
    //create a geocoder to look up locations
    var geocoder = new google.maps.Geocoder();
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer();
    directionsDisplay.setMap(map);
    
    var collegeMarker;
    var locationMarker;
    
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position){
            var location = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            var infoWindow = new google.maps.InfoWindow({
                content: "This is your location"
            });
            locationMarker = new google.maps.Marker({
                map: map,
                position: location
            });
            infoWindow.open(locationMarker.get('map'), locationMarker);
        });
        
    }
    
    collegeSelection.onchange = function(){
        var college = collegeSelection.value;
        directionsDisplay.setMap(null);
        directionsDisplay.setPanel(null);
        if(collegeMarker != null){
            collegeMarker.setMap(null);
        }
        geocoder.geocode({'address': college}, function(results, status){
           for (var i =0; i < results.length;i++){
               console.log(results[i].formatted_address);
           }
           collegeMarker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location 
           }); 
           
           
        });
        
    }
    
    directionsButton.onclick = function(){
        
        getRoute(directionsService,directionsDisplay,locationMarker.position,collegeMarker.position,modeSelection.value,map);
        
    }
}

function getRoute(directionsService, directionsDisplay,start,end,mode,map){
    directionsService.route({
        origin: start,
        destination:end,
        travelMode: mode
    }, function(response, status){
        directionsDisplay.setDirections(response);
        directionsDisplay.setMap(map);
        directionsDisplay.setPanel(document.getElementById("directions"));
    });
}