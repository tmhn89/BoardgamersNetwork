$( document ).ready(function() {

    function initialize() {
    // Function for initalizing map on the page

        // Location of the user
        var user_latlng = new google.maps.LatLng(user_location_x, user_location_y);

        // Define where the map will be loaded
        var mapCanvas = document.getElementById('map');

        // Map options, more can be found here
        // https://developers.google.com/maps/documentation/javascript/reference#MapOptions
        var mapOptions = {
            center: user_latlng,
            zoom: 12,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };
        var map = new google.maps.Map(mapCanvas, mapOptions);


        var userInfoWin = new google.maps.InfoWindow({content: "My location"});
        var user_location = new google.maps.Marker({
            map: map,
            position: user_latlng,
            title: "My location",
        });
        google.maps.event.addListener(user_location, 'click', function(){
            userInfoWin.open(map, user_location);
        });

        // Edit styles for map
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
        function addMarkerToMap(map, name, latlng, type){
            var infoWin = new google.maps.InfoWindow({content: name});
            var marker = new google.maps.Marker({
                map: map,
                position: latlng,
                title: name,
            });
            if (type === 'events') {
                events_markers.push(marker);
            } else if (type === 'guilds') {
                guilds_markers.push(marker);
            } else {
                stores_markers.push(marker);
            }
            google.maps.event.addListener(marker, 'click', function(){
                infoWin.open(map, marker);
            });
        }

        function setMapOnAll(map, markerslist) {
            for (var i = 0; i < markerslist.length; i++) {
                markerslist[i].setMap(map);
            }
        }

        function clearMarkers(markerslist) {
            setMapOnAll(null, markerslist);
        }

        function addWantedMarkers(){
            // list of dicts
            var mappoints = [];
            if (document.getElementById('events').checked) {
                mappoints.push(event_dict);
                $( ".events" ).show();
            } else {
                clearMarkers(events_markers);
                events_markers = [];
                $( ".events" ).hide();
            }
            if (document.getElementById('guilds').checked) {
                mappoints.push(guild_dict);
                $( ".guilds" ).show();
            } else {
                clearMarkers(guilds_markers);
                guilds_markers = [];
                $( ".guilds" ).hide();
            }
            if (document.getElementById('stores').checked) {
                mappoints.push(store_dict);
                $( ".stores" ).show();
            } else {
                clearMarkers(stores_markers);
                stores_markers = [];
                $( ".stores" ).hide();
            }

            // go through the dict/dicts
            var type;
            for (var d in mappoints) {
                if (d == 0) {
                    type = 'events';
                } else if (d == 1) {
                    type  = 'guilds';
                } else {
                    type = 'stores';
                }

                var dict = mappoints[d];
                // for each key in dict add a marker to map
                for (var key in dict) {
                    name = key;
                    coordinates = dict[key];
                    latlng = new google.maps.LatLng(coordinates[0], coordinates[1]);
                    if (type === 'events') {
                        addMarkerToMap(map, name, latlng, type);
                    } else if (type === 'guilds') {
                        addMarkerToMap(map, name, latlng, type);
                    } else {
                        addMarkerToMap(map, name, latlng, type);
                    }
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
