$( document ).ready(function() {
    console.log( "ready!" );

    $('#usersTableAdmin').DataTable({
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
    
    $('#usersTableCaretaker').DataTable({
      columns: [
          {orderable: false, searchable: true},   // Login
          {orderable: true, searchable: true},    // Role
          {orderable: true, searchable: true},    // Jméno
          {orderable: false, searchable: true},   // Bydliště
          {orderable: true, searchable: true},    // Email
          {orderable: false, searchable: true},   // Telefon
          {orderable: false, searchable: true},   // Hodnocení
          {orderable: true, searchable: true}]    // Ověření
    });
});
