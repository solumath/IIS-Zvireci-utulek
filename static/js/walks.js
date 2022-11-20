$( document ).ready(function() {
    console.log( "ready!" );

    $('#futureTable').DataTable({
        columns: [
            {orderable: true, searchable: false},   // Index
            {orderable: true, searchable: true},    // Začátek
            {orderable: true, searchable: true},    // Konec
            {orderable: true, searchable: true},    // Jméno
            {orderable: false, searchable: true},   // Popis
            {orderable: false, searchable: false}]  // Smazat
    });
    
    $('#historyTable').DataTable({
      columns: [
            {orderable: false, searchable: true},   // Index
            {orderable: true, searchable: true},    // Začátek
            {orderable: true, searchable: true},    // Konec
            {orderable: true, searchable: true},    // Jméno
            {orderable: false, searchable: true}]   // Popis
    });

});
