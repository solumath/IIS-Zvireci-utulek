$(document).ready(function () {
    console.log("ready!");

    $('#eventsTable').DataTable({
        columns: [
            { orderable: true, searchable: true },    // Druh události
            { orderable: true, searchable: true },    // Jméno osoby
            { orderable: true, searchable: true },    // Email
            { orderable: false, searchable: true },   // Začátek
            { orderable: true, searchable: true },    // Konec
            { orderable: true, searchable: true },    // Jméno zvířete
            { orderable: false, searchable: true },   // Popis
            { orderable: false, searchable: false },  // Edit
            { orderable: false, searchable: false }]  // Smazat
    });
});
