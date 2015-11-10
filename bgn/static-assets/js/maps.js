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


        // add some markers on the map
        var myCenter = new google.maps.LatLng(60.187058, 24.834908);
        var OneEvent = new google.maps.LatLng(60.186797, 24.833648);
        var AnotherEvent =  new google.maps.LatLng(60.187331, 24.823403);

        var marker = new google.maps.Marker({
            position: myCenter,
            map: map,
            title: 'Event!',
            // icon: 'http://i.imgur.com/ktFR7U8.png'
        });
        var marker1 = new google.maps.Marker({
            position: OneEvent,
            map: map,
            title: 'Event!',
            // icon: 'http://i.imgur.com/ktFR7U8.png'
        });
        var marker2 = new google.maps.Marker({
            position: AnotherEvent,
            map: map,
            title: 'Event!',
            // icon: 'http://i.imgur.com/ktFR7U8.png'
        });
    }


    // call initialize function when the page is fully loaded
    google.maps.event.addDomListener(window, 'load', initialize);

});
