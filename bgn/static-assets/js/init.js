(function($){
  $(function(){

    $('.button-collapse').sideNav();

    var $container = $('#masonry-grid').masonry({
        itemSelector: '.game-item',
    });

    $container.imagesLoaded().progress( function() {
      $container.masonry('layout');
    });

    $('select').material_select();
    $('#id_time').pickadate({        
        format: 'mm/dd/yyyy',
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 15 // Creates a dropdown of 15 years to control year
    });
    $('textarea').addClass('materialize-textarea');

  }); // end of document ready
    
})(jQuery); // end of jQuery name space