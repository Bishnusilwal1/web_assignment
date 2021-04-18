function pageRedirect() {
    window.location.replace("https://www.tutorialrepublic.com/");
} 

(function($) {
    "use strict";
    jQuery(document).ready(function($) {
        $('.category-slide2').owlCarousel( {
            autoplay: false, 
            autoplaySpeed: 600, 
            nav: false, 
            dots: false, 
            loop: true, 
            margin:30, 
        }
        );
    }
    );
}

(jQuery))