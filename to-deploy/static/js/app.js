$(document).ready(function(){
    $('.tab').on('click', function() {
        var tabname = $(this).data('tabname');
        $('.tab-content').addClass('hide');
        $('.tab-content[data-tabname="'+tabname+'"]').removeClass('hide');
        $('.tab').removeClass('active');
        $('.tab[data-tabname="'+tabname+'"]').addClass('active');
    });
});
