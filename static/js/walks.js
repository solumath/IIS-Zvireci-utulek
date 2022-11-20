$( document ).ready(function() {
    console.log( "ready!" );

    $('.deleteWalk').on('submit', function(e){
        const id = $(this).find('input[name="id"]').val();
        const url = $(this).find('input[name="url"]').val();
        const formData = {id: id};
                
        $.ajax({
            type: "DELETE",
            url: url,
            data: formData,
            dataType: "json"
        });
    });
});
