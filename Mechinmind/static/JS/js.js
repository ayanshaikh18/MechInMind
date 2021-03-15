$('.copy_text').click(function (e) {
    e.preventDefault();
    var copyText = $(this).attr('href');

    document.addEventListener('copy', function (e) {
        e.clipboardData.setData('text/plain', copyText);
        e.preventDefault();
    }, true);

    document.execCommand('copy');
    console.log('copied text : ', copyText);
    alert('copied text: ' + copyText);
});


function openNav() {
    document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}


function opencat() {
    document.getElementById("myNav2").style.width = "100%";
}

function closecat() {
    document.getElementById("myNav2").style.width = "0%";
}


function opencat1(catId) {
    $.ajax({
            type: "GET",
            url: "/articles/getSubCategories/",
            data: {
                'id': catId
            },
            success: function (data) {
                var navbar = $(".overlay-content3")
                navbar.empty()
                $.each(data, function (key, value) {
                    navbar.append(`<a href="/articles/getArticlesBySubCategories/${key}">${value}</a><br>`)
                })
            }
        }
    )
    document.getElementById("myNav3").style.width = "100%";
}

function closecat1() {
    document.getElementById("myNav3").style.width = "0%";
}


function opencat2() {
    document.getElementById("myNav4").style.width = "100%";
}

function closecat2() {
    document.getElementById("myNav4").style.width = "0%";
}


function opencat4() {
    document.getElementById("myNav5").style.width = "100%";
}

function closecat4() {
    document.getElementById("myNav5").style.width = "0%";
}


$(document).ready(function () {
    /**********
     BOTTOM SCROLL TOP BUTTON
     **********/

        // declare variable
    var scrollTop = $(".scrollTop");

    $(window).scroll(function () {
        // declare variable
        var topPos = $(this).scrollTop();

        // if user scrolls down - show scroll to top button
        if (topPos > 100) {
            $(scrollTop).css("opacity", "1");

        } else {
            $(scrollTop).css("opacity", "0");
        }

    }); // scroll END

    //Click event to scroll to top
    $(scrollTop).click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 900);
        return false;

    }); // click() scroll top EMD

    /*************
     LEFT MENU SMOOTH SCROLL ANIMATION
     *************/
    // declare variable

}); // ready() END

$(document).ready(function () {

    // Add class to mailto link
    // Needed to separate the disabling of the default action AND copy email to clipboard
    $('a[href^=mailto]').addClass('mailto-link');

    var mailto = $('.mailto-link');

    mailto.append('<span class="mailto-message"></span>');

    // Disable email client
    $('a[href^=mailto]').click(function () {
        return false;
    })

    // On click, get href and remove 'mailto:' from value
    // Store email address in a variable.
    mailto.click(function () {
        var href = $(this).attr('href');
        var email = href.replace('mailto:', '');
        copyToClipboard(email);
        setTimeout(function () {
        }, 2000);
    });

});

// Copies the email variable to clipboard
function copyToClipboard(text) {
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
    dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand('copy');
    document.body.removeChild(dummy);
}