(function($){
  $(function(){

    $('.button-collapse').sideNav();

    var $container = $('#masonry-grid').masonry({
        itemSelector: '.game-item',
    });

    $container.imagesLoaded().progress( function() {
      $container.masonry('layout');
    });
    
  }); // end of document ready
    
})(jQuery); // end of jQuery name space