$(document).ready(function(){
    $('.tab').on('click', function() {
        var tabname = $(this).data('tabname');
        $('.tab-content').addClass('hide');
        $('.tab-content[data-tabname="'+tabname+'"]').removeClass('hide');
        $('.tab').removeClass('active');
        $('.tab[data-tabname="'+tabname+'"]').addClass('active');
    });
});

window.onload = function(){
    SC.initialize({
        client_id: 'e6cd33d3f7b5e434c0b1d20491181fe0'
    });

    var track_url = 'http://soundcloud.com/forss/flickermood';
    SC.oEmbed(track_url, { auto_play: true }, function(oEmbed) {
        console.log('oEmbed response: ', oEmbed);
        if (oEmbed) {
            $('#songs').html(oEmbed.html);
        } else {
            $('.sidebar').addClass('hide');
        }
    });
};
