/**
 * Created by hobo on 12/23/16.
 */

;(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var RaccoonSanta = {
        send_request: function (url) {
            $.ajax({
                url: url,
                type: "POST",
                success: function (data) {
                    $('#santa_button').remove();
                    $('#santa_result').html(
			"<div><p>Your Presentee is <span id='presentee'></span></p></div><div><img src='/static/images/wohoo.gif' class='img-responsive center-block'/></div>"
		    );
                    $('#presentee').html(data.presentee_name);
                }
            });
        }
    };

    window.RaccoonSanta = RaccoonSanta;

})();
