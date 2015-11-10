$( document ).ready(function() {

    function initialize() {
    // Function for initalizing map on the page

        // Define where the map will be loaded
        var mapCanvas = document.getElementById('map');

        // Map options, more can be found here
        // https://developers.google.com/maps/documentation/javascript/reference#MapOptions
        var mapOptions = {
            center: new google.maps.LatLng(60.186289, 24.828528),
            zoom: 12,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
        };
        var map = new google.maps.Map(mapCanvas, mapOptions);

        // Edit styles for map
        map.set('styles', [
            {
                stylers: [
                    { hue: "#ee6e73" },
                    { saturation: -20 }
                ]
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [
                    { lightness: 100 },
                    { visibility: "simplified" }
                ]
            }, {
                featureType: 'road',
                elementType: 'labels',
                stylers: [
                    { saturation: -100 },
                    { invert_lightness: true }
                ]
            }, {
                featureType: 'landscape',
                elementType: 'geometry',
                stylers: [
                    { hue: "#524E4E" },
                    { saturation: 10 },
                    { lightness: -20 },
                    { gamma: 1.51 }
                ]
            }, {
                featureType: "road",
                elementType: "labels",
                stylers: [
                    { visibility: "off" }
                ]
            }
        ]);

        function addMarker(map, name, latlng){
            var infoWin = new google.maps.InfoWindow({content: name});
            var marker = new google.maps.Marker({
                map: map,
                position: latlng,
                title: name,
            });
            google.maps.event.addListener(marker, 'click', function(){
                infoWin.open(map, marker);
            });
        }

        // add markers on the map
        for (var event_key in dict) {
            event_name = event_key;
            event_coordinates = dict[event_key];
            var latlng = new google.maps.LatLng(event_coordinates[0], event_coordinates[1]);
            addMarker(map, event_name, latlng);
        }

    }


    // call initialize function when the page is fully loaded
    google.maps.event.addDomListener(window, 'load', initialize);

});
