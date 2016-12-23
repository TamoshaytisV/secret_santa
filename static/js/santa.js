/**
 * Created by hobo on 12/23/16.
 */

;(function () {

    var RaccoonSanta = {
        send_request: function (url) {
            $.ajax({
                url: url,
                type: "POST",
                success: function (data) {
                    console.log(data);
                },
            });
        }
    };

    window._ = RaccoonSanta;

})();