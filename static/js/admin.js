$( document ).ready(function() {
    console.log( "ready!" );

    $('#usersTable').DataTable({
        columns: [
            {orderable: false, searchable: true},   // Login
            {orderable: true, searchable: true},    // Role
            {orderable: true, searchable: true},    // Jméno
            {orderable: false, searchable: true},   // Bydliště
            {orderable: true, searchable: true},    // Email
            {orderable: false, searchable: true},   // Telefon
            {orderable: false, searchable: true},   // Hodnocení
            {orderable: true, searchable: true},    // Ověření
            {orderable: false, searchable: false},  // Edit
            {orderable: false, searchable: false}]  // Smazat
      });
    
    $('#animalsTable').DataTable({
        columns: [
            {orderable: true, searchable: true},    // Jméno
            {orderable: true, searchable: true},    // Pohlaví
            {orderable: true, searchable: true},    // Barva
            {orderable: false, searchable: true},   // Váha
            {orderable: true, searchable: true},    // Výška
            {orderable: true, searchable: true},    // Druh
            {orderable: false, searchable: true},   // Plemeno
            {orderable: true, searchable: true},    // Kód
            {orderable: false, searchable: false},  // Edit
            {orderable: false, searchable: false}]  // Smazat
    });

    $('#eventsTable').DataTable({
        columns: [
            {orderable: true, searchable: true},    // Druh události
            {orderable: true, searchable: true},    // Jméno osoby
            {orderable: true, searchable: true},    // Email
            {orderable: false, searchable: true},   // Začátek
            {orderable: true, searchable: true},    // Konec
            {orderable: true, searchable: true},    // Jméno zvířete
            {orderable: false, searchable: true},   // Druh
            {orderable: true, searchable: true},    // Kód
            {orderable: false, searchable: true},   // Popis
            {orderable: false, searchable: false},  // Edit
            {orderable: false, searchable: false}]  // Smazat
    });
});
