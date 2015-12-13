$( document ).ready(function() {

    function initialize() {
    // Function for initalizing map on the page

        var mapCanvas = document.getElementById('map');

        var mapOptions = {
            zoom: 12,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            scrollwheel: false,
        };
        var map = new google.maps.Map(mapCanvas, mapOptions);

        var infoWindow = new google.maps.InfoWindow({content: "My location"});

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                infoWindow.setPosition(pos);
                infoWindow.setContent('Location found.');
                map.setCenter(pos);
                addMarkerToMap(map, "My location", pos, "user");
            });
        }

        var user_location = new google.maps.Marker({
            map: map,
            title: "My location",
            icon: '/static-assets/marker_user.png'
        });
        google.maps.event.addListener(user_location, 'click', function(){
            userInfoWin.open(map, user_location);
        });

        // Styles for map
        map.set('styles', [
            {
                "featureType":"water",
                "elementType":"all",
                "stylers":[
                    {"hue":"#bbbbbb"},
                    {"saturation":-100},
                    {"lightness":-4},
                    {"visibility":"on"}
                ]
            },
            {
                "featureType":"landscape",
                "elementType":"all",
                "stylers":[
                    {"hue":"#999999"},
                    {"saturation":-100},
                    {"lightness":-33},
                    {"visibility":"on"}
                ]
            },
            {
                "featureType":"road",
                "elementType":"all",
                "stylers":[
                    {"hue":"#999999"},
                    {"saturation":-100},
                    {"lightness":-6},
                    {"visibility":"on"}
                ]
            },
            {
                "featureType":"poi",
                "elementType":"all",
                "stylers":[
                    {"hue":"#aaaaaa"},
                    {"saturation":-100},
                    {"lightness":-15},
                    {"visibility":"on"}
                ]
            }
        ]);

        var events_markers = [];
        var guilds_markers = [];
        var stores_markers = [];

        // Function for adding selected markers to map
        function addMarkerToMap(map, name, latlng, type){
            var infoWin = new google.maps.InfoWindow({content: name});
            var marker;

            if (type === 'events') {
                marker = new google.maps.Marker({
                    map: map,
                    position: latlng,
                    title: name,
                    icon: '/static-assets/marker_event.png'
                });
                events_markers.push(marker);
            } else if (type === 'guilds') {
                marker = new google.maps.Marker({
                    map: map,
                    position: latlng,
                    title: name,
                    icon: '/static-assets/marker_guild.png'
                });
                guilds_markers.push(marker);
            } else if (type === 'stores') {
                marker = new google.maps.Marker({
                    map: map,
                    position: latlng,
                    title: name,
                    icon: '/static-assets/marker_store.png'
                });
                stores_markers.push(marker);
            } else {
                marker = new google.maps.Marker({
                    map: map,
                    position: latlng,
                    title: name,
                    icon: '/static-assets/marker_user.png'
                });
            }
            google.maps.event.addListener(marker, 'click', function(){
                infoWin.open(map, marker);
            });
        }

        // Function used my clearMarkers()
        function setMapOnAll(map, markerslist) {
            for (var i = 0; i < markerslist.length; i++) {
                markerslist[i].setMap(map);
            }
        }
        // Clearing markers from map
        function clearMarkers(markerslist) {
            setMapOnAll(null, markerslist);
        }

        // Handle showing the right markers
        function addWantedMarkers(){
            var mappoints = {};
            if (document.getElementById('events').checked) {
                mappoints['events'] = event_dict;
                $( ".events" ).show();
            } else {
                clearMarkers(events_markers);
                events_markers = [];
                $( ".events" ).hide();
            }
            if (document.getElementById('guilds').checked) {
                mappoints['guilds'] = guild_dict;
                $( ".guilds" ).show();
            } else {
                clearMarkers(guilds_markers);
                guilds_markers = [];
                $( ".guilds" ).hide();
            }
            if (document.getElementById('stores').checked) {
                mappoints['stores'] = store_dict;
                $( ".stores" ).show();
            } else {
                clearMarkers(stores_markers);
                stores_markers = [];
                $( ".stores" ).hide();
            }

            // go through the dict/dicts
            for (var type in mappoints) {
                var dict = mappoints[type];
                // for each key in dict add a marker to map
                for (var name in dict) {
                    coordinates = dict[name];
                    latlng = new google.maps.LatLng(coordinates[0], coordinates[1]);
                    addMarkerToMap(map, name, latlng, type);
                }
            }
        }
        var mappoints = [event_dict, guild_dict, store_dict];
        $( "#check_map" ).change(function() {
            addWantedMarkers();
        });
        addWantedMarkers();
    }
    // call initialize function when the page is fully loaded
    google.maps.event.addDomListener(window, 'load', initialize);
});