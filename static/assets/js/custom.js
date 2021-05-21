/**************************************
 File Name: custom.js
 Template Name: Tech Blog
 Created By: HTML.Design
 http://themeforest.net/user/wpdestek
 **************************************/

(function ($) {
    "use strict";
    $(document).ready(function () {
        $('#nav-expander').on('click', function (e) {
            e.preventDefault();
            $('body').toggleClass('nav-expanded');
        });
        $('#nav-close').on('click', function (e) {
            e.preventDefault();
            $('body').removeClass('nav-expanded');
        });
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    $('.carousel').carousel({
        interval: 4000
    })

    $(window).load(function () {
        $("#preloader").on(500).fadeOut();
        $(".preloader").on(600).fadeOut("slow");
    });

    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 1) {
            jQuery('.dmtop').css({bottom: "25px"});
        } else {
            jQuery('.dmtop').css({bottom: "-100px"});
        }
    });
    jQuery('.dmtop').click(function () {
        jQuery('html, body').animate({scrollTop: '0px'}, 800);
        return false;
    });

})(jQuery);


function openCategory(evt, catName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(catName).style.display = "block";
    evt.currentTarget.className += " active";
}

function selectCategory(cateogry) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response)['result'];
            var myNewStr = "";
            for (var i = 0; i <= output.length-1; i++) {
                myNewStr += '<div class="col-lg-3 col-md-6 col-sm-12 col-xs-12">';
                myNewStr += '<div class="blog-box">';
                myNewStr += '<div class="post-media">';
                myNewStr += `<a target="_blank" href="${output[i].urlsdata}" title="">`;
                myNewStr += `<img src="${output[i].fullimage}" alt="" class="img-fluid">`;
                myNewStr += "<div class=\"hovereffect\"></div><span class=\"menucat\">Science</span></a></div>";
                myNewStr += "<div class=\"blog-meta\">"
                myNewStr += `<h4><a target="_blank" href="${output[i].urlsdata}" title="">${output[i]['title']}</a></h4>`
                myNewStr += "</div></div></div>"
            }
            document.getElementById('mynews').innerHTML = myNewStr;
        }
    };
    xhttp.open("GET", "navbarCategoryNews?cat=" + cateogry, true);
    xhttp.send();
}
